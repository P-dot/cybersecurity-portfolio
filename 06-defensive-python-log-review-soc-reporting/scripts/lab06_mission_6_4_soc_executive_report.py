#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime
import re
from collections import Counter, defaultdict


# ============================================================
# Lab 06.4 — SOC executive report generator
# ============================================================
# Pseudocode overview:
# 1. Read the technical event extraction report generated in Mission 6.3.
# 2. Parse the Markdown table of extracted events.
# 3. Group technical event types into executive SOC categories.
# 4. Detect known low-value/noise findings that should not be escalated.
# 5. Count events by category, event type and severity.
# 6. Build a cleaner SOC-style executive report.
# 7. Save the report as Markdown for evidence and GitHub documentation.


# ============================================================
# 1. Define lab paths
# ============================================================
# Idea:
# The script does not read raw system logs directly in this mission.
# It reads the structured technical report created in Mission 6.3 and
# converts it into a cleaner executive report.

LAB06_DIR = Path.home() / "lab06"
LAB06_EVIDENCE_DIR = LAB06_DIR / "evidencias"
LAB06_REPORTS_DIR = LAB06_DIR / "reportes"

INPUT_REPORT = LAB06_EVIDENCE_DIR / "lab06_03_defensive_pattern_extraction.md"
OUTPUT_REPORT = LAB06_REPORTS_DIR / "lab06_04_soc_executive_report.md"


# ============================================================
# 2. Define executive categories
# ============================================================
# Idea:
# The technical report contains detailed event types.
# A SOC executive report should group them into categories that are easier
# to understand: security-relevant, operational/technical, lab infrastructure,
# audit activity and residual noise.

CATEGORY_MAP = {
    "Authentication failure": "Security-relevant events",
    "Sudo authentication failure": "Security-relevant events",
    "Sudo incorrect password attempts": "Security-relevant events",
    "SSH authentication activity": "Security-relevant events",

    "Sudo command execution": "Privileged activity / audit trail",
    "Scheduled root cron session": "Privileged activity / audit trail",

    "Failed service": "Operational / technical issues",
    "DNS or network issue": "Operational / technical issues",
    "Storage capacity warning": "Operational / technical issues",

    "VirtualBox shared-folder failure": "Lab infrastructure events",
    "VirtualBox shared-folder success": "Lab infrastructure events",
    "Kernel or virtualization warning": "Lab infrastructure events",
}

CATEGORY_ORDER = [
    "Security-relevant events",
    "Privileged activity / audit trail",
    "Operational / technical issues",
    "Lab infrastructure events",
    "Noise / low-value findings",
]


# ============================================================
# 3. Define simple noise indicators
# ============================================================
# Idea:
# Mission 6.3 already reduced noise, but we saw one residual false positive:
# a line like "systemd-timesync **Never logged in**".
# Here we explicitly downgrade that kind of finding into a low-value/noise bucket.

KNOWN_NOISE_PATTERNS = [
    "**Never logged in**",
    "never logged in",
]


# ============================================================
# 4. Utility functions
# ============================================================

def read_text_safely(file_path: Path) -> str:
    """
    Read a text file safely.

    Intention:
    Avoid breaking the script if a file contains unexpected characters.
    """
    return file_path.read_text(encoding="utf-8", errors="replace")


def clean_markdown_text(text: str, max_length: int = 260) -> str:
    """
    Prepare text for Markdown output.

    Intention:
    Keep report rows readable and avoid Markdown tables breaking because of pipes.
    """
    cleaned = text.strip().replace("|", "\\|")

    if len(cleaned) > max_length:
        return cleaned[:max_length] + "..."

    return cleaned


def is_known_noise(event_text: str) -> bool:
    """
    Decide whether an extracted event is a known low-value/noise finding.

    Intention:
    Separate false positives from findings that deserve analyst attention.
    """
    lower_text = event_text.lower()

    for pattern in KNOWN_NOISE_PATTERNS:
        if pattern.lower() in lower_text:
            return True

    return False


def map_event_to_category(event_type: str, event_text: str) -> str:
    """
    Map a technical event type to an executive category.

    Intention:
    Convert technical rows into a SOC-style summary structure.
    """
    if is_known_noise(event_text):
        return "Noise / low-value findings"

    return CATEGORY_MAP.get(event_type, "Operational / technical issues")


# ============================================================
# 5. Parse the Mission 6.3 Markdown event table
# ============================================================
# Expected table format:
# | ID | Event type | Source file | Line | Severity | Extracted event | Analyst note |
# | 1  | ...        | ...         | 150  | Low      | `event text`    | note         |


def parse_event_row(line: str) -> dict | None:
    """
    Parse one Markdown table row from the Mission 6.3 report.

    Intention:
    Extract structured fields from a Markdown row without re-reading raw logs.
    """
    stripped = line.strip()

    # Ignore non-table lines quickly.
    if not stripped.startswith("|"):
        return None

    # Only rows that start with a numeric ID are event rows.
    if not re.match(r"^\|\s*\d+\s*\|", stripped):
        return None

    # This regex expects seven columns:
    # ID, event type, source file, line, severity, extracted event, analyst note.
    match = re.match(
        r"^\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*`?(.*?)`?\s*\|\s*(.*?)\s*\|$",
        stripped,
    )

    if not match:
        return None

    event_id, event_type, source_file, line_number, severity, event_text, analyst_note = match.groups()

    return {
        "id": int(event_id),
        "event_type": event_type.strip(),
        "source_file": source_file.strip(),
        "line_number": int(line_number),
        "severity": severity.strip(),
        "event_text": event_text.strip(),
        "analyst_note": analyst_note.strip(),
    }


def parse_events_from_report(report_text: str) -> list[dict]:
    """
    Parse all extracted events from the Mission 6.3 technical report.

    Intention:
    Convert the technical Markdown evidence into Python dictionaries for counting,
    grouping and executive reporting.
    """
    events = []

    for line in report_text.splitlines():
        parsed_event = parse_event_row(line)

        if parsed_event is None:
            continue

        executive_category = map_event_to_category(
            parsed_event["event_type"],
            parsed_event["event_text"],
        )

        parsed_event["executive_category"] = executive_category
        events.append(parsed_event)

    return events


# ============================================================
# 6. Build counts and findings
# ============================================================

def count_by_field(events: list[dict], field_name: str) -> Counter:
    """
    Count events by one dictionary field.

    Intention:
    Reuse the same logic for categories, severities and event types.
    """
    return Counter(event[field_name] for event in events)


def group_events_by_category(events: list[dict]) -> dict[str, list[dict]]:
    """
    Group events by executive category.

    Intention:
    Make it easy to print short samples and category summaries.
    """
    grouped = defaultdict(list)

    for event in events:
        grouped[event["executive_category"]].append(event)

    return grouped


def event_type_exists(events: list[dict], event_type: str) -> bool:
    """
    Check whether a given event type appears in the parsed events.
    """
    return any(event["event_type"] == event_type for event in events)


def build_key_findings(events: list[dict]) -> list[str]:
    """
    Build short executive findings from the extracted event set.

    Intention:
    Translate counts into SOC-style statements that a recruiter, team lead
    or technical manager can understand quickly.
    """
    findings = []
    category_counts = count_by_field(events, "executive_category")
    severity_counts = count_by_field(events, "severity")

    findings.append(
        f"The script reviewed {len(events)} extracted technical events from Mission 6.3 and grouped them into executive SOC categories."
    )

    if category_counts.get("Security-relevant events", 0) > 0:
        findings.append(
            "Security-relevant events were observed, mainly authentication and sudo-related failures. In this lab context they are interpreted as low to low-medium severity unless repetition, remote origin or unexpected users are confirmed."
        )

    if event_type_exists(events, "SSH authentication activity"):
        findings.append(
            "SSH authentication activity was identified and should be reviewed for source IP, username and expected exposure."
        )
    else:
        findings.append(
            "No clear SSH authentication activity was extracted from the reviewed evidence."
        )

    if category_counts.get("Operational / technical issues", 0) > 0:
        findings.append(
            "Operational and technical issues were present, including failed services, DNS/network problems or storage capacity warnings. These affect reliability and evidence collection more than direct compromise indicators in this lab."
        )

    if category_counts.get("Lab infrastructure events", 0) > 0:
        findings.append(
            "Several findings are related to the virtualized lab environment, especially VirtualBox shared-folder behavior and kernel/virtualization warnings."
        )

    if category_counts.get("Noise / low-value findings", 0) > 0:
        findings.append(
            "Residual low-value noise was detected and separated from analyst-relevant findings, improving report quality compared with raw keyword matching."
        )

    if severity_counts.get("High", 0) == 0 and severity_counts.get("Critical", 0) == 0:
        findings.append(
            "No high or critical severity finding was identified by the static rules used in this lab."
        )

    findings.append(
        "No clear evidence of compromise is concluded by this script; final judgment requires analyst review and correlation."
    )

    return findings


def build_recommended_actions(events: list[dict]) -> list[str]:
    """
    Build recommended SOC actions based on observed categories and event types.

    Intention:
    Convert event extraction into practical next steps without overclaiming.
    """
    actions = []
    category_counts = count_by_field(events, "executive_category")

    if category_counts.get("Security-relevant events", 0) > 0:
        actions.append(
            "Review authentication and sudo failures for repetition, unexpected users, remote origin, unusual timing and affected accounts."
        )

    if event_type_exists(events, "Sudo command execution"):
        actions.append(
            "Keep sudo command execution as an audit trail and review commands only if user, path or timing is unexpected."
        )

    if event_type_exists(events, "Failed service"):
        actions.append(
            "Review failed services by business or system criticality; fwupd-refresh failures can be treated as maintenance/update issues in this lab."
        )

    if event_type_exists(events, "DNS or network issue"):
        actions.append(
            "Check DNS, gateway, NAT and external update reachability when updates or package refreshes fail."
        )

    if event_type_exists(events, "Storage capacity warning"):
        actions.append(
            "Monitor free space in the shared evidence export folder to avoid future collection or reporting failures."
        )

    if category_counts.get("Lab infrastructure events", 0) > 0:
        actions.append(
            "Document VirtualBox and lab-infrastructure warnings as environmental baseline unless they combine with instability or suspicious activity."
        )

    actions.append(
        "Use this executive report together with the technical event table from Mission 6.3; do not use it as a standalone incident verdict."
    )

    return actions


# ============================================================
# 7. Build the executive Markdown report
# ============================================================

def build_markdown_report(events: list[dict], input_report_exists: bool) -> str:
    """
    Build the final SOC executive report in Markdown.

    Intention:
    Produce a readable report that separates evidence, interpretation,
    limitations and recommended actions.
    """
    report_lines = []
    category_counts = count_by_field(events, "executive_category")
    event_type_counts = count_by_field(events, "event_type")
    severity_counts = count_by_field(events, "severity")
    grouped_events = group_events_by_category(events)
    key_findings = build_key_findings(events) if events else []
    recommended_actions = build_recommended_actions(events) if events else []

    report_lines.append("# Lab 06.4 — SOC executive report")
    report_lines.append("")
    report_lines.append(f"Date: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC")
    report_lines.append("")

    report_lines.append("## Executive summary")
    report_lines.append("")

    if not input_report_exists:
        report_lines.append(
            "The Mission 6.3 technical report was not found, so no executive analysis could be generated."
        )
        report_lines.append("")
        report_lines.append("## Mission status")
        report_lines.append("")
        report_lines.append("Mission 6.4 completed with missing input report.")
        report_lines.append("")
        return "\n".join(report_lines)

    if not events:
        report_lines.append(
            "The Mission 6.3 report was found, but no extractable event rows were parsed."
        )
    else:
        report_lines.append(
            f"This report converts {len(events)} technical events from Mission 6.3 into an executive SOC-style summary. "
            "Findings are grouped into security-relevant events, privileged/audit activity, operational issues, lab infrastructure events and residual low-value noise."
        )
        report_lines.append("")
        report_lines.append(
            "The reviewed evidence does not automatically prove compromise. The output supports analyst review by summarising what deserves attention and what appears to be expected lab or operational noise."
        )

    report_lines.append("")
    report_lines.append("## Scope")
    report_lines.append("")
    report_lines.append(f"- Input technical report: `{INPUT_REPORT}`")
    report_lines.append(f"- Output executive report: `{OUTPUT_REPORT}`")
    report_lines.append("- Source context: Lab 05 Linux evidence processed through Lab 06.3 defensive pattern extraction")
    report_lines.append("- Method: static parsing, counting, categorisation and analyst-oriented summarisation")
    report_lines.append("")

    if events:
        report_lines.append("## Category summary")
        report_lines.append("")
        report_lines.append("| Executive category | Events |")
        report_lines.append("|---|---:|")

        for category in CATEGORY_ORDER:
            report_lines.append(f"| {category} | {category_counts.get(category, 0)} |")

        report_lines.append("")

        report_lines.append("## Severity summary")
        report_lines.append("")
        report_lines.append("| Severity | Events |")
        report_lines.append("|---|---:|")

        for severity, total in severity_counts.most_common():
            report_lines.append(f"| {severity} | {total} |")

        report_lines.append("")

        report_lines.append("## Event type summary")
        report_lines.append("")
        report_lines.append("| Event type | Events |")
        report_lines.append("|---|---:|")

        for event_type, total in event_type_counts.most_common():
            report_lines.append(f"| {event_type} | {total} |")

        report_lines.append("")

        report_lines.append("## Key findings")
        report_lines.append("")

        for finding in key_findings:
            report_lines.append(f"- {finding}")

        report_lines.append("")

        report_lines.append("## Representative samples by category")
        report_lines.append("")

        for category in CATEGORY_ORDER:
            category_events = grouped_events.get(category, [])
            report_lines.append(f"### {category}")
            report_lines.append("")

            if not category_events:
                report_lines.append("No events in this category.")
                report_lines.append("")
                continue

            report_lines.append("| Event type | Severity | Source | Line | Sample |")
            report_lines.append("|---|---|---|---:|---|")

            for event in category_events[:5]:
                sample = clean_markdown_text(event["event_text"])
                report_lines.append(
                    f"| {event['event_type']} | {event['severity']} | {event['source_file']} | "
                    f"{event['line_number']} | `{sample}` |"
                )

            report_lines.append("")

        report_lines.append("## Recommended analyst actions")
        report_lines.append("")

        for action in recommended_actions:
            report_lines.append(f"- {action}")

        report_lines.append("")

    report_lines.append("## SOC interpretation")
    report_lines.append("")
    report_lines.append(
        "This report is an analyst-support artifact. It summarises extracted findings and separates security-relevant events from operational issues, lab infrastructure events and residual noise."
    )
    report_lines.append("")
    report_lines.append(
        "It should not be interpreted as an autonomous detection engine or final incident decision. A real SOC workflow would require correlation with timestamps, users, source IPs, asset criticality, baselines, SIEM alerts and business context."
    )
    report_lines.append("")

    report_lines.append("## Limitations")
    report_lines.append("")
    report_lines.append("- Static rules only; no machine learning or behavioural baseline.")
    report_lines.append("- No enrichment with threat intelligence, IP reputation or asset inventory.")
    report_lines.append("- No timeline reconstruction across multiple systems.")
    report_lines.append("- No incident response action is performed.")
    report_lines.append("- Findings come from a controlled lab environment, not a production SIEM.")
    report_lines.append("")

    report_lines.append("## Conclusion")
    report_lines.append("")
    report_lines.append(
        "Mission 6.4 demonstrates the ability to convert technical log-extraction output into a clearer SOC-style executive report. The report helps separate review-worthy findings from operational and lab-context noise while preserving a conservative analyst interpretation."
    )
    report_lines.append("")

    report_lines.append("## Mission status")
    report_lines.append("")
    report_lines.append("Mission 6.4 completed pending review.")
    report_lines.append("")

    return "\n".join(report_lines)


# ============================================================
# 8. Main execution flow
# ============================================================

def main() -> None:
    """
    Main function.

    Pseudocode:
    1. Ensure the report output directory exists.
    2. Check whether the Mission 6.3 report exists.
    3. If it exists, parse its event table.
    4. Build an executive SOC report from the parsed events.
    5. Save the report and print a short execution summary.
    """
    LAB06_REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    input_report_exists = INPUT_REPORT.exists()
    events = []

    if input_report_exists:
        technical_report_text = read_text_safely(INPUT_REPORT)
        events = parse_events_from_report(technical_report_text)

    executive_report = build_markdown_report(events, input_report_exists)
    OUTPUT_REPORT.write_text(executive_report, encoding="utf-8")

    print(f"Report created: {OUTPUT_REPORT}")
    print(f"Parsed events: {len(events)}")


# ============================================================
# 9. Script entry point
# ============================================================
# This ensures the script only runs when executed directly, not when imported.

if __name__ == "__main__":
    main()
