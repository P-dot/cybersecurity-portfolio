# Lab 06.4 — SOC executive report

Date: 2026-06-23 13:17:57 UTC

## Executive summary

This report converts 70 technical events from Mission 6.3 into an executive SOC-style summary. Findings are grouped into security-relevant events, privileged/audit activity, operational issues, lab infrastructure events and residual low-value noise.

The reviewed evidence does not automatically prove compromise. The output supports analyst review by summarising what deserves attention and what appears to be expected lab or operational noise.

## Scope

- Input technical report: `/home/vbox/lab06/evidencias/lab06_03_defensive_pattern_extraction.md`
- Output executive report: `/home/vbox/lab06/reportes/lab06_04_soc_executive_report.md`
- Source context: Lab 05 Linux evidence processed through Lab 06.3 defensive pattern extraction
- Method: static parsing, counting, categorisation and analyst-oriented summarisation

## Category summary

| Executive category | Events |
|---|---:|
| Security-relevant events | 12 |
| Privileged activity / audit trail | 15 |
| Operational / technical issues | 21 |
| Lab infrastructure events | 21 |
| Noise / low-value findings | 1 |

## Severity summary

| Severity | Events |
|---|---:|
| Low | 38 |
| Informational | 18 |
| Low-Medium | 13 |
| Medium | 1 |

## Event type summary

| Event type | Events |
|---|---:|
| Kernel or virtualization warning | 11 |
| Sudo command execution | 10 |
| Failed service | 10 |
| DNS or network issue | 10 |
| VirtualBox shared-folder failure | 8 |
| Scheduled root cron session | 5 |
| Sudo authentication failure | 5 |
| Authentication failure | 4 |
| VirtualBox shared-folder success | 3 |
| Sudo incorrect password attempts | 3 |
| Storage capacity warning | 1 |

## Key findings

- The script reviewed 70 extracted technical events from Mission 6.3 and grouped them into executive SOC categories.
- Security-relevant events were observed, mainly authentication and sudo-related failures. In this lab context they are interpreted as low to low-medium severity unless repetition, remote origin or unexpected users are confirmed.
- No clear SSH authentication activity was extracted from the reviewed evidence.
- Operational and technical issues were present, including failed services, DNS/network problems or storage capacity warnings. These affect reliability and evidence collection more than direct compromise indicators in this lab.
- Several findings are related to the virtualized lab environment, especially VirtualBox shared-folder behavior and kernel/virtualization warnings.
- Residual low-value noise was detected and separated from analyst-relevant findings, improving report quality compared with raw keyword matching.
- No high or critical severity finding was identified by the static rules used in this lab.
- No clear evidence of compromise is concluded by this script; final judgment requires analyst review and correlation.

## Representative samples by category

### Security-relevant events

| Event type | Severity | Source | Line | Sample |
|---|---|---|---:|---|
| Authentication failure | Low | lab05_02_auth_sudo_sessions.txt | 149 | `Jun 21 10:31:46 vbox login[702]: pam_unix(login:auth): authentication failure; logname=LOGIN uid=0 euid=0 tty=/dev/tty1 ruser= rhost=` |
| Authentication failure | Low | lab05_02_auth_sudo_sessions.txt | 150 | `Jun 21 10:31:49 vbox login[702]: FAILED LOGIN (1) on '/dev/tty1' FOR 'UNKNOWN', Authentication failure` |
| Sudo authentication failure | Low | lab05_02_auth_sudo_sessions.txt | 154 | `Jun 21 10:59:45 vbox sudo: pam_unix(sudo:auth): authentication failure; logname=vbox uid=1000 euid=0 tty=/dev/tty1 ruser=vbox rhost=  user=vbox` |
| Sudo authentication failure | Low | lab05_02_auth_sudo_sessions.txt | 210 | `Jun 21 10:59:45 vbox sudo: pam_unix(sudo:auth): authentication failure; logname=vbox uid=1000 euid=0 tty=/dev/tty1 ruser=vbox rhost=  user=vbox` |
| Authentication failure | Low | lab05_02_auth_sudo_sessions.txt | 218 | `Jun 21 10:31:46 vbox login[702]: pam_unix(login:auth): authentication failure; logname=LOGIN uid=0 euid=0 tty=/dev/tty1 ruser= rhost=` |

### Privileged activity / audit trail

| Event type | Severity | Source | Line | Sample |
|---|---|---|---:|---|
| Scheduled root cron session | Informational | lab05_02_auth_sudo_sessions.txt | 83 | `Jun 19 10:17:02 vbox CRON[1315]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)` |
| Scheduled root cron session | Informational | lab05_02_auth_sudo_sessions.txt | 85 | `Jun 20 14:17:01 vbox CRON[1507]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)` |
| Scheduled root cron session | Informational | lab05_02_auth_sudo_sessions.txt | 87 | `Jun 20 15:17:01 vbox CRON[1534]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)` |
| Scheduled root cron session | Informational | lab05_02_auth_sudo_sessions.txt | 89 | `Jun 21 09:17:01 vbox CRON[1617]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)` |
| Sudo command execution | Informational | lab05_02_auth_sudo_sessions.txt | 91 | `Jun 21 09:39:37 vbox sudo:     vbox : TTY=tty1 ; PWD=/home/vbox/lab05 ; USER=root ; COMMAND=/usr/bin/journalctl --list-boots` |

### Operational / technical issues

| Event type | Severity | Source | Line | Sample |
|---|---|---|---:|---|
| Failed service | Low | lab05_03_system_health_errors.txt | 26 | `● fwupd-refresh.service loaded failed failed Refresh fwupd metadata and update motd` |
| Failed service | Low | lab05_03_system_health_errors.txt | 35 | `● fwupd-refresh.service loaded failed failed Refresh fwupd metadata and update motd` |
| DNS or network issue | Low-Medium | lab05_03_system_health_errors.txt | 43 | `Jun 18 15:43:25 vbox systemd-resolved[606]: Using degraded feature set TCP instead of UDP for DNS server 192.168.1.1.` |
| DNS or network issue | Low-Medium | lab05_03_system_health_errors.txt | 44 | `Jun 18 16:13:50 vbox systemd-resolved[606]: Using degraded feature set UDP instead of UDP+EDNS0 for DNS server 192.168.1.1.` |
| Failed service | Low | lab05_03_system_health_errors.txt | 51 | `Jun 19 10:20:38 vbox systemd[1]: fwupd-refresh.service: Failed with result 'exit-code'.` |

### Lab infrastructure events

| Event type | Severity | Source | Line | Sample |
|---|---|---|---:|---|
| Kernel or virtualization warning | Low | lab05_03_system_health_errors.txt | 49 | `Jun 19 09:48:47 vbox kernel: 09:48:47.825331 timesync vgsvcTimeSyncWorker: Radical host time change: 62 006 623 000 000ns (HostNow=1 781 862 527 807 000 000 ns HostLast=1 781 800 521 184 000 000 ns)` |
| Kernel or virtualization warning | Low | lab05_03_system_health_errors.txt | 50 | `Jun 19 09:48:57 vbox kernel: 09:48:57.829235 timesync vgsvcTimeSyncWorker: Radical guest time change: 62 007 277 670 000ns (GuestNow=1 781 862 537 829 191 000 ns GuestLast=1 781 800 530 551 521 000 ns fSetTimeLastLoop=true)` |
| Kernel or virtualization warning | Low | lab05_03_system_health_errors.txt | 57 | `Jun 20 13:52:15 vbox kernel: 13:52:15.319874 timesync vgsvcTimeSyncWorker: Radical host time change: 97 216 545 000 000ns (HostNow=1 781 963 535 303 000 000 ns HostLast=1 781 866 318 758 000 000 ns)` |
| Kernel or virtualization warning | Low | lab05_03_system_health_errors.txt | 58 | `Jun 20 13:52:25 vbox kernel: 13:52:25.322917 timesync vgsvcTimeSyncWorker: Radical guest time change: 97 216 598 590 000ns (GuestNow=1 781 963 545 322 845 000 ns GuestLast=1 781 866 328 724 255 000 ns fSetTimeLastLoop=true)` |
| Kernel or virtualization warning | Low | lab05_03_system_health_errors.txt | 65 | `Jun 21 08:31:34 vbox kernel: 08:31:34.246882 timesync vgsvcTimeSyncWorker: Radical host time change: 59 126 893 000 000ns (HostNow=1 782 030 694 232 000 000 ns HostLast=1 781 971 567 339 000 000 ns)` |

### Noise / low-value findings

| Event type | Severity | Source | Line | Sample |
|---|---|---|---:|---|
| Kernel or virtualization warning | Low | lab05_02_auth_sudo_sessions.txt | 65 | `systemd-timesync                           **Never logged in**` |

## Recommended analyst actions

- Review authentication and sudo failures for repetition, unexpected users, remote origin, unusual timing and affected accounts.
- Keep sudo command execution as an audit trail and review commands only if user, path or timing is unexpected.
- Review failed services by business or system criticality; fwupd-refresh failures can be treated as maintenance/update issues in this lab.
- Check DNS, gateway, NAT and external update reachability when updates or package refreshes fail.
- Monitor free space in the shared evidence export folder to avoid future collection or reporting failures.
- Document VirtualBox and lab-infrastructure warnings as environmental baseline unless they combine with instability or suspicious activity.
- Use this executive report together with the technical event table from Mission 6.3; do not use it as a standalone incident verdict.

## SOC interpretation

This report is an analyst-support artifact. It summarises extracted findings and separates security-relevant events from operational issues, lab infrastructure events and residual noise.

It should not be interpreted as an autonomous detection engine or final incident decision. A real SOC workflow would require correlation with timestamps, users, source IPs, asset criticality, baselines, SIEM alerts and business context.

## Limitations

- Static rules only; no machine learning or behavioural baseline.
- No enrichment with threat intelligence, IP reputation or asset inventory.
- No timeline reconstruction across multiple systems.
- No incident response action is performed.
- Findings come from a controlled lab environment, not a production SIEM.

## Conclusion

Mission 6.4 demonstrates the ability to convert technical log-extraction output into a clearer SOC-style executive report. The report helps separate review-worthy findings from operational and lab-context noise while preserving a conservative analyst interpretation.

## Mission status

Mission 6.4 validated.
