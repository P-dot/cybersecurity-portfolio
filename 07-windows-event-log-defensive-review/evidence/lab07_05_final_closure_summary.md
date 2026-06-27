# Lab 07.5 — Final Closure Summary: Windows Event Log Defensive Review

## Lab status

**Lab:** Lab 07 — Windows Event Log Defensive Review  
**Status:** Completed  
**Focus:** Defensive review of Windows Event Logs from a SOC L1 perspective  
**Evidence handling:** Sanitized evidence only

---

## 1. Objective

The objective of this lab was to perform a defensive Windows Event Log review and produce sanitized SOC-style evidence suitable for a public cybersecurity portfolio.

The lab focused on:

- Windows Event Log source visibility.
- Authentication-related Security events.
- System and Application health events.
- Count-based triage indicators.
- Conservative SOC interpretation.
- Privacy-conscious evidence handling.

---

## 2. Evidence created

| Evidence file | Purpose | Status |
|---|---|---|
| `lab07_01_windows_log_inventory_sanitized.txt` | Inventory of readable Windows logs and recent event volume | Completed |
| `lab07_02_windows_authentication_review_sanitized.txt` | Sanitized authentication event review | Completed |
| `lab07_03_windows_system_application_health_sanitized.txt` | Sanitized System/Application health review | Completed |
| `lab07_04_windows_mini_triage_soc.md` | Consolidated SOC-style mini triage summary | Completed |
| `lab07_05_final_closure_summary.md` | Final closure and portfolio summary | Completed |

---

## 3. Environment summary

The reviewed host was a Windows lab host used for defensive cybersecurity portfolio work.

Observed environment characteristics:

- Windows 10 Pro.
- 64-bit architecture.
- Build 19045.
- Security, System, Application and PowerShell event sources available for review.
- Evidence was generated using read-only PowerShell commands.

No offensive activity was performed.

---

## 4. Key findings

### Log visibility

The following Windows Event Log sources were readable:

- Security.
- System.
- Application.
- Windows PowerShell.
- Microsoft-Windows-PowerShell/Operational.

This provides a basic but useful Windows visibility baseline for SOC L1-style review.

### Authentication review

The Security log provided count-based visibility for:

- Successful logons.
- Logoffs.
- Explicit credential usage.
- Special privilege assignment events.

No usernames, IP addresses, workstation names, domains or raw messages were exported.

### System/Application health review

The System log showed operational events requiring documentation and monitoring:

- Service Control Manager errors.
- DistributedCOM errors/warnings.
- DNS Client warnings.
- Time-Service warnings.
- Wireless/network-related warnings.
- Bluetooth-related events.

The Application log did not show sampled critical, error or warning events in the reviewed window.

### Mini triage conclusion

No confirmed security incident was identified from the exported sanitized evidence.

The correct analyst decision is:

**Document and monitor. Do not escalate as a confirmed incident based only on this evidence.**

---

## 5. SOC classification

| Field | Assessment |
|---|---|
| Classification | Operational security review / Windows log triage |
| Priority | P3 — Review and monitor |
| Confirmed incident | No |
| Evidence of compromise | Not indicated in exported evidence |
| Escalation required | No immediate escalation |
| Recommended action | Document, monitor, review recurring operational issues |

---

## 6. Skills demonstrated

This lab demonstrates:

- Windows Event Log review.
- PowerShell-based defensive evidence collection.
- Windows Security event ID awareness.
- Authentication triage basics.
- System/Application health review.
- Sanitized reporting.
- Conservative SOC interpretation.
- Portfolio-safe evidence handling.
- Markdown reporting for GitHub.

---

## 7. Limitations

This lab intentionally avoids exporting sensitive or excessive host data.

Limitations:

- No raw Windows event messages exported.
- No usernames, IP addresses, workstation names or command lines exported.
- No SIEM correlation.
- No EDR telemetry.
- No process tree or timeline reconstruction.
- No threat intelligence enrichment.
- No domain controller logs.
- No enterprise environment context.

These limitations are acceptable for a defensive portfolio lab and should be stated clearly in GitHub.

---

## 8. Portfolio summary

**Professional summary for CV/GitHub:**

Windows Event Log defensive review lab focused on SOC L1-style triage. Reviewed Security, System, Application and PowerShell event sources, analyzed authentication-related event IDs, summarized System/Application health indicators and produced sanitized evidence with conservative analyst interpretation.

---

## 9. Final conclusion

Lab 07 is complete.

The lab adds a Windows-focused defensive monitoring component to the portfolio and complements previous Linux log monitoring and defensive Python reporting work.

**Final status:** Completed and ready for GitHub packaging.
