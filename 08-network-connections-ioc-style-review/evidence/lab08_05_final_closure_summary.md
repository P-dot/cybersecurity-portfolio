# Lab 08.5 — Final Closure Summary: Network Connections & IOC-style Review

## Lab status

**Lab:** Lab 08 — Network Connections & IOC-style Review  
**Status:** Completed  
**Focus:** Defensive review of local network connections, listening ports, process context and IOC-style triage  
**Evidence handling:** Sanitized evidence only  
**Execution mode:** Read-only PowerShell evidence collection

---

## 1. Objective

The objective of this lab was to review local Windows network activity from a SOC L1 perspective and produce sanitized evidence suitable for a public cybersecurity portfolio.

The lab focused on:

- Network adapter and IP configuration visibility.
- TCP/UDP connection inventory.
- Listening port exposure.
- Process-to-network context.
- Basic IOC-style triage reasoning.
- Conservative SOC interpretation.
- Privacy-conscious evidence handling.

---

## 2. Evidence created

| Evidence file | Purpose | Status |
|---|---|---|
| `lab08_01_network_connections_inventory_sanitized.txt` | Sanitized inventory of adapters, TCP/UDP entries, ports and processes | Completed |
| `lab08_02_listening_ports_exposure_review_sanitized.txt` | Sanitized listening-port exposure review and analyst action classification | Completed |
| `lab08_03_active_connections_process_context_sanitized.txt` | Sanitized active TCP connection and process-context review | Completed |
| `lab08_04_ioc_style_mini_triage_summary.md` | Consolidated IOC-style mini triage summary | Completed |
| `lab08_05_final_closure_summary.md` | Final lab closure and portfolio summary | Completed |

---

## 3. Environment and scope

The reviewed host was a Windows lab host used for defensive cybersecurity portfolio work.

The evidence was generated using read-only PowerShell commands and did not modify:

- firewall rules,
- services,
- routes,
- DNS settings,
- users,
- permissions,
- files outside the evidence folder,
- system configuration.

No offensive activity was performed. No third-party systems were scanned or interacted with.

---

## 4. Key findings

### Network visibility

The host provided sufficient local network visibility for basic SOC-style review:

- network adapters,
- IPv4/IPv6 configuration counts,
- TCP connection states,
- UDP endpoint counts,
- local ports,
- listening entries,
- process names associated with TCP/UDP activity.

Sensitive values such as raw IP addresses, DNS names, process paths, command lines and usernames were intentionally excluded.

### Listening exposure

The listening-port review identified Windows service exposure and application/service context requiring analyst review:

- RPC / Windows service exposure,
- NetBIOS / SMB exposure,
- TeamViewer context,
- Syncthing synchronization and local web interface context,
- Windows service discovery,
- dynamic high Windows ports.

The active network category was identified as **Public**, which is relevant defensive context.

### Active connections

The active connection review identified a small number of active TCP entries, mainly associated with:

- Syncthing,
- Windows system components,
- user/web-facing components,
- HTTPS traffic,
- one CloseWait state requiring review if recurring.

No unknown process context was identified in the sanitized active connection review.

---

## 5. SOC classification

| Field | Assessment |
|---|---|
| Classification | Network visibility and exposure review |
| Priority | P3 — Review and monitor |
| Confirmed incident | No |
| Evidence of compromise | Not indicated in exported evidence |
| Escalation required | No immediate escalation |
| Recommended action | Document exposure, verify expected tools, monitor recurring patterns |

---

## 6. Skills demonstrated

This lab demonstrates:

- Windows network connection review.
- PowerShell-based defensive evidence collection.
- TCP/UDP visibility analysis.
- Listening-port exposure review.
- Process-to-network context interpretation.
- Basic IOC-style reasoning.
- SOC-style action classification: Monitor / Review / Document.
- Privacy-conscious evidence handling.
- Markdown reporting for GitHub.
- Conservative analyst decision-making.

---

## 7. Limitations

This lab intentionally avoids exporting sensitive data and does not represent a full enterprise investigation.

Limitations:

- No raw IP addresses exported.
- No DNS names exported.
- No process paths exported.
- No command lines exported.
- No packet capture in this lab phase.
- No SIEM correlation.
- No EDR telemetry.
- No threat intelligence enrichment.
- No reputation lookup.
- No long-term historical baseline.
- No enterprise/domain environment context.

These limitations are acceptable for a defensive portfolio lab and are documented explicitly.

---

## 8. Portfolio summary

**Professional summary for CV/GitHub:**

Network connections and IOC-style defensive review lab focused on SOC L1-style triage. Reviewed TCP/UDP activity, listening ports, process-to-network context and exposure indicators using sanitized PowerShell evidence, with conservative classification of findings into Monitor, Review and Document actions.

---

## 9. Final conclusion

Lab 08 is complete.

The lab adds a network-visibility and exposure-review component to the portfolio and complements previous Linux log monitoring, defensive Python reporting and Windows Event Log review work.

The correct analyst decision is to **document, verify expected services and monitor**, not to escalate as a confirmed incident.

**Final status:** Completed and ready for GitHub packaging.
