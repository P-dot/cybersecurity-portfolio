# Lab 07.4 — Mini SOC Triage Summary: Windows Event Log Defensive Review

## 1. Objective

This report consolidates the sanitized evidence collected during Lab 07:

- **Lab 07.1:** Windows Event Log inventory.
- **Lab 07.2:** Windows authentication review.
- **Lab 07.3:** Windows System/Application health review.

The goal is to produce a short SOC-style triage summary suitable for a defensive cybersecurity portfolio.

---

## 2. Scope and privacy controls

**Environment:** Windows lab host used for defensive portfolio work.  
**Operating system:** Microsoft Windows 10 Pro, 64-bit, build 19045.  
**Time window:** last 7 days from each evidence collection point.  
**Data handling:** sanitized evidence only.

The exported evidence intentionally excludes:

- usernames,
- IP addresses,
- workstation names,
- domains,
- raw event messages,
- personal paths,
- command lines.

This lab is defensive and read-only. It does not modify logs, users, services, firewall rules, registry settings or system configuration.

---

## 3. Available Windows log sources

The following Windows Event Log sources were available and readable:

| Log source | Status | Observed volume |
|---|---:|---:|
| Security | Readable | 27,518 total records; 1,000 sampled in last 7 days |
| System | Readable | 37,133 total records; 746 sampled in last 7 days |
| Application | Readable | 40,890 total records; 927 sampled in last 7 days |
| Windows PowerShell | Readable | 5,387 total records; 208 sampled in last 7 days |
| Microsoft-Windows-PowerShell/Operational | Readable | 1,742 total records; 666 sampled in last 7 days |

**SOC relevance:** the host has sufficient Windows event visibility for basic L1 triage across authentication, system health, application health and PowerShell-related sources.

---

## 4. Authentication findings

The Windows Security log was reviewed using sanitized, count-based indicators.

| Event ID | Meaning | Count / status |
|---:|---|---:|
| 4624 | Successful logon | 714 |
| 4625 | Failed logon | Not available or no readable events |
| 4634 | Logoff | 64 |
| 4648 | Explicit credentials used | 62 |
| 4672 | Special privileges assigned | 687 |

### Authentication interpretation

- Authentication visibility is available through the Windows Security log.
- Successful logons and privileged logons are present in the selected window.
- Explicit credential use is present and should be interpreted in context.
- No failed logon evidence was available in the sanitized sample.
- Counts alone are not proof of compromise.

### Authentication triage decision

**Priority:** P3 — Monitor / contextual review.  
**Reasoning:** privileged logon and explicit credential events can be normal on a Windows host, especially during administration or system activity. There is no exported evidence of failed logon bursts, lockouts or account changes in this sanitized dataset.

---

## 5. System and Application health findings

### Event volume by severity

| Log | Critical | Error | Warning |
|---|---:|---:|---:|
| System | 0 | 113 | 84 |
| Application | 0 | 0 | 0 |

### Top System error providers

| Provider | Count |
|---|---:|
| Service Control Manager | 90 |
| Microsoft-Windows-DistributedCOM | 12 |
| BTHUSB | 11 |

### Top System warning providers

| Provider | Count |
|---|---:|
| Microsoft-Windows-DistributedCOM | 36 |
| Microsoft-Windows-DNS-Client | 20 |
| Microsoft-Windows-Time-Service | 14 |
| Netwtw06 | 6 |
| Microsoft-Windows-WLAN-AutoConfig | 5 |
| Tcpip | 2 |
| Microsoft-Windows-Kernel-Processor-Power | 1 |

### Top System Event IDs

| Severity | Event ID | Count |
|---|---:|---:|
| Error | 7016 | 77 |
| Error | 17 | 11 |
| Error | 10005 | 11 |
| Error | 7000 | 11 |
| Error | 7031 | 2 |
| Error | 10010 | 1 |
| Warning | 10016 | 36 |
| Warning | 1014 | 20 |
| Warning | 134 | 14 |
| Warning | 6000 | 6 |
| Warning | 4003 | 3 |
| Warning | 10002 | 2 |
| Warning | 4227 | 2 |
| Warning | 37 | 1 |

### System/Application interpretation

- No critical events were observed in the sampled window.
- Application log did not show sampled critical, error or warning events.
- System log shows operational noise mainly related to:
  - Service Control Manager,
  - DistributedCOM,
  - DNS client,
  - time synchronization,
  - wireless/network stack,
  - Bluetooth USB.
- These findings are operationally relevant but do not prove compromise.

### System/Application triage decision

**Priority:** P3 — Review / document.  
**Reasoning:** System errors and warnings may affect stability, service behavior or network reliability. They should be documented and monitored, but the sanitized evidence does not support escalation as a confirmed security incident.

---

## 6. Consolidated SOC assessment

### Overall classification

**Classification:** Operational security review / Windows log triage.  
**Overall priority:** P3 — Review and monitor.  
**Escalation required:** No immediate escalation based on sanitized evidence.  
**Incident confirmed:** No.  
**Compromise indicated:** No evidence of compromise in the exported data.

### Key positives

- Security, System, Application and PowerShell logs are readable.
- Authentication events can be reviewed.
- System health issues can be summarized without exposing sensitive data.
- Evidence handling is privacy-conscious and suitable for a public portfolio.

### Key limitations

- Evidence is sanitized and count-based.
- Raw messages were not exported.
- No usernames, IP addresses or workstation context were retained.
- No SIEM correlation, endpoint telemetry, process lineage or threat intelligence enrichment was performed.
- The host is a lab/workstation environment, not a corporate domain environment.

---

## 7. Recommended actions

| Area | Recommendation |
|---|---|
| Authentication | Continue monitoring 4624, 4625, 4648 and 4672 in context. |
| Privileged events | Review whether high 4672 volume aligns with expected administrative/system activity. |
| System health | Review recurring Service Control Manager and DistributedCOM events for operational stability. |
| DNS/time/network | Monitor DNS Client, Time-Service, WLAN and TCP/IP warnings for reliability issues. |
| Evidence handling | Keep public evidence sanitized; do not publish raw Windows event messages. |
| Next lab step | Convert this triage into a GitHub-ready Lab 07 README and evidence package. |

---

## 8. Analyst conclusion

The Windows lab host provides sufficient event log visibility for basic SOC L1-style review. The collected evidence shows authentication activity, privileged logon activity and recurring System-level operational issues, but no critical events, no Application-level sampled errors/warnings and no sanitized evidence of compromise.

The correct analyst decision is to **document and monitor**, not to escalate as a confirmed incident.

**Lab 07.4 status:** completed.
