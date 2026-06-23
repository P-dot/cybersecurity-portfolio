#!/usr/bin/env python3

"""
Lab 06.3 - Defensive pattern extraction

Purpose:
    Read selected Lab 05 evidence files, filter simple report noise,
    extract defensive events that look closer to real operational log findings,
    and generate a Markdown report for SOC-style review.

Safety:
    This script only reads evidence files and writes a new report.
    It does not use sudo, modify logs, change services, scan networks,
    install packages or perform offensive activity.
"""

from pathlib import Path
from datetime import datetime
import re


# ============================================================
# 1. Define lab paths
# ============================================================
# Intention:
#   The script needs a controlled input folder and a controlled output folder.
#
# Input:
#   Lab 05 evidence files already generated during the Linux log monitoring lab.
#
# Output:
#   A new Lab 06 Markdown report with extracted defensive events.

LAB05_EVIDENCE_DIR = Path.home() / "lab05" / "evidencias"
LAB06_DIR = Path.home() / "lab06"
LAB06_EVIDENCE_DIR = LAB06_DIR / "evidencias"

OUTPUT_REPORT = LAB06_EVIDENCE_DIR / "lab06_03_defensive_pattern_extraction.md"


# ============================================================
# 2. Select the evidence files to analyse
# ============================================================
# Intention:
#   We do not analyse every file blindly.
#   We select the Lab 05 evidence files that contain the most log-like content.
#
# Why these files?
#   - lab05_02 contains authentication, sudo, sessions and SSH checks.
#   - lab05_03 contains failed services, warnings, syslog, journalctl and dmesg.
#
# Why not 5.4 and 5.5 here?
#   They are already reports written in Markdown. Analysing them would add
#   too much report text and increase false positives.

SOURCE_FILES = [
    "lab05_02_auth_sudo_sessions.txt",
    "lab05_03_system_health_errors.txt",
]


# ============================================================
# 3. Limit repeated event types
# ============================================================
# Intention:
#   A SOC report should be readable. If a file contains 200 sudo lines,
#   we do not want to flood the report with all of them.
#
# This limit keeps up to 10 examples per event type.

MAX_EVENTS_PER_TYPE = 10


# ============================================================
# 4. Read files safely
# ============================================================
# Intention:
#   Read a text evidence file and return it as a list of lines.
#
# Why errors="replace"?
#   If a file contains an unusual character, the script will not crash.
#   The unusual character will be replaced and the analysis can continue.

def read_lines_safely(file_path: Path) -> list[str]:
    content = file_path.read_text(encoding="utf-8", errors="replace")
    return content.splitlines()


# ============================================================
# 5. Clean log lines for Markdown output
# ============================================================
# Intention:
#   Markdown tables use the pipe character "|" as a column separator.
#   If a log line contains "|", it could break the report table.
#
# This function escapes "|" and also shortens very long lines.

def clean_for_markdown(text: str, max_length: int = 240) -> str:
    cleaned = text.strip().replace("|", "\\|")

    if len(cleaned) > max_length:
        return cleaned[:max_length] + "..."

    return cleaned


# ============================================================
# 6. Filter obvious report noise
# ============================================================
# Intention:
#   In Lab 06.2, keyword search counted headings, Markdown tables and grep commands.
#   Here we reduce that noise before trying to classify events.
#
# Examples of noise:
#   - Markdown headings: "### SSH service status"
#   - Table rows: "| File | Exists |"
#   - Helper commands: "COMMAND=/usr/bin/grep ..."
#   - Empty lines and report status lines
#
# Important:
#   This is a simple rule-based filter. It is useful, but not perfect.

def is_noise_line(line: str) -> bool:
    stripped = line.strip()

    # Empty lines do not carry event information.
    if not stripped:
        return True

    # Lines starting with these prefixes are usually report formatting,
    # table headers, summaries or command output labels rather than events.
    noise_prefixes = (
        "#",
        "===",
        "---",
        "|",
        "Date:",
        "LOAD",
        "ACTIVE",
        "SUB",
        "total ",
        "Filesystem",
        "Mem:",
        "Swap:",
        "END OF",
    )

    if stripped.startswith(noise_prefixes):
        return True

    # These fragments usually indicate report text, status text or helper searches,
    # not the original event itself.
    noise_fragments = [
        "No sample lines found",
        "Mission status",
        "completed pending review",
        "Mission 6.",
        "Keyword group",
        "Matching lines",
        "Evidence inventory",
        "COMMAND=/usr/bin/grep",
        "COMMAND=/bin/grep",
        "grep -Ei",
        "grep -i",
    ]

    lower_line = stripped.lower()

    for fragment in noise_fragments:
        if fragment.lower() in lower_line:
            return True

    return False


# ============================================================
# 7. Extract disk usage percentage
# ============================================================
# Intention:
#   Some df -h lines include a percentage such as "86%".
#   We extract it to classify high storage usage.
#
# Example input:
#   Capturas 465G 396G 69G 86% /mnt/capturas
#
# Output:
#   86

def extract_disk_usage_percent(line: str) -> int | None:
    match = re.search(r"\s(\d{1,3})%\s", line)

    if not match:
        return None

    return int(match.group(1))


# ============================================================
# 8. Classify one possible event line
# ============================================================
# Intention:
#   Read one non-noise line and decide whether it matches one defensive event type.
#
# Return:
#   - A dictionary with event type, severity and analyst note if useful.
#   - None if the line is not useful for this mission.
#
# Important:
#   The script gives an initial classification only.
#   It does not decide whether there is a real attack.

def classify_event(line: str) -> dict | None:
    lower_line = line.lower()

    # 8.1 SSH authentication activity
    # Why first?
    #   SSH lines can also contain words like "failed" or "authentication".
    #   We classify SSH first so it is not swallowed by a generic auth rule.
    if (
        "sshd[" in lower_line
        or "sshd:" in lower_line
        or "failed password" in lower_line
        or "accepted password" in lower_line
        or "invalid user" in lower_line
    ):
        return {
            "event_type": "SSH authentication activity",
            "severity": "Medium",
            "analyst_note": (
                "SSH-related authentication event observed. Review source IP, username, "
                "result and whether SSH exposure is expected."
            ),
        }

    # 8.2 Failed local login or generic authentication failure
    # Purpose:
    #   Detect local login failures and non-sudo authentication failures.
    if "failed login" in lower_line or (
        "authentication failure" in lower_line and "sudo:" not in lower_line
    ):
        return {
            "event_type": "Authentication failure",
            "severity": "Low",
            "analyst_note": (
                "Authentication failure observed. In this lab context it is likely manual/local, "
                "but repetition, remote origin or affected accounts should be reviewed."
            ),
        }

    # 8.3 Sudo authentication failure
    # Purpose:
    #   Detect failed privilege elevation attempts with sudo.
    if "sudo:" in lower_line and "authentication failure" in lower_line:
        return {
            "event_type": "Sudo authentication failure",
            "severity": "Low",
            "analyst_note": (
                "Failed sudo authentication observed. Usually indicates incorrect password "
                "or failed privilege elevation attempt. Review repetition and user context."
            ),
        }

    # 8.4 Multiple incorrect sudo password attempts
    # Purpose:
    #   Detect lines reporting several incorrect password attempts.
    if "incorrect password attempts" in lower_line:
        return {
            "event_type": "Sudo incorrect password attempts",
            "severity": "Low-Medium",
            "analyst_note": (
                "Multiple incorrect sudo password attempts observed. In production this should "
                "be correlated with user, command, time and repetition."
            ),
        }

    # 8.5 Sudo command execution
    # Purpose:
    #   Extract administrative actions for audit review.
    if "sudo:" in lower_line and "command=" in lower_line:
        return {
            "event_type": "Sudo command execution",
            "severity": "Informational",
            "analyst_note": (
                "Administrative command executed with sudo. This is useful for audit trail "
                "and should be reviewed if command, user or timing is unexpected."
            ),
        }

    # 8.6 Scheduled root cron sessions
    # Purpose:
    #   Cron sessions for root are often normal scheduled system activity.
    #   They are useful as baseline events.
    if "cron[" in lower_line and "session opened for user root" in lower_line:
        return {
            "event_type": "Scheduled root cron session",
            "severity": "Informational",
            "analyst_note": (
                "Scheduled root cron session observed. Usually expected system activity; "
                "review only if frequency, timing or related command is unusual."
            ),
        }

    # 8.7 Failed service
    # Purpose:
    #   Detect service start failures and failed systemd units.
    if (
        "failed to start" in lower_line
        or "failed with result" in lower_line
        or "loaded failed failed" in lower_line
        or "service failed" in lower_line
    ):
        return {
            "event_type": "Failed service",
            "severity": "Low",
            "analyst_note": (
                "Failed service observed. Classify by service criticality. In this lab, "
                "fwupd-refresh is interpreted as a technical maintenance/update issue."
            ),
        }

    # 8.8 DNS or network issue
    # Purpose:
    #   Detect DNS degradation, name resolution failures and update connectivity errors.
    if (
        "systemd-resolved" in lower_line
        or "temporary failure in name resolution" in lower_line
        or "name resolution" in lower_line
        or "api.snapcraft.io" in lower_line
        or "snapcraft" in lower_line
        or "degraded feature set" in lower_line
    ):
        return {
            "event_type": "DNS or network issue",
            "severity": "Low-Medium",
            "analyst_note": (
                "Network or DNS-related issue observed. Review DNS, gateway, NAT and whether "
                "the error coincides with lab network changes."
            ),
        }

    # 8.9 VirtualBox shared-folder failure
    # Purpose:
    #   Detect the shared-folder issue we had during the lab.
    if "vboxsf" in lower_line and (
        "share not found" in lower_line
        or "failed for 'capturas'" in lower_line
    ):
        return {
            "event_type": "VirtualBox shared-folder failure",
            "severity": "Low",
            "analyst_note": (
                "VirtualBox shared-folder mount failure observed. This is a resolved lab "
                "infrastructure issue, not a security incident by itself."
            ),
        }

    # 8.10 VirtualBox shared-folder success
    # Purpose:
    #   Detect the line proving that the export path started working.
    if "successfully mounted" in lower_line and "capturas" in lower_line:
        return {
            "event_type": "VirtualBox shared-folder success",
            "severity": "Informational",
            "analyst_note": (
                "Shared-folder mount succeeded. This validates the evidence export path."
            ),
        }

    # 8.11 Kernel or virtualization warning
    # Purpose:
    #   Detect common VM/kernel warnings that should be documented but not over-escalated.
    if (
        "retbleed" in lower_line
        or "vboxguest" in lower_line
        or "vmwgfx" in lower_line
        or "out-of-tree module" in lower_line
        or "apic calibration" in lower_line
        or "timesync" in lower_line
        or "guest additions" in lower_line
    ):
        return {
            "event_type": "Kernel or virtualization warning",
            "severity": "Low",
            "analyst_note": (
                "Kernel or virtualization-related warning observed. Common in lab VMs; "
                "escalate only if combined with instability or suspicious activity."
            ),
        }

    # 8.12 Storage capacity warning
    # Purpose:
    #   Detect high usage on the shared folder used to export evidence.
    if "capturas" in lower_line and "/mnt/capturas" in lower_line and "%" in lower_line:
        usage_percent = extract_disk_usage_percent(line)

        if usage_percent is not None and usage_percent >= 85:
            return {
                "event_type": "Storage capacity warning",
                "severity": "Medium",
                "analyst_note": (
                    "Shared folder storage usage is high. Monitor free space to avoid "
                    "future evidence collection or export failures."
                ),
            }

    return None


# ============================================================
# 9. Extract classified events from one file
# ============================================================
# Intention:
#   Process one evidence file line by line.
#
# Flow:
#   1. Ignore missing files.
#   2. Read all lines safely.
#   3. Skip noise lines.
#   4. Classify useful lines.
#   5. Limit repeated event types.
#   6. Store each extracted event in a list.

def extract_events_from_file(file_path: Path) -> list[dict]:
    events = []

    if not file_path.exists():
        return events

    lines = read_lines_safely(file_path)
    event_type_counter = {}

    for line_number, line in enumerate(lines, start=1):
        # First filter: skip headings, tables, helper commands and empty lines.
        if is_noise_line(line):
            continue

        # Second filter: see whether this line matches a defensive event type.
        classification = classify_event(line)

        if classification is None:
            continue

        event_type = classification["event_type"]
        current_count = event_type_counter.get(event_type, 0)

        # Avoid flooding the report with too many examples of the same event type.
        if current_count >= MAX_EVENTS_PER_TYPE:
            continue

        event_type_counter[event_type] = current_count + 1

        events.append({
            "event_type": event_type,
            "source_file": file_path.name,
            "line_number": line_number,
            "severity": classification["severity"],
            "event": clean_for_markdown(line),
            "analyst_note": classification["analyst_note"],
        })

    return events


# ============================================================
# 10. Build summary counts
# ============================================================
# Intention:
#   Create a small summary by event type.
#
# Example:
#   Failed service -> 10 events -> Low
#   DNS/network issue -> 8 events -> Low-Medium

def build_summary(events: list[dict]) -> dict:
    summary = {}

    for event in events:
        event_type = event["event_type"]
        severity = event["severity"]

        if event_type not in summary:
            summary[event_type] = {
                "total": 0,
                "severity": severity,
            }

        summary[event_type]["total"] += 1

    return summary


# ============================================================
# 11. Build Markdown report
# ============================================================
# Intention:
#   Convert extracted events into a GitHub-readable Markdown report.
#
# Sections:
#   - Objective
#   - Source files
#   - Extraction summary
#   - Extracted events table
#   - SOC interpretation
#   - Limitations
#   - Mission status

def build_markdown_report(events: list[dict], missing_files: list[str]) -> str:
    summary = build_summary(events)
    report_lines = []

    report_lines.append("# Lab 06.3 — Defensive pattern extraction")
    report_lines.append("")
    report_lines.append(f"Date: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC")
    report_lines.append("")
    report_lines.append("## Objective")
    report_lines.append("")
    report_lines.append(
        "Extract and classify relevant defensive events from Lab 05 evidence files "
        "while reducing simple keyword-search noise such as headings, Markdown tables "
        "and grep helper commands."
    )
    report_lines.append("")

    report_lines.append("## Source files")
    report_lines.append("")

    for file_name in SOURCE_FILES:
        status = "missing" if file_name in missing_files else "found"
        report_lines.append(f"- {file_name}: {status}")

    report_lines.append("")
    report_lines.append("## Extraction summary")
    report_lines.append("")

    if not summary:
        report_lines.append("No classified events were extracted.")
        report_lines.append("")
    else:
        report_lines.append("| Event type | Extracted events | Severity |")
        report_lines.append("|---|---:|---|")

        for event_type, data in summary.items():
            report_lines.append(
                f"| {event_type} | {data['total']} | {data['severity']} |"
            )

        report_lines.append("")

    report_lines.append("## Extracted events")
    report_lines.append("")

    if not events:
        report_lines.append("No events extracted.")
        report_lines.append("")
    else:
        report_lines.append(
            "| ID | Event type | Source file | Line | Severity | Extracted event | Analyst note |"
        )
        report_lines.append("|---:|---|---|---:|---|---|---|")

        for index, event in enumerate(events, start=1):
            report_lines.append(
                f"| {index} | {event['event_type']} | {event['source_file']} | "
                f"{event['line_number']} | {event['severity']} | "
                f"`{event['event']}` | {event['analyst_note']} |"
            )

        report_lines.append("")

    report_lines.append("## SOC interpretation")
    report_lines.append("")
    report_lines.append(
        "This script improves on basic keyword counting by filtering common report noise "
        "and extracting events that more closely resemble operational log findings."
    )
    report_lines.append("")
    report_lines.append(
        "The output is still an analyst-support artifact, not an autonomous detection engine. "
        "Each extracted event must be interpreted with context, including source, user, "
        "frequency, time window, origin and operational impact."
    )
    report_lines.append("")
    report_lines.append("## Limitations")
    report_lines.append("")
    report_lines.append(
        "Rules are simple and static. The script does not perform correlation, enrichment, "
        "timeline reconstruction, IP reputation checks, SIEM ingestion or incident response."
    )
    report_lines.append("")
    report_lines.append("## Mission status")
    report_lines.append("")
    report_lines.append("Mission 6.3 completed pending review.")
    report_lines.append("")

    return "\n".join(report_lines)


# ============================================================
# 12. Main execution flow
# ============================================================
# Intention:
#   This is the controlled execution path of the script.
#
# Flow:
#   1. Ensure Lab 06 evidence folder exists.
#   2. Iterate through selected source files.
#   3. Track missing files.
#   4. Extract events from found files.
#   5. Build report.
#   6. Write report to disk.
#   7. Print a short execution summary.

def main() -> None:
    LAB06_EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

    all_events = []
    missing_files = []

    for file_name in SOURCE_FILES:
        file_path = LAB05_EVIDENCE_DIR / file_name

        if not file_path.exists():
            missing_files.append(file_name)
            continue

        file_events = extract_events_from_file(file_path)
        all_events.extend(file_events)

    report = build_markdown_report(all_events, missing_files)
    OUTPUT_REPORT.write_text(report, encoding="utf-8")

    print(f"Report created: {OUTPUT_REPORT}")
    print(f"Extracted events: {len(all_events)}")


# ============================================================
# 13. Script entry point
# ============================================================
# Intention:
#   Only run main() when this file is executed directly.
#   If the file is imported from another script in the future,
#   main() will not run automatically.

if __name__ == "__main__":
    main()
