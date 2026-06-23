#!/usr/bin/env python3

"""
Lab 06.6 — Final professional closure

Defensive scope:
- Read Lab 06 artifacts already created in previous missions.
- Verify that scripts, evidence and reports exist.
- Generate a final closure summary suitable for a GitHub portfolio.
- Do not modify original evidence, do not use sudo, do not connect to the network.
"""

from pathlib import Path
from datetime import datetime, timezone


# ============================================================
# 1. Define lab paths
# ============================================================
# Idea:
# The closure script needs to know where Lab 06 lives and where
# evidence, scripts and reports were stored during the previous missions.
# We use Path.home() so the script works for the current Ubuntu user.

LAB06_DIR = Path.home() / "lab06"
SCRIPTS_DIR = LAB06_DIR / "scripts"
EVIDENCE_DIR = LAB06_DIR / "evidencias"
REPORTS_DIR = LAB06_DIR / "reportes"
MASTER_REPORT = LAB06_DIR / "Lab_06_Python_Defensivo_Log_Review.md"

OUTPUT_REPORT = REPORTS_DIR / "lab06_06_final_closure_summary.md"


# ============================================================
# 2. Define the expected Lab 06 artifacts
# ============================================================
# Idea:
# A professional lab is not only "a script that ran". It must have
# scripts, evidence, generated reports and a main narrative report.
# This checklist lets us verify whether the lab is complete enough
# for GitHub/portfolio publication.

EXPECTED_ARTIFACTS = [
    {
        "mission": "6.1",
        "type": "Evidence",
        "path": EVIDENCE_DIR / "lab06_01_environment_check.txt",
        "description": "Python environment and Lab 05 evidence availability check",
    },
    {
        "mission": "6.2",
        "type": "Script",
        "path": SCRIPTS_DIR / "lab06_mission_6_2_evidence_reader.py",
        "description": "Defensive evidence reader",
    },
    {
        "mission": "6.2",
        "type": "Evidence",
        "path": EVIDENCE_DIR / "lab06_02_evidence_reader_report.md",
        "description": "Evidence inventory and keyword summary report",
    },
    {
        "mission": "6.3",
        "type": "Script",
        "path": SCRIPTS_DIR / "lab06_mission_6_3_pattern_extractor.py",
        "description": "Defensive event pattern extractor",
    },
    {
        "mission": "6.3",
        "type": "Evidence",
        "path": EVIDENCE_DIR / "lab06_03_defensive_pattern_extraction.md",
        "description": "Extracted and classified defensive events",
    },
    {
        "mission": "6.4",
        "type": "Script",
        "path": SCRIPTS_DIR / "lab06_mission_6_4_soc_executive_report.py",
        "description": "SOC executive report generator",
    },
    {
        "mission": "6.4",
        "type": "Report",
        "path": REPORTS_DIR / "lab06_04_soc_executive_report.md",
        "description": "Executive SOC-style summary report",
    },
    {
        "mission": "6.5",
        "type": "Script",
        "path": SCRIPTS_DIR / "lab06_mission_6_5_soc_action_classifier.py",
        "description": "Basic SOC action classifier",
    },
    {
        "mission": "6.5",
        "type": "Report",
        "path": REPORTS_DIR / "lab06_05_soc_action_classifier.md",
        "description": "SOC action and priority classification report",
    },
    {
        "mission": "6.6",
        "type": "Main report",
        "path": MASTER_REPORT,
        "description": "Main Lab 06 narrative report",
    },
]


# ============================================================
# 3. Utility: convert bytes into a readable size
# ============================================================
# Idea:
# GitHub readers and recruiters do not need raw byte counts.
# A small human-readable size makes the closure report easier to scan.

def human_size(size_bytes: int) -> str:
    if size_bytes < 1024:
        return f"{size_bytes} B"

    size_kb = size_bytes / 1024
    if size_kb < 1024:
        return f"{size_kb:.1f} KB"

    size_mb = size_kb / 1024
    return f"{size_mb:.1f} MB"


# ============================================================
# 4. Utility: read text safely
# ============================================================
# Idea:
# We only read files. We use errors="replace" to avoid the script
# failing because of an unexpected character in a log/report.

def read_text_safely(file_path: Path) -> str:
    if not file_path.exists():
        return ""

    return file_path.read_text(encoding="utf-8", errors="replace")


# ============================================================
# 5. Inspect one expected artifact
# ============================================================
# Idea:
# For each required artifact, we record whether it exists, its size,
# and whether a mission-status marker appears inside the file.
# This gives us a controlled closure view of the lab.

def inspect_artifact(artifact: dict) -> dict:
    file_path = artifact["path"]
    exists = file_path.exists()
    size = "N/A"
    status_hint = "N/A"

    if exists:
        size = human_size(file_path.stat().st_size)
        content = read_text_safely(file_path)

        if "validated" in content.lower():
            status_hint = "validated marker found"
        elif "completed pending review" in content.lower():
            status_hint = "pending review marker found"
        else:
            status_hint = "no explicit status marker"

    return {
        "mission": artifact["mission"],
        "type": artifact["type"],
        "path": file_path,
        "file_name": file_path.name,
        "description": artifact["description"],
        "exists": exists,
        "size": size,
        "status_hint": status_hint,
    }


# ============================================================
# 6. Build professional capability summary
# ============================================================
# Idea:
# This section turns the lab into recruiter/interview language.
# It states what the lab demonstrates without exaggerating or claiming
# production SOC experience.

def build_capability_summary() -> list[str]:
    return [
        "Defensive Python scripting for Linux log and evidence review.",
        "Safe file handling using standard Python libraries.",
        "Evidence inventory generation and keyword-based defensive review.",
        "Noise reduction and extraction of classified security/operational events.",
        "SOC-style executive reporting from technical event data.",
        "Basic SOC action mapping: Review, Monitor, Document, No escalation and Needs analyst attention.",
        "Conservative analyst interpretation with documented limitations.",
    ]


# ============================================================
# 7. Build GitHub publication checklist
# ============================================================
# Idea:
# Before pushing the lab to GitHub, we need a clean folder structure.
# This checklist helps avoid uploading random temporary files or unclear evidence.

def build_github_checklist() -> list[str]:
    return [
        "Create a dedicated GitHub folder for Lab 06.",
        "Include README.md with objective, scope, tools, workflow, findings and limitations.",
        "Include scripts with pseudocomments and defensive scope.",
        "Include selected evidence and generated reports.",
        "Avoid uploading secrets, real credentials, private data or unrelated screenshots.",
        "State clearly that the lab is controlled, defensive and authorized.",
        "Mention that scripts support analyst review and do not produce autonomous incident verdicts.",
    ]


# ============================================================
# 8. Build the final Markdown closure report
# ============================================================
# Idea:
# This report is the final evidence of Lab 06 completion.
# It summarises artifacts, capabilities, limitations and GitHub readiness.

def build_markdown_report(artifact_results: list[dict]) -> str:
    found_count = sum(1 for item in artifact_results if item["exists"])
    missing_count = len(artifact_results) - found_count

    report_lines = []

    report_lines.append("# Lab 06.6 — Final closure summary")
    report_lines.append("")
    report_lines.append(f"Date: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC")
    report_lines.append("")

    report_lines.append("## Executive summary")
    report_lines.append("")
    report_lines.append(
        "Lab 06 developed a defensive Python workflow for Linux evidence review, "
        "event extraction, SOC-style reporting and initial action classification. "
        "The lab demonstrates how Python can support a SOC Level 1 workflow while "
        "preserving conservative analyst interpretation."
    )
    report_lines.append("")
    report_lines.append(
        "The scripts do not modify original evidence, do not require sudo, do not scan "
        "networks and do not make autonomous incident decisions. They transform controlled "
        "lab evidence into structured reports for analyst review."
    )
    report_lines.append("")

    report_lines.append("## Completion status")
    report_lines.append("")
    report_lines.append(f"- Expected artifacts: {len(artifact_results)}")
    report_lines.append(f"- Found artifacts: {found_count}")
    report_lines.append(f"- Missing artifacts: {missing_count}")
    report_lines.append("")

    if missing_count == 0:
        report_lines.append("Overall status: Lab 06 appears complete and ready for final review.")
    else:
        report_lines.append("Overall status: Lab 06 requires artifact review before publication.")

    report_lines.append("")

    report_lines.append("## Artifact checklist")
    report_lines.append("")
    report_lines.append("| Mission | Type | File | Exists | Size | Status hint | Description |")
    report_lines.append("|---|---|---|---|---:|---|---|")

    for item in artifact_results:
        exists_text = "yes" if item["exists"] else "no"
        report_lines.append(
            f"| {item['mission']} | {item['type']} | `{item['file_name']}` | "
            f"{exists_text} | {item['size']} | {item['status_hint']} | {item['description']} |"
        )

    report_lines.append("")

    report_lines.append("## Demonstrated capabilities")
    report_lines.append("")

    for capability in build_capability_summary():
        report_lines.append(f"- {capability}")

    report_lines.append("")

    report_lines.append("## GitHub publication checklist")
    report_lines.append("")

    for item in build_github_checklist():
        report_lines.append(f"- {item}")

    report_lines.append("")

    report_lines.append("## Professional portfolio statement")
    report_lines.append("")
    report_lines.append(
        "Defensive Python lab for Linux log review and SOC triage: evidence reading, "
        "keyword review, pattern extraction, executive reporting and action classification "
        "using conservative analyst-support logic."
    )
    report_lines.append("")

    report_lines.append("## Limitations")
    report_lines.append("")
    report_lines.append("- Controlled lab environment, not production telemetry.")
    report_lines.append("- Static rules only; no SIEM correlation or behavioural baseline.")
    report_lines.append("- No threat intelligence enrichment, IP reputation or asset inventory.")
    report_lines.append("- No automatic incident verdict or response action.")
    report_lines.append("- Some residual noise may appear and should be documented as parser limitation.")
    report_lines.append("")

    report_lines.append("## Recommended next steps")
    report_lines.append("")
    report_lines.append("- Create the GitHub Lab 06 folder with scripts, evidence and reports.")
    report_lines.append("- Write a concise README explaining workflow and findings.")
    report_lines.append("- Update portfolio README with Lab 06 capability line.")
    report_lines.append("- Use Lab 06 in interviews as an example of SOC L1 reasoning with Python.")
    report_lines.append("")

    report_lines.append("## Mission status")
    report_lines.append("")
    report_lines.append("Mission 6.6 completed pending review.")
    report_lines.append("")

    return "\n".join(report_lines)


# ============================================================
# 9. Main execution flow
# ============================================================
# Idea:
# The main function keeps the script readable:
# create output folder, inspect artifacts, build report, write report,
# print a short execution summary.

def main() -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    artifact_results = []

    for artifact in EXPECTED_ARTIFACTS:
        artifact_results.append(inspect_artifact(artifact))

    report = build_markdown_report(artifact_results)
    OUTPUT_REPORT.write_text(report, encoding="utf-8")

    found_count = sum(1 for item in artifact_results if item["exists"])
    missing_count = len(artifact_results) - found_count

    print(f"Report created: {OUTPUT_REPORT}")
    print(f"Artifacts found: {found_count}")
    print(f"Artifacts missing: {missing_count}")


# ============================================================
# 10. Script entry point
# ============================================================
# Idea:
# This prevents the script from running automatically if it is imported
# from another Python file in the future.

if __name__ == "__main__":
    main()
