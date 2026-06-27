# Lab 07 — Windows Event Log Defensive Review

## Overview

This lab documents a defensive review of Windows Event Logs from a SOC L1 perspective.  
The goal is to collect and summarize sanitized Windows evidence without exposing personal data or raw event messages.

The lab focuses on:

- Windows Event Log inventory.
- Security log authentication review.
- System/Application health review.
- SOC-style mini triage.
- Privacy-conscious reporting.

---

## Scope

This lab was performed on a Windows lab host used for defensive cybersecurity portfolio work.

The evidence is sanitized and intentionally excludes:

- usernames,
- IP addresses,
- workstation names,
- domains,
- raw event messages,
- personal file paths,
- command lines.

No offensive activity was performed.

---

## Evidence files

| File | Description |
|---|---|
| `evidence/lab07_01_windows_log_inventory_sanitized.txt` | Inventory of readable Windows logs and recent event volume |
| `evidence/lab07_02_windows_authentication_review_sanitized.txt` | Sanitized authentication review from Windows Security log |
| `evidence/lab07_03_windows_system_application_health_sanitized.txt` | Sanitized System/Application health review |
| `evidence/lab07_04_windows_mini_triage_soc.md` | SOC-style mini triage summary |
| `evidence/lab07_05_final_closure_summary.md` | Final lab closure summary |

---

## Key findings

- Security, System, Application and PowerShell event sources were readable.
- Authentication activity was visible through the Windows Security log.
- Successful logons, logoffs, explicit credential usage and special privilege events were reviewed as count-based indicators.
- System log contained operational errors and warnings mainly related to Service Control Manager, DistributedCOM, DNS, time service, wireless/network and Bluetooth components.
- Application log did not show sampled critical, error or warning events in the reviewed window.
- No confirmed incident or evidence of compromise was identified from the exported sanitized evidence.

---

## SOC interpretation

The collected evidence supports a conservative SOC L1 decision:

**Priority:** P3 — Review and monitor  
**Escalation:** No immediate escalation  
**Incident confirmed:** No  
**Recommended action:** Document recurring operational issues and monitor authentication/system-health indicators over time.

---

## Skills demonstrated

- Windows Event Log review.
- PowerShell-based defensive evidence collection.
- Authentication event ID awareness.
- Security/System/Application log triage.
- Count-based event summarization.
- Sanitized reporting.
- Markdown technical documentation.
- Conservative SOC decision-making.

---

## Limitations

This lab does not include:

- SIEM correlation.
- EDR telemetry.
- Raw event messages.
- Threat intelligence enrichment.
- Full timeline reconstruction.
- Domain controller logs.
- Enterprise SOC context.

The lab is designed as a defensive portfolio exercise and should not be interpreted as a full incident response investigation.

---

## Portfolio statement

Windows Event Log defensive review lab focused on SOC L1-style triage: log source visibility, authentication event review, System/Application health indicators, sanitized evidence handling and conservative analyst reporting.
