# Lab 08 — Network Connections & IOC-style Review

## Overview

This lab documents a defensive review of local Windows network activity from a SOC L1 perspective.

The goal is to collect and summarize sanitized evidence related to:

- local network visibility,
- TCP/UDP connection inventory,
- listening ports,
- process-to-network context,
- exposure review,
- basic IOC-style triage reasoning.

The lab is defensive, read-only and suitable for a public cybersecurity portfolio.

---

## Scope

This lab was performed on a Windows lab host used for defensive cybersecurity portfolio work.

The evidence is sanitized and intentionally excludes:

- raw IP addresses,
- DNS names,
- usernames,
- process paths,
- command lines,
- personal data.

No offensive activity was performed.  
No third-party systems were scanned or interacted with.

---

## Evidence files

| File | Description |
|---|---|
| `evidence/lab08_01_network_connections_inventory_sanitized.txt` | Sanitized inventory of adapters, TCP/UDP entries, ports and process names |
| `evidence/lab08_02_listening_ports_exposure_review_sanitized.txt` | Sanitized listening-port exposure review with analyst actions |
| `evidence/lab08_03_active_connections_process_context_sanitized.txt` | Sanitized active TCP connection and process-context review |
| `evidence/lab08_04_ioc_style_mini_triage_summary.md` | Consolidated IOC-style mini triage summary |
| `evidence/lab08_05_final_closure_summary.md` | Final lab closure summary |

---

## Key findings

- The host had readable local network visibility through PowerShell.
- TCP and UDP activity was summarized without exporting raw IPs, DNS names or command lines.
- Listening ports were classified by exposure context and analyst action.
- Windows service ports such as RPC/NetBIOS/SMB were identified as review-worthy.
- TeamViewer and Syncthing were identified as tools requiring context because remote access and synchronization can increase exposure if misconfigured.
- Active TCP connections were linked to process names and remote service categories without exporting remote IPs.
- One CloseWait state was identified for review if recurring.
- No confirmed incident or evidence of compromise was identified from the exported sanitized evidence.

---

## SOC interpretation

The collected evidence supports a conservative SOC L1 decision:

**Priority:** P3 — Review and monitor  
**Escalation:** No immediate escalation  
**Incident confirmed:** No  
**Recommended action:** Document exposure, verify expected services and monitor recurring patterns.

---

## Skills demonstrated

- Windows TCP/UDP connection review.
- Listening-port exposure analysis.
- Process-to-network context review.
- Sanitized PowerShell evidence collection.
- Basic IOC-style triage reasoning.
- SOC-style classification: Monitor / Review / Document.
- Technical reporting in Markdown.
- Privacy-conscious evidence handling.
- Conservative analyst decision-making.

---

## Limitations

This lab does not include:

- raw IP address publication,
- DNS name publication,
- command-line export,
- packet capture,
- SIEM correlation,
- EDR telemetry,
- threat intelligence enrichment,
- reputation lookup,
- long-term baseline,
- enterprise/domain network context.

The lab is designed as a defensive portfolio exercise and should not be interpreted as a full incident response investigation.

---

## Portfolio statement

Network connections and IOC-style defensive review lab focused on SOC L1-style triage: TCP/UDP activity, listening-port exposure, process-to-network context, sanitized evidence handling and conservative analyst reporting.
