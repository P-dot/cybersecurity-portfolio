#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime


# =========================
# Lab paths
# =========================

LAB05_EVIDENCE_DIR = Path.home() / "lab05" / "evidencias"
LAB06_DIR = Path.home() / "lab06"
LAB06_EVIDENCE_DIR = LAB06_DIR / "evidencias"

OUTPUT_REPORT = LAB06_EVIDENCE_DIR / "lab06_02_evidence_reader_report.md"


# =========================
# Evidence files to review
# =========================

EVIDENCE_FILES = [
    "lab05_02_auth_sudo_sessions.txt",
    "lab05_03_system_health_errors.txt",
    "lab05_04_mini_triage_soc.md",
    "lab05_05_final_closure_summary.md",
]


# =========================
# Defensive keyword groups
# =========================

KEYWORD_GROUPS = {
    "sudo_activity": [
        "sudo",
    ],
    "authentication_failures": [
        "failed login",
        "authentication failure",
        "incorrect password",
        "failed password",
        "invalid user",
    ],
    "ssh_activity": [
        "ssh",
        "sshd",
    ],
    "service_failures": [
        "failed to start",
        "failed with result",
        "loaded failed failed",
        "service failed",
    ],
    "dns_or_network_issues": [
        "dns",
        "name resolution",
        "temporary failure in name resolution",
        "systemd-resolved",
        "snapcraft",
        "api.snapcraft.io",
    ],
    "virtualbox_or_lab_infrastructure": [
        "virtualbox",
        "vboxsf",
        "vboxguest",
        "capturas",
        "guest additions",
    ],
    "warnings_errors_timeouts": [
        "warning",
        "error",
        "failure",
        "failed",
        "critical",
        "denied",
        "timeout",
    ],
}


MAX_SAMPLES_PER_GROUP = 5


# =========================
# Helper functions
# =========================

def human_size(size_bytes: int) -> str:
    """
    Convert a file size in bytes into a readable value.
    Example: 1024 -> 1.0 KB
    """
    if size_bytes < 1024:
        return f"{size_bytes} B"

    size_kb = size_bytes / 1024

    if size_kb < 1024:
        return f"{size_kb:.1f} KB"

    size_mb = size_kb / 1024
    return f"{size_mb:.1f} MB"


def read_lines_safely(file_path: Path) -> list[str]:
    """
    Read a text file and return its lines.

    errors='replace' prevents the script from crashing
    if the file contains an unusual character.
    """
    content = file_path.read_text(encoding="utf-8", errors="replace")
    return content.splitlines()


def line_matches_any_keyword(line: str, keywords: list[str]) -> bool:
    """
    Check whether a line contains at least one keyword from a group.
    Search is case-insensitive.
    """
    lower_line = line.lower()

    for keyword in keywords:
        if keyword.lower() in lower_line:
            return True

    return False


def analyse_file(file_path: Path) -> dict:
    """
    Analyse one evidence file.

    The function returns a dictionary with:
    - file existence
    - size
    - number of lines
    - keyword match counts
    - sample matching lines
    """
    result = {
        "file_name": file_path.name,
        "path": str(file_path),
        "exists": file_path.exists(),
        "size": "N/A",
        "line_count": 0,
        "keyword_results": {},
    }

    if not file_path.exists():
        return result

    size_bytes = file_path.stat().st_size
    lines = read_lines_safely(file_path)

    result["size"] = human_size(size_bytes)
    result["line_count"] = len(lines)

    for group_name, keywords in KEYWORD_GROUPS.items():
        match_count = 0
        samples = []

        for line_number, line in enumerate(lines, start=1):
            if line_matches_any_keyword(line, keywords):
                match_count += 1

                if len(samples) < MAX_SAMPLES_PER_GROUP:
                    samples.append({
                        "line_number": line_number,
                        "line": line.strip(),
                    })

        result["keyword_results"][group_name] = {
            "count": match_count,
            "samples": samples,
        }

    return result


def build_markdown_report(results: list[dict]) -> str:
    """
    Build the final Markdown report from all analysis results.
    """
    report_lines = []

    report_lines.append("# Lab 06.2 — Defensive evidence reader report")
    report_lines.append("")
    report_lines.append(f"Date: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC")
    report_lines.append("")
    report_lines.append("## Objective")
    report_lines.append("")
    report_lines.append(
        "Read Lab 05 evidence files with Python and generate a defensive summary "
        "including file presence, size, line count, keyword matches and sample lines."
    )
    report_lines.append("")
    report_lines.append("## Evidence inventory")
    report_lines.append("")
    report_lines.append("| File | Exists | Size | Lines |")
    report_lines.append("|---|---|---:|---:|")

    for result in results:
        exists_text = "yes" if result["exists"] else "no"
        report_lines.append(
            f"| {result['file_name']} | {exists_text} | {result['size']} | {result['line_count']} |"
        )

    report_lines.append("")
    report_lines.append("## Keyword summary")
    report_lines.append("")

    for result in results:
        report_lines.append(f"### {result['file_name']}")
        report_lines.append("")

        if not result["exists"]:
            report_lines.append("File not found.")
            report_lines.append("")
            continue

        report_lines.append("| Keyword group | Matching lines |")
        report_lines.append("|---|---:|")

        for group_name, group_result in result["keyword_results"].items():
            report_lines.append(
                f"| {group_name} | {group_result['count']} |"
            )

        report_lines.append("")

    report_lines.append("## Sample matching lines")
    report_lines.append("")

    for result in results:
        report_lines.append(f"### {result['file_name']}")
        report_lines.append("")

        if not result["exists"]:
            report_lines.append("File not found.")
            report_lines.append("")
            continue

        for group_name, group_result in result["keyword_results"].items():
            report_lines.append(f"#### {group_name}")
            report_lines.append("")

            samples = group_result["samples"]

            if not samples:
                report_lines.append("No sample lines found.")
                report_lines.append("")
                continue

            for sample in samples:
                report_lines.append(
                    f"- Line {sample['line_number']}: `{sample['line']}`"
                )

            report_lines.append("")

    report_lines.append("## SOC interpretation")
    report_lines.append("")
    report_lines.append(
        "This script does not determine whether an incident occurred. "
        "It prepares evidence for analyst review by identifying relevant patterns "
        "and summarising where they appear."
    )
    report_lines.append("")
    report_lines.append(
        "Keyword matches must be interpreted with context. For example, a single local "
        "authentication failure may be a manual mistake, while repeated remote failures "
        "could require further investigation."
    )
    report_lines.append("")
    report_lines.append("## Mission status")
    report_lines.append("")
    report_lines.append("Mission 6.2 completed pending review.")
    report_lines.append("")

    return "\n".join(report_lines)


def main() -> None:
    """
    Main execution flow.
    """
    LAB06_EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

    results = []

    for file_name in EVIDENCE_FILES:
        file_path = LAB05_EVIDENCE_DIR / file_name
        analysis_result = analyse_file(file_path)
        results.append(analysis_result)

    report = build_markdown_report(results)

    OUTPUT_REPORT.write_text(report, encoding="utf-8")

    print(f"Report created: {OUTPUT_REPORT}")


if __name__ == "__main__":
    main()
