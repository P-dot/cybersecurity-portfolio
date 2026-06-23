# Lab 06 — Defensive Python for Linux Log Review and SOC Reporting

## Objective

This lab demonstrates a defensive Python workflow for Linux evidence review, basic SOC triage support and analyst-oriented reporting.

The goal is not to create an autonomous detection engine. The goal is to show how Python can help a SOC Level 1 analyst read collected evidence, reduce simple noise, extract relevant events, generate an executive summary and assign initial analyst actions.

## Scope

This lab uses evidence generated in a controlled and authorized Linux monitoring lab. The scripts work with local text files and Markdown reports only.

The workflow covers:

- Python environment validation.
- Lab evidence inventory.
- Defensive keyword review.
- Pattern extraction from Linux log evidence.
- SOC-style executive reporting.
- Basic action classification for analyst triage.
- Final artifact review for GitHub publication.

## Repository structure

```text
06-defensive-python-log-review-soc-reporting/
├── README.md
├── evidence/
│   ├── lab06_01_environment_check.txt
│   ├── lab06_02_evidence_reader_report.md
│   └── lab06_03_defensive_pattern_extraction.md
├── reports/
│   ├── Lab_06_Python_Defensivo_Log_Review.md
│   ├── lab06_04_soc_executive_report.md
│   ├── lab06_05_soc_action_classifier.md
│   └── lab06_06_final_closure_summary.md
└── scripts/
    ├── lab06_mission_6_2_evidence_reader.py
    ├── lab06_mission_6_3_pattern_extractor.py
    ├── lab06_mission_6_4_soc_executive_report.py
    ├── lab06_mission_6_5_soc_action_classifier.py
    └── lab06_mission_6_6_final_closure.py
```

## Workflow

### Mission 6.1 — Environment check

Validated the Python environment, Lab 06 directory structure and availability of Lab 05 evidence files.

### Mission 6.2 — Defensive evidence reader

Created a Python script that reads selected Lab 05 evidence files and generates a Markdown inventory with:

- File existence.
- File size.
- Line counts.
- Keyword-group matches.
- Sample matching lines.

This first stage performs broad evidence review and prepares material for analyst inspection.

### Mission 6.3 — Defensive pattern extraction

Created a Python extractor that reduces simple report noise and classifies relevant technical events from Linux evidence.

Extracted event types include:

- Authentication failures.
- Sudo authentication failures.
- Sudo command execution.
- Failed services.
- DNS or network issues.
- VirtualBox shared-folder failures and successes.
- Kernel or virtualization warnings.
- Storage capacity warnings.

The script generated a technical event table with source file, line number, severity and analyst note.

### Mission 6.4 — SOC executive report

Created a Python reporting script that converts the technical event table into an executive SOC-style summary.

The report separates findings into:

- Security-relevant events.
- Privileged activity and audit trail.
- Operational or technical issues.
- Lab infrastructure events.
- Noise or low-value findings.

The report includes key findings, representative samples, recommended analyst actions, limitations and conservative SOC interpretation.

### Mission 6.5 — Basic SOC action classifier

Created a Python classifier that maps extracted events to initial SOC analyst actions:

- Needs analyst attention.
- Review.
- Monitor.
- Document.
- No escalation.

The classifier also assigns educational priorities such as P2, P3 and P4. It does not create tickets or declare incidents.

### Mission 6.6 — Final closure

Generated a final closure report confirming that all expected artifacts were present and ready for GitHub review.

## Key results

- Python environment validated.
- 70 technical events were processed from the extracted evidence.
- Events were summarised into SOC-style executive categories.
- Initial analyst actions were assigned conservatively.
- No high or critical severity finding was identified by the static rules used in this lab.
- No clear evidence of compromise was concluded by the scripts.

## Tools and technologies

- Python 3.
- pathlib.
- datetime.
- re.
- Linux log evidence.
- Markdown reporting.
- Git/GitHub.

## Defensive value

This lab demonstrates the ability to move from raw evidence to structured analyst support:

```text
Linux evidence → Python parsing → event extraction → executive SOC report → action classification
```

This is relevant for SOC Level 1 and security operations roles because it shows:

- Evidence handling.
- Log review mindset.
- Conservative interpretation.
- Basic automation.
- Report writing.
- Initial triage logic.
- Awareness of false positives and lab-context noise.

## Security and ethics

This lab is defensive and controlled.

The scripts:

- Do not modify original evidence.
- Do not require sudo.
- Do not scan networks.
- Do not exploit systems.
- Do not collect credentials.
- Do not perform incident response actions.
- Do not make autonomous incident decisions.

All outputs are intended to support analyst review in a controlled lab environment.

## Limitations

- Static rules only.
- No SIEM ingestion.
- No timeline reconstruction.
- No behavioural baseline.
- No threat intelligence enrichment.
- No IP reputation checks.
- No asset criticality model.
- Some residual noise may appear and should be treated as parser limitation.

## Professional portfolio statement

Defensive Python lab for Linux log review and SOC triage: evidence reading, keyword review, defensive pattern extraction, executive SOC-style reporting and action classification using conservative analyst-support logic.
