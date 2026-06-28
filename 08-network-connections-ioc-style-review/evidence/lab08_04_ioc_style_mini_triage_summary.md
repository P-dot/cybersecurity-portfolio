# Lab 08.4 — IOC-style Mini Triage Summary: Network Connections Review

## 1. Objective

This report consolidates the sanitized evidence collected during Lab 08:

- **Lab 08.1:** Network connections inventory.
- **Lab 08.2:** Listening ports and exposure review.
- **Lab 08.3:** Active connections and process context review.

The goal is to produce a short SOC-style triage summary focused on local network visibility, exposure review and basic IOC-style reasoning without exporting sensitive data.

---

## 2. Scope and privacy controls

**Environment:** Windows lab host used for defensive cybersecurity portfolio work.  
**Collection mode:** read-only PowerShell evidence collection.  
**Data handling:** sanitized evidence only.

The exported evidence intentionally excludes:

- raw IP addresses,
- DNS names,
- usernames,
- process paths,
- command lines,
- personal data.

This lab is defensive and does not scan, attack or interact with third-party systems.

---

## 3. Network visibility summary

The host showed the following local network visibility:

| Area | Result |
|---|---:|
| Network adapters detected | 5 |
| Active adapters | 3 |
| Disconnected adapters | 2 |
| IPv4 entries detected | 8 |
| IPv6 entries detected | 8 |
| TCP connection entries | 67 |
| UDP endpoint entries | 53 |

### TCP state summary

| TCP state | Count |
|---|---:|
| Listen | 25 |
| Bound | 24 |
| Established | 14 |
| CloseWait | 3 |
| TimeWait | 1 |

### Main TCP processes observed

| Process | TCP entries |
|---|---:|
| svchost | 17 |
| SearchApp | 16 |
| syncthing | 7 |
| System | 5 |
| OneDrive.Sync.Service | 5 |
| MsMpEng | 4 |

### Main UDP processes observed

| Process | UDP entries |
|---|---:|
| svchost | 36 |
| System | 6 |
| TeamViewer_Service | 5 |
| syncthing | 5 |
| msedgewebview2 | 1 |

---

## 4. Listening ports and exposure review

The listening-port review identified:

| Finding | Result |
|---|---:|
| Total listening TCP entries | 25 |
| Network category | Public |
| Bindings on all interfaces | 18 |
| Loopback-only bindings | 4 |
| Specific local interface bindings | 3 |

### Analyst action summary

| Action | Count |
|---|---:|
| Monitor | 14 |
| Review | 9 |
| Document | 2 |

### Exposure points requiring analyst context

| Port / service area | Interpretation | Action |
|---|---|---|
| 135 | Windows RPC service exposure | Review |
| 139 | NetBIOS / Windows service exposure | Review |
| 445 | SMB / Windows service exposure | Review |
| 5939 | TeamViewer-related service, loopback only | Review |
| 8384 | Syncthing web interface, loopback only | Review |
| 22000 | Syncthing synchronization, all interfaces | Review |
| 49664–49678 range | Dynamic/high Windows ports | Monitor |
| 5357 | Windows device/service discovery | Monitor |
| 5040 | Windows connected devices/platform service | Document |

### Exposure interpretation

- The Windows network profile is **Public**, which is a positive defensive context.
- Windows service ports such as 135, 139 and 445 can be expected on Windows hosts, but remain sensitive and should be reviewed against firewall/profile configuration.
- TeamViewer and Syncthing require context because remote access or synchronization tooling can expand exposure if misconfigured.
- Dynamic high Windows ports are common but should be monitored when persistent or linked to unexpected processes.

---

## 5. Active connections and process context

The active TCP connection review identified:

| Area | Result |
|---|---:|
| Active TCP entries reviewed | 7 |
| Established | 6 |
| CloseWait | 1 |

### Analyst action summary

| Action | Count |
|---|---:|
| Monitor | 5 |
| Document | 1 |
| Review | 1 |

### Active process summary

| Process | Active TCP entries |
|---|---:|
| syncthing | 4 |
| svchost | 1 |
| msedgewebview2 | 1 |
| SearchApp | 1 |

### Process category summary

| Category | Count |
|---|---:|
| Synchronization service | 4 |
| User/web-facing application | 2 |
| Windows system component | 1 |

### Remote service category summary

| Remote service category | Count |
|---|---:|
| HTTPS / encrypted web or API traffic | 3 |
| Dynamic/high remote port | 2 |
| Syncthing synchronization | 1 |
| Other remote service requiring context | 1 |

### Active connection interpretation

- Most active connections are linked to expected categories: synchronization, Windows components or user/web-facing applications.
- Syncthing accounts for most active TCP entries.
- HTTPS traffic from user-facing or Windows components is expected but still context-dependent.
- One **CloseWait** state associated with SearchApp was classified for review.
- No unknown process context was observed in the sanitized active connection review.

---

## 6. IOC-style triage assessment

This lab uses “IOC-style” reasoning in a conservative way. It does not claim that any connection, port or process is malicious. Instead, it identifies local indicators that would deserve analyst attention in a SOC workflow.

### Indicators to monitor

| Indicator type | Observation | SOC decision |
|---|---|---|
| Windows service exposure | 135, 139, 445 present | Review firewall/profile context |
| Remote-access tooling | TeamViewer service present, loopback only | Verify expected use |
| Synchronization tooling | Syncthing ports/processes present | Verify intended scope |
| Dynamic high ports | Multiple Windows high ports present | Monitor |
| CloseWait state | One SearchApp CloseWait entry | Review if recurring |
| HTTPS activity | Present from user/system processes | Monitor in context |

---

## 7. Overall SOC classification

| Field | Assessment |
|---|---|
| Classification | Network visibility and exposure review |
| Priority | P3 — Review and monitor |
| Confirmed incident | No |
| Evidence of compromise | Not indicated in exported evidence |
| Escalation required | No immediate escalation |
| Recommended action | Document exposure, verify expected tools, monitor recurring patterns |

---

## 8. Key limitations

This lab intentionally avoids sensitive exports and does not represent a full incident response investigation.

Limitations:

- No raw IP addresses exported.
- No DNS names exported.
- No command lines or process paths exported.
- No packet capture in this lab phase.
- No SIEM correlation.
- No threat intelligence enrichment.
- No reputation lookup.
- No EDR telemetry.
- No historical baseline across multiple days.
- No enterprise network context.

These limitations are acceptable for a defensive portfolio lab and should be clearly stated.

---

## 9. Recommended next actions

| Area | Recommendation |
|---|---|
| Windows service ports | Confirm firewall posture for 135, 139 and 445 under Public profile. |
| Remote-access tooling | Confirm TeamViewer is expected, controlled and not externally exposed unexpectedly. |
| Synchronization tooling | Confirm Syncthing ports are intended and access scope is appropriate. |
| Active connections | Monitor recurrence of CloseWait entries and unusual remote port categories. |
| Documentation | Keep evidence sanitized for public GitHub publication. |
| Portfolio | Use this lab to demonstrate network exposure review and SOC-style prioritization. |

---

## 10. Analyst conclusion

The Windows lab host shows normal but review-worthy local network activity: Windows service exposure, synchronization services, remote-access tooling context and expected HTTPS traffic. The evidence does not indicate a confirmed incident or compromise.

The correct analyst decision is to **document, verify expected services and monitor**, not to escalate as a confirmed security incident.

**Lab 08.4 status:** completed.
