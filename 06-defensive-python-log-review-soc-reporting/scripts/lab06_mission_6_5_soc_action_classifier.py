#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime
from collections import Counter


# ==========================================================
# Lab 06.5 — Basic SOC action classifier
# ==========================================================
# Defensive goal:
# Convert the technical event table from Mission 6.3 into an
# initial SOC action table.
#
# This script does NOT decide that an incident occurred.
# It only maps extracted events to conservative analyst actions:
# Review, Monitor, Document, No escalation or Needs analyst attention.
# ==========================================================


# ----------------------------------------------------------
# 1. Define input and output paths.
#
# Idea:
# We do not re-read raw logs here. Mission 6.3 already extracted
# classified technical events. Mission 6.5 adds an operational SOC
# decision layer on top of that evidence.
# ----------------------------------------------------------

LAB06_DIR = Path.home() / "lab06"
INPUT_REPORT = LAB06_DIR / "evidencias" / "lab06_03_defensive_pattern_extraction.md"
OUTPUT_DIR = LAB06_DIR / "reportes"
OUTPUT_REPORT = OUTPUT_DIR / "lab06_05_soc_action_classifier.md"


# ----------------------------------------------------------
# 2. Define event types that require special handling.
#
# Idea:
# Some event types should not be treated the same way:
# - authentication and sudo failures require review;
# - technical issues require monitoring;
# - audit events should be documented;
# - lab infrastructure noise should not be escalated.
# ----------------------------------------------------------

SECURITY_REVIEW_EVENTS = {
    "Authentication failure",
    "Sudo authentication failure",
    "SSH authentication activity",
}

ATTENTION_EVENTS = {
    "Sudo incorrect password attempts",
    "Storage capacity warning",
}

MONITOR_EVENTS = {
    "Failed service",
    "DNS or network issue",
}

DOCUMENT_EVENTS = {
    "Sudo command execution",
    "Scheduled root cron session",
    "VirtualBox shared-folder success",
}

NO_ESCALATION_EVENTS = {
    "Kernel or virtualization warning",
    "VirtualBox shared-folder failure",
}


# ----------------------------------------------------------
# 3. Read text safely.
#
# Idea:
# The report is Markdown text. We read it as UTF-8 and replace
# undecodable characters instead of crashing.
# ----------------------------------------------------------

def read_text_safely(file_path: Path) -> str:
    return file_path.read_text(encoding="utf-8", errors="replace")


# ----------------------------------------------------------
# 4. Split one Markdown table row.
#
# Idea:
# Mission 6.3 created a Markdown table. Each event is stored as a row.
# We trim the leading/trailing pipe symbols and split columns.
# ----------------------------------------------------------

def split_markdown_row(row: str) -> list[str]:
    cleaned = row.strip()

    if cleaned.startswith("|"):
        cleaned = cleaned[1:]

    if cleaned.endswith("|"):
        cleaned = cleaned[:-1]

    return [column.strip() for column in cleaned.split("|")]


# ----------------------------------------------------------
# 5. Parse extracted events from the Mission 6.3 report.
#
# Idea:
# We only want rows from the "Extracted events" table.
# Header rows and separator rows are ignored.
# Each valid event row becomes a dictionary with the fields we need.
# ----------------------------------------------------------

def parse_events_from_report(report_text: str) -> list[dict]:
    events = []
    inside_events_table = False

    for line in report_text.splitlines():
        stripped = line.strip()

        if stripped == "## Extracted events":
            inside_events_table = True
            continue

        if inside_events_table and stripped.startswith("## "):
            break

        if not inside_events_table:
            continue

        if not stripped.startswith("|"):
            continue

        if stripped.startswith("| ID") or stripped.startswith("|---"):
            continue

        columns = split_markdown_row(stripped)

        if len(columns) < 7:
            continue

        raw_id = columns[0]

        if not raw_id.isdigit():
            continue

        events.append({
            "id": int(raw_id),
            "event_type": columns[1],
            "source_file": columns[2],
            "line_number": columns[3],
            "severity": columns[4],
            "sample": columns[5],
            "analyst_note": columns[6],
        })

    return events


# ----------------------------------------------------------
# 6. Detect residual low-value noise.
#
# Idea:
# In Mission 6.3 we noticed one example of residual noise:
# "systemd-timesync **Never logged in**".
# It contains a system-like keyword but is not really a security event.
# ----------------------------------------------------------

def is_low_value_noise(event: dict) -> bool:
    sample = event["sample"].lower()

    low_value_fragments = [
        "never logged in",
        "**never logged in**",
    ]

    return any(fragment in sample for fragment in low_value_fragments)


# ----------------------------------------------------------
# 7. Assign a SOC action to one event.
#
# Idea:
# This is the core classifier. It maps an event type to:
# - action: what the analyst should initially do;
# - priority: how urgent it is in this lab context;
# - rationale: why that action makes sense.
#
# Important:
# These are conservative lab rules, not production-grade incident logic.
# ----------------------------------------------------------

def classify_soc_action(event: dict) -> dict:
    event_type = event["event_type"]

    if is_low_value_noise(event):
        return {
            "action": "No escalation",
            "priority": "P4",
            "rationale": (
                "Residual low-value noise detected. Document as parser limitation; "
                "do not escalate without additional suspicious context."
            ),
        }

    if event_type in ATTENTION_EVENTS:
        return {
            "action": "Needs analyst attention",
            "priority": "P2",
            "rationale": (
                "Event may affect security review or evidence collection. Analyst should "
                "confirm context, repetition, affected user/system and operational impact."
            ),
        }

    if event_type in SECURITY_REVIEW_EVENTS:
        return {
            "action": "Review",
            "priority": "P3",
            "rationale": (
                "Security-relevant event. Review user, source, timing, repetition and "
                "whether the activity was expected in the lab or production context."
            ),
        }

    if event_type in MONITOR_EVENTS:
        return {
            "action": "Monitor",
            "priority": "P3",
            "rationale": (
                "Operational issue observed. Monitor for recurrence and assess whether it "
                "affects updates, availability, collection or reporting reliability."
            ),
        }

    if event_type in DOCUMENT_EVENTS:
        return {
            "action": "Document",
            "priority": "P4",
            "rationale": (
                "Expected or useful audit-trail activity. Keep as context, but do not "
                "escalate unless user, command, timing or frequency is unexpected."
            ),
        }

    if event_type in NO_ESCALATION_EVENTS:
        return {
            "action": "No escalation",
            "priority": "P4",
            "rationale": (
                "Lab infrastructure or virtualization-related finding. Treat as baseline/noise "
                "unless combined with instability or other suspicious evidence."
            ),
        }

    return {
        "action": "Review",
        "priority": "P3",
        "rationale": (
            "Unmapped event type. Review manually and decide whether it should be "
            "monitored, documented or escalated."
        ),
    }


# ----------------------------------------------------------
# 8. Enrich every event with SOC action fields.
#
# Idea:
# We keep the original technical fields and add the new operational decision:
# action, priority and rationale.
# ----------------------------------------------------------

def build_action_events(events: list[dict]) -> list[dict]:
    action_events = []

    for event in events:
        decision = classify_soc_action(event)

        enriched_event = {
            **event,
            "action": decision["action"],
            "priority": decision["priority"],
            "rationale": decision["rationale"],
        }

        action_events.append(enriched_event)

    return action_events


# ----------------------------------------------------------
# 9. Build counters for summary sections.
#
# Idea:
# A SOC report should not only list events. It should also show totals by
# action, priority and event type so an analyst can quickly understand workload.
# ----------------------------------------------------------

def build_counters(action_events: list[dict]) -> dict:
    return {
        "by_action": Counter(event["action"] for event in action_events),
        "by_priority": Counter(event["priority"] for event in action_events),
        "by_event_type": Counter(event["event_type"] for event in action_events),
    }


# ----------------------------------------------------------
# 10. Convert counters to Markdown tables.
#
# Idea:
# This keeps the reporting code clean and avoids repeating table logic.
# ----------------------------------------------------------

def build_counter_table(counter: Counter, first_column_name: str) -> list[str]:
    lines = []
    lines.append(f"| {first_column_name} | Events |")
    lines.append("|---|---:|")

    for key, value in counter.most_common():
        lines.append(f"| {key} | {value} |")

    return lines


# ----------------------------------------------------------
# 11. Build the final Markdown report.
#
# Idea:
# The output is a SOC-style action report: summary first, then the full
# classifier table, then interpretation and limitations.
# ----------------------------------------------------------

def build_markdown_report(action_events: list[dict]) -> str:
    counters = build_counters(action_events)
    report_lines = []

    report_lines.append("# Lab 06.5 — Basic SOC action classifier")
    report_lines.append("")
    report_lines.append(f"Date: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC")
    report_lines.append("")

    report_lines.append("## Executive summary")
    report_lines.append("")
    report_lines.append(
        f"This report maps {len(action_events)} extracted technical events from Mission 6.3 "
        "to initial SOC analyst actions. The goal is to support triage by separating "
        "events that should be reviewed, monitored, documented or not escalated."
    )
    report_lines.append("")
    report_lines.append(
        "No automatic incident verdict is produced. Actions are conservative and must be "
        "validated by an analyst using context, repetition, source, users and operational impact."
    )
    report_lines.append("")

    report_lines.append("## Scope")
    report_lines.append("")
    report_lines.append(f"- Input technical report: `{INPUT_REPORT}`")
    report_lines.append(f"- Output action report: `{OUTPUT_REPORT}`")
    report_lines.append("- Method: static rule-based action mapping")
    report_lines.append("- Environment: controlled defensive lab")
    report_lines.append("")

    report_lines.append("## Action summary")
    report_lines.append("")
    report_lines.extend(build_counter_table(counters["by_action"], "SOC action"))
    report_lines.append("")

    report_lines.append("## Priority summary")
    report_lines.append("")
    report_lines.extend(build_counter_table(counters["by_priority"], "Priority"))
    report_lines.append("")

    report_lines.append("## Event type summary")
    report_lines.append("")
    report_lines.extend(build_counter_table(counters["by_event_type"], "Event type"))
    report_lines.append("")

    report_lines.append("## SOC action table")
    report_lines.append("")

    if not action_events:
        report_lines.append("No events were parsed from the input report.")
        report_lines.append("")
    else:
        report_lines.append(
            "| ID | Event type | Severity | Action | Priority | Source | Line | Rationale | Sample |"
        )
        report_lines.append("|---:|---|---|---|---|---|---:|---|---|")

        for event in action_events:
            report_lines.append(
                f"| {event['id']} | {event['event_type']} | {event['severity']} | "
                f"{event['action']} | {event['priority']} | {event['source_file']} | "
                f"{event['line_number']} | {event['rationale']} | {event['sample']} |"
            )

        report_lines.append("")

    report_lines.append("## Action guidance")
    report_lines.append("")
    report_lines.append("- **Needs analyst attention**: review first; validate impact, repetition and context.")
    report_lines.append("- **Review**: inspect user, origin, timing, frequency and expected activity.")
    report_lines.append("- **Monitor**: watch recurrence and operational impact before escalating.")
    report_lines.append("- **Document**: keep as audit trail or operational context.")
    report_lines.append("- **No escalation**: treat as lab/environment noise unless correlated with other suspicious indicators.")
    report_lines.append("")

    report_lines.append("## SOC interpretation")
    report_lines.append("")
    report_lines.append(
        "This classifier represents a basic SOC L1 triage layer. It helps translate "
        "technical events into initial operational actions, but it does not replace "
        "human analyst judgment or a production SIEM workflow."
    )
    report_lines.append("")
    report_lines.append(
        "A real production workflow would require correlation across time, users, source IPs, "
        "asset criticality, authentication sources, endpoint telemetry and business context."
    )
    report_lines.append("")

    report_lines.append("## Limitations")
    report_lines.append("")
    report_lines.append("- Static rules only; no behavioural baseline or adaptive scoring.")
    report_lines.append("- No ticket creation, alert dispatching or incident response action.")
    report_lines.append("- No enrichment with IP reputation, threat intelligence or asset inventory.")
    report_lines.append("- Findings come from a controlled lab environment.")
    report_lines.append("- Priorities are educational and conservative, not production SLA definitions.")
    report_lines.append("")

    report_lines.append("## Conclusion")
    report_lines.append("")
    report_lines.append(
        "Mission 6.5 demonstrates how Python can support a SOC workflow by assigning "
        "initial analyst actions to extracted security and operational events. The output "
        "helps move from evidence extraction to triage decision support."
    )
    report_lines.append("")

    report_lines.append("## Mission status")
    report_lines.append("")
    report_lines.append("Mission 6.5 completed pending review.")
    report_lines.append("")

    return "\n".join(report_lines)


# ----------------------------------------------------------
# 12. Main execution flow.
#
# Idea:
# Prepare output folder, check input report, parse events, classify them,
# generate Markdown and write the final action report.
# ----------------------------------------------------------

def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if not INPUT_REPORT.exists():
        raise FileNotFoundError(f"Input report not found: {INPUT_REPORT}")

    technical_report = read_text_safely(INPUT_REPORT)
    extracted_events = parse_events_from_report(technical_report)
    action_events = build_action_events(extracted_events)

    report = build_markdown_report(action_events)
    OUTPUT_REPORT.write_text(report, encoding="utf-8")

    print(f"Report created: {OUTPUT_REPORT}")
    print(f"Parsed events: {len(extracted_events)}")
    print(f"Classified actions: {len(action_events)}")


# ----------------------------------------------------------
# 13. Script entry point.
#
# Idea:
# This makes the script executable from the terminal while keeping the
# main logic inside functions that are easier to read, test and maintain.
# ----------------------------------------------------------

if __name__ == "__main__":
    main()
