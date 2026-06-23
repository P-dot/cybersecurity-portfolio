# Lab 06.5 — Basic SOC action classifier

Date: 2026-06-23 13:44:06 UTC

## Executive summary

This report maps 70 extracted technical events from Mission 6.3 to initial SOC analyst actions. The goal is to support triage by separating events that should be reviewed, monitored, documented or not escalated.

No automatic incident verdict is produced. Actions are conservative and must be validated by an analyst using context, repetition, source, users and operational impact.

## Scope

- Input technical report: `/home/vbox/lab06/evidencias/lab06_03_defensive_pattern_extraction.md`
- Output action report: `/home/vbox/lab06/reportes/lab06_05_soc_action_classifier.md`
- Method: static rule-based action mapping
- Environment: controlled defensive lab

## Action summary

| SOC action | Events |
|---|---:|
| Monitor | 20 |
| No escalation | 19 |
| Document | 18 |
| Review | 9 |
| Needs analyst attention | 4 |

## Priority summary

| Priority | Events |
|---|---:|
| P4 | 37 |
| P3 | 29 |
| P2 | 4 |

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

## SOC action table

| ID | Event type | Severity | Action | Priority | Source | Line | Rationale | Sample |
|---:|---|---|---|---|---|---:|---|---|
| 1 | Kernel or virtualization warning | Low | No escalation | P4 | lab05_02_auth_sudo_sessions.txt | 65 | Residual low-value noise detected. Document as parser limitation; do not escalate without additional suspicious context. | `systemd-timesync                           **Never logged in**` |
| 2 | Scheduled root cron session | Informational | Document | P4 | lab05_02_auth_sudo_sessions.txt | 83 | Expected or useful audit-trail activity. Keep as context, but do not escalate unless user, command, timing or frequency is unexpected. | `Jun 19 10:17:02 vbox CRON[1315]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)` |
| 3 | Scheduled root cron session | Informational | Document | P4 | lab05_02_auth_sudo_sessions.txt | 85 | Expected or useful audit-trail activity. Keep as context, but do not escalate unless user, command, timing or frequency is unexpected. | `Jun 20 14:17:01 vbox CRON[1507]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)` |
| 4 | Scheduled root cron session | Informational | Document | P4 | lab05_02_auth_sudo_sessions.txt | 87 | Expected or useful audit-trail activity. Keep as context, but do not escalate unless user, command, timing or frequency is unexpected. | `Jun 20 15:17:01 vbox CRON[1534]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)` |
| 5 | Scheduled root cron session | Informational | Document | P4 | lab05_02_auth_sudo_sessions.txt | 89 | Expected or useful audit-trail activity. Keep as context, but do not escalate unless user, command, timing or frequency is unexpected. | `Jun 21 09:17:01 vbox CRON[1617]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)` |
| 6 | Sudo command execution | Informational | Document | P4 | lab05_02_auth_sudo_sessions.txt | 91 | Expected or useful audit-trail activity. Keep as context, but do not escalate unless user, command, timing or frequency is unexpected. | `Jun 21 09:39:37 vbox sudo:     vbox : TTY=tty1 ; PWD=/home/vbox/lab05 ; USER=root ; COMMAND=/usr/bin/journalctl --list-boots` |
| 7 | Sudo command execution | Informational | Document | P4 | lab05_02_auth_sudo_sessions.txt | 94 | Expected or useful audit-trail activity. Keep as context, but do not escalate unless user, command, timing or frequency is unexpected. | `Jun 21 09:39:37 vbox sudo:     vbox : TTY=tty1 ; PWD=/home/vbox/lab05 ; USER=root ; COMMAND=/usr/bin/tail -n 20 /var/log/auth.log` |
| 8 | Sudo command execution | Informational | Document | P4 | lab05_02_auth_sudo_sessions.txt | 97 | Expected or useful audit-trail activity. Keep as context, but do not escalate unless user, command, timing or frequency is unexpected. | `Jun 21 09:39:37 vbox sudo:     vbox : TTY=tty1 ; PWD=/home/vbox/lab05 ; USER=root ; COMMAND=/usr/bin/tail -n 20 /var/log/syslog` |
| 9 | Sudo command execution | Informational | Document | P4 | lab05_02_auth_sudo_sessions.txt | 100 | Expected or useful audit-trail activity. Keep as context, but do not escalate unless user, command, timing or frequency is unexpected. | `Jun 21 10:02:37 vbox sudo:     vbox : TTY=tty1 ; PWD=/home/vbox/lab05 ; USER=root ; COMMAND=/usr/bin/journalctl --list-boots` |
| 10 | Sudo command execution | Informational | Document | P4 | lab05_02_auth_sudo_sessions.txt | 103 | Expected or useful audit-trail activity. Keep as context, but do not escalate unless user, command, timing or frequency is unexpected. | `Jun 21 10:02:37 vbox sudo:     vbox : TTY=tty1 ; PWD=/home/vbox/lab05 ; USER=root ; COMMAND=/usr/bin/tail -n 20 /var/log/auth.log` |
| 11 | Sudo command execution | Informational | Document | P4 | lab05_02_auth_sudo_sessions.txt | 106 | Expected or useful audit-trail activity. Keep as context, but do not escalate unless user, command, timing or frequency is unexpected. | `Jun 21 10:02:38 vbox sudo:     vbox : TTY=tty1 ; PWD=/home/vbox/lab05 ; USER=root ; COMMAND=/usr/bin/tail -n 20 /var/log/syslog` |
| 12 | Sudo command execution | Informational | Document | P4 | lab05_02_auth_sudo_sessions.txt | 109 | Expected or useful audit-trail activity. Keep as context, but do not escalate unless user, command, timing or frequency is unexpected. | `Jun 21 10:10:55 vbox sudo:     vbox : TTY=tty1 ; PWD=/home/vbox/lab05 ; USER=root ; COMMAND=/usr/bin/cp /home/vbox/lab05/evidencias/lab05_01_log_sources.txt /mnt/capturas/` |
| 13 | Scheduled root cron session | Informational | Document | P4 | lab05_02_auth_sudo_sessions.txt | 112 | Expected or useful audit-trail activity. Keep as context, but do not escalate unless user, command, timing or frequency is unexpected. | `Jun 21 10:17:01 vbox CRON[1721]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)` |
| 14 | Sudo command execution | Informational | Document | P4 | lab05_02_auth_sudo_sessions.txt | 114 | Expected or useful audit-trail activity. Keep as context, but do not escalate unless user, command, timing or frequency is unexpected. | `Jun 21 10:18:47 vbox sudo:     vbox : TTY=tty1 ; PWD=/home/vbox/lab05 ; USER=root ; COMMAND=/usr/bin/mkdir -p /mnt/capturas` |
| 15 | Sudo command execution | Informational | Document | P4 | lab05_02_auth_sudo_sessions.txt | 117 | Expected or useful audit-trail activity. Keep as context, but do not escalate unless user, command, timing or frequency is unexpected. | `Jun 21 10:19:49 vbox sudo:     vbox : TTY=tty1 ; PWD=/home/vbox/lab05 ; USER=root ; COMMAND=/usr/bin/mount -t vboxsf Capturas /mnt/capturas` |
| 16 | Sudo command execution | Informational | Document | P4 | lab05_02_auth_sudo_sessions.txt | 120 | Expected or useful audit-trail activity. Keep as context, but do not escalate unless user, command, timing or frequency is unexpected. | `Jun 21 10:20:12 vbox sudo:     vbox : TTY=tty1 ; PWD=/home/vbox/lab05 ; USER=root ; COMMAND=/usr/bin/mount -t vboxsf Capturas /mnt/05_capturas` |
| 17 | Authentication failure | Low | Review | P3 | lab05_02_auth_sudo_sessions.txt | 149 | Security-relevant event. Review user, source, timing, repetition and whether the activity was expected in the lab or production context. | `Jun 21 10:31:46 vbox login[702]: pam_unix(login:auth): authentication failure; logname=LOGIN uid=0 euid=0 tty=/dev/tty1 ruser= rhost=` |
| 18 | Authentication failure | Low | Review | P3 | lab05_02_auth_sudo_sessions.txt | 150 | Security-relevant event. Review user, source, timing, repetition and whether the activity was expected in the lab or production context. | `Jun 21 10:31:49 vbox login[702]: FAILED LOGIN (1) on '/dev/tty1' FOR 'UNKNOWN', Authentication failure` |
| 19 | Sudo authentication failure | Low | Review | P3 | lab05_02_auth_sudo_sessions.txt | 154 | Security-relevant event. Review user, source, timing, repetition and whether the activity was expected in the lab or production context. | `Jun 21 10:59:45 vbox sudo: pam_unix(sudo:auth): authentication failure; logname=vbox uid=1000 euid=0 tty=/dev/tty1 ruser=vbox rhost=  user=vbox` |
| 20 | Sudo authentication failure | Low | Review | P3 | lab05_02_auth_sudo_sessions.txt | 210 | Security-relevant event. Review user, source, timing, repetition and whether the activity was expected in the lab or production context. | `Jun 21 10:59:45 vbox sudo: pam_unix(sudo:auth): authentication failure; logname=vbox uid=1000 euid=0 tty=/dev/tty1 ruser=vbox rhost=  user=vbox` |
| 21 | Authentication failure | Low | Review | P3 | lab05_02_auth_sudo_sessions.txt | 218 | Security-relevant event. Review user, source, timing, repetition and whether the activity was expected in the lab or production context. | `Jun 21 10:31:46 vbox login[702]: pam_unix(login:auth): authentication failure; logname=LOGIN uid=0 euid=0 tty=/dev/tty1 ruser= rhost=` |
| 22 | Authentication failure | Low | Review | P3 | lab05_02_auth_sudo_sessions.txt | 219 | Security-relevant event. Review user, source, timing, repetition and whether the activity was expected in the lab or production context. | `Jun 21 10:31:49 vbox login[702]: FAILED LOGIN (1) on '/dev/tty1' FOR 'UNKNOWN', Authentication failure` |
| 23 | Sudo authentication failure | Low | Review | P3 | lab05_02_auth_sudo_sessions.txt | 220 | Security-relevant event. Review user, source, timing, repetition and whether the activity was expected in the lab or production context. | `Jun 21 10:59:45 vbox sudo: pam_unix(sudo:auth): authentication failure; logname=vbox uid=1000 euid=0 tty=/dev/tty1 ruser=vbox rhost=  user=vbox` |
| 24 | Sudo authentication failure | Low | Review | P3 | lab05_02_auth_sudo_sessions.txt | 239 | Security-relevant event. Review user, source, timing, repetition and whether the activity was expected in the lab or production context. | `May 26 17:54:53 vbox sudo[1292]: pam_unix(sudo:auth): authentication failure; logname=vbox uid=1000 euid=0 tty=/dev/tty1 ruser=vbox rhost=  user=vbox` |
| 25 | Sudo authentication failure | Low | Review | P3 | lab05_02_auth_sudo_sessions.txt | 296 | Security-relevant event. Review user, source, timing, repetition and whether the activity was expected in the lab or production context. | `Jun 21 10:59:45 vbox sudo[1218]: pam_unix(sudo:auth): authentication failure; logname=vbox uid=1000 euid=0 tty=/dev/tty1 ruser=vbox rhost=  user=vbox` |
| 26 | Failed service | Low | Monitor | P3 | lab05_03_system_health_errors.txt | 26 | Operational issue observed. Monitor for recurrence and assess whether it affects updates, availability, collection or reporting reliability. | `● fwupd-refresh.service loaded failed failed Refresh fwupd metadata and update motd` |
| 27 | Failed service | Low | Monitor | P3 | lab05_03_system_health_errors.txt | 35 | Operational issue observed. Monitor for recurrence and assess whether it affects updates, availability, collection or reporting reliability. | `● fwupd-refresh.service loaded failed failed Refresh fwupd metadata and update motd` |
| 28 | DNS or network issue | Low-Medium | Monitor | P3 | lab05_03_system_health_errors.txt | 43 | Operational issue observed. Monitor for recurrence and assess whether it affects updates, availability, collection or reporting reliability. | `Jun 18 15:43:25 vbox systemd-resolved[606]: Using degraded feature set TCP instead of UDP for DNS server 192.168.1.1.` |
| 29 | DNS or network issue | Low-Medium | Monitor | P3 | lab05_03_system_health_errors.txt | 44 | Operational issue observed. Monitor for recurrence and assess whether it affects updates, availability, collection or reporting reliability. | `Jun 18 16:13:50 vbox systemd-resolved[606]: Using degraded feature set UDP instead of UDP+EDNS0 for DNS server 192.168.1.1.` |
| 30 | Kernel or virtualization warning | Low | No escalation | P4 | lab05_03_system_health_errors.txt | 49 | Lab infrastructure or virtualization-related finding. Treat as baseline/noise unless combined with instability or other suspicious evidence. | `Jun 19 09:48:47 vbox kernel: 09:48:47.825331 timesync vgsvcTimeSyncWorker: Radical host time change: 62 006 623 000 000ns (HostNow=1 781 862 527 807 000 000 ns HostLast=1 781 800 521 184 000 000 ns)` |
| 31 | Kernel or virtualization warning | Low | No escalation | P4 | lab05_03_system_health_errors.txt | 50 | Lab infrastructure or virtualization-related finding. Treat as baseline/noise unless combined with instability or other suspicious evidence. | `Jun 19 09:48:57 vbox kernel: 09:48:57.829235 timesync vgsvcTimeSyncWorker: Radical guest time change: 62 007 277 670 000ns (GuestNow=1 781 862 537 829 191 000 ns GuestLast=1 781 800 530 551 521 000 ns fSetTimeLastLoop=true)` |
| 32 | Failed service | Low | Monitor | P3 | lab05_03_system_health_errors.txt | 51 | Operational issue observed. Monitor for recurrence and assess whether it affects updates, availability, collection or reporting reliability. | `Jun 19 10:20:38 vbox systemd[1]: fwupd-refresh.service: Failed with result 'exit-code'.` |
| 33 | Failed service | Low | Monitor | P3 | lab05_03_system_health_errors.txt | 52 | Operational issue observed. Monitor for recurrence and assess whether it affects updates, availability, collection or reporting reliability. | `Jun 19 10:20:38 vbox systemd[1]: Failed to start Refresh fwupd metadata and update motd.` |
| 34 | Kernel or virtualization warning | Low | No escalation | P4 | lab05_03_system_health_errors.txt | 57 | Lab infrastructure or virtualization-related finding. Treat as baseline/noise unless combined with instability or other suspicious evidence. | `Jun 20 13:52:15 vbox kernel: 13:52:15.319874 timesync vgsvcTimeSyncWorker: Radical host time change: 97 216 545 000 000ns (HostNow=1 781 963 535 303 000 000 ns HostLast=1 781 866 318 758 000 000 ns)` |
| 35 | Kernel or virtualization warning | Low | No escalation | P4 | lab05_03_system_health_errors.txt | 58 | Lab infrastructure or virtualization-related finding. Treat as baseline/noise unless combined with instability or other suspicious evidence. | `Jun 20 13:52:25 vbox kernel: 13:52:25.322917 timesync vgsvcTimeSyncWorker: Radical guest time change: 97 216 598 590 000ns (GuestNow=1 781 963 545 322 845 000 ns GuestLast=1 781 866 328 724 255 000 ns fSetTimeLastLoop=true)` |
| 36 | Failed service | Low | Monitor | P3 | lab05_03_system_health_errors.txt | 59 | Operational issue observed. Monitor for recurrence and assess whether it affects updates, availability, collection or reporting reliability. | `Jun 20 14:52:42 vbox systemd[1]: fwupd-refresh.service: Failed with result 'exit-code'.` |
| 37 | Failed service | Low | Monitor | P3 | lab05_03_system_health_errors.txt | 60 | Operational issue observed. Monitor for recurrence and assess whether it affects updates, availability, collection or reporting reliability. | `Jun 20 14:52:42 vbox systemd[1]: Failed to start Refresh fwupd metadata and update motd.` |
| 38 | Kernel or virtualization warning | Low | No escalation | P4 | lab05_03_system_health_errors.txt | 65 | Lab infrastructure or virtualization-related finding. Treat as baseline/noise unless combined with instability or other suspicious evidence. | `Jun 21 08:31:34 vbox kernel: 08:31:34.246882 timesync vgsvcTimeSyncWorker: Radical host time change: 59 126 893 000 000ns (HostNow=1 782 030 694 232 000 000 ns HostLast=1 781 971 567 339 000 000 ns)` |
| 39 | Kernel or virtualization warning | Low | No escalation | P4 | lab05_03_system_health_errors.txt | 66 | Lab infrastructure or virtualization-related finding. Treat as baseline/noise unless combined with instability or other suspicious evidence. | `Jun 21 08:31:44 vbox kernel: 08:31:44.258613 timesync vgsvcTimeSyncWorker: Radical guest time change: 59 126 951 500 000ns (GuestNow=1 782 030 704 258 573 000 ns GuestLast=1 781 971 577 307 073 000 ns fSetTimeLastLoop=true)` |
| 40 | VirtualBox shared-folder failure | Low | No escalation | P4 | lab05_03_system_health_errors.txt | 69 | Lab infrastructure or virtualization-related finding. Treat as baseline/noise unless combined with instability or other suspicious evidence. | `Jun 21 10:19:49 vbox kernel: vboxsf: SHFL_FN_MAP_FOLDER failed for 'Capturas': share not found` |
| 41 | VirtualBox shared-folder failure | Low | No escalation | P4 | lab05_03_system_health_errors.txt | 70 | Lab infrastructure or virtualization-related finding. Treat as baseline/noise unless combined with instability or other suspicious evidence. | `Jun 21 10:20:33 vbox kernel: vboxsf: SHFL_FN_MAP_FOLDER failed for 'Capturas': share not found` |
| 42 | VirtualBox shared-folder failure | Low | No escalation | P4 | lab05_03_system_health_errors.txt | 71 | Lab infrastructure or virtualization-related finding. Treat as baseline/noise unless combined with instability or other suspicious evidence. | `Jun 21 10:21:47 vbox kernel: vboxsf: SHFL_FN_MAP_FOLDER failed for 'Capturas': share not found` |
| 43 | VirtualBox shared-folder failure | Low | No escalation | P4 | lab05_03_system_health_errors.txt | 72 | Lab infrastructure or virtualization-related finding. Treat as baseline/noise unless combined with instability or other suspicious evidence. | `Jun 21 10:23:35 vbox kernel: vboxsf: SHFL_FN_MAP_FOLDER failed for 'Capturas': share not found` |
| 44 | Kernel or virtualization warning | Low | No escalation | P4 | lab05_03_system_health_errors.txt | 80 | Lab infrastructure or virtualization-related finding. Treat as baseline/noise unless combined with instability or other suspicious evidence. | `Jun 21 10:31:19 vbox kernel: RETBleed: WARNING: Spectre v2 mitigation leaves CPU vulnerable to RETBleed attacks, data leaks possible!` |
| 45 | Kernel or virtualization warning | Low | No escalation | P4 | lab05_03_system_health_errors.txt | 81 | Lab infrastructure or virtualization-related finding. Treat as baseline/noise unless combined with instability or other suspicious evidence. | `Jun 21 10:31:19 vbox kernel: APIC calibration not consistent with PM-Timer: 116ms instead of 100ms` |
| 46 | Kernel or virtualization warning | Low | No escalation | P4 | lab05_03_system_health_errors.txt | 84 | Lab infrastructure or virtualization-related finding. Treat as baseline/noise unless combined with instability or other suspicious evidence. | `Jun 21 10:31:19 vbox kernel: [drm:vmw_host_printf [vmwgfx]] *ERROR* Failed to send host log message.` |
| 47 | Kernel or virtualization warning | Low | No escalation | P4 | lab05_03_system_health_errors.txt | 87 | Lab infrastructure or virtualization-related finding. Treat as baseline/noise unless combined with instability or other suspicious evidence. | `Jun 21 10:31:24 vbox kernel: vboxguest: loading out-of-tree module taints kernel.` |
| 48 | VirtualBox shared-folder success | Informational | Document | P4 | lab05_03_system_health_errors.txt | 110 | Expected or useful audit-trail activity. Keep as context, but do not escalate unless user, command, timing or frequency is unexpected. | `Jun 21 10:31:35 vbox kernel: 10:31:35.375183 automount vbsvcAutomounterMountIt: Successfully mounted 'Capturas' on '/mnt/capturas'` |
| 49 | Failed service | Low | Monitor | P3 | lab05_03_system_health_errors.txt | 118 | Operational issue observed. Monitor for recurrence and assess whether it affects updates, availability, collection or reporting reliability. | `Jun 21 16:58:54 vbox systemd[1]: fwupd-refresh.service: Failed with result 'exit-code'.` |
| 50 | Failed service | Low | Monitor | P3 | lab05_03_system_health_errors.txt | 119 | Operational issue observed. Monitor for recurrence and assess whether it affects updates, availability, collection or reporting reliability. | `Jun 21 16:58:54 vbox systemd[1]: Failed to start Refresh fwupd metadata and update motd.` |
| 51 | DNS or network issue | Low-Medium | Monitor | P3 | lab05_03_system_health_errors.txt | 120 | Operational issue observed. Monitor for recurrence and assess whether it affects updates, availability, collection or reporting reliability. | `Jun 21 17:37:33 vbox systemd-resolved[591]: Using degraded feature set UDP instead of UDP+EDNS0 for DNS server 192.168.1.1.` |
| 52 | Sudo incorrect password attempts | Low-Medium | Needs analyst attention | P2 | lab05_03_system_health_errors.txt | 135 | Event may affect security review or evidence collection. Analyst should confirm context, repetition, affected user/system and operational impact. | `Mar 13 11:09:53 vbox sudo[14786]:     vbox : 2 incorrect password attempts ; TTY=tty1 ; PWD=/home/vbox ; USER=root ; COMMAND=/usr/bin/apt install x11/.` |
| 53 | Sudo incorrect password attempts | Low-Medium | Needs analyst attention | P2 | lab05_03_system_health_errors.txt | 136 | Event may affect security review or evidence collection. Analyst should confirm context, repetition, affected user/system and operational impact. | `Mar 15 02:05:13 vbox sudo[26640]:     vbox : 3 incorrect password attempts ; TTY=tty1 ; PWD=/home/vbox ; USER=root ; COMMAND=/usr/sbin/dpkg-reconfigure keyboard-configuration` |
| 54 | Sudo incorrect password attempts | Low-Medium | Needs analyst attention | P2 | lab05_03_system_health_errors.txt | 137 | Event may affect security review or evidence collection. Analyst should confirm context, repetition, affected user/system and operational impact. | `Mar 15 02:05:39 vbox sudo[26641]:     vbox : 3 incorrect password attempts ; TTY=tty1 ; PWD=/home/vbox ; USER=root ; COMMAND=/usr/sbin/dpkg-reconfigure keyboard-configuration` |
| 55 | Failed service | Low | Monitor | P3 | lab05_03_system_health_errors.txt | 138 | Operational issue observed. Monitor for recurrence and assess whether it affects updates, availability, collection or reporting reliability. | `Apr 27 17:37:26 vbox systemd[1]: Failed to start Refresh fwupd metadata and update motd.` |
| 56 | Failed service | Low | Monitor | P3 | lab05_03_system_health_errors.txt | 139 | Operational issue observed. Monitor for recurrence and assess whether it affects updates, availability, collection or reporting reliability. | `May 11 12:08:06 vbox systemd[1]: Failed to start Refresh fwupd metadata and update motd.` |
| 57 | DNS or network issue | Low-Medium | Monitor | P3 | lab05_03_system_health_errors.txt | 149 | Operational issue observed. Monitor for recurrence and assess whether it affects updates, availability, collection or reporting reliability. | `May 18 20:29:38 vbox systemd-resolved[533]: Failed to save link data /run/systemd/resolve/netif/3: Permission denied` |
| 58 | DNS or network issue | Low-Medium | Monitor | P3 | lab05_03_system_health_errors.txt | 150 | Operational issue observed. Monitor for recurrence and assess whether it affects updates, availability, collection or reporting reliability. | `May 18 20:29:38 vbox systemd-resolved[533]: Failed to save link data /run/systemd/resolve/netif/3: Permission denied` |
| 59 | VirtualBox shared-folder success | Informational | Document | P4 | lab05_03_system_health_errors.txt | 222 | Expected or useful audit-trail activity. Keep as context, but do not escalate unless user, command, timing or frequency is unexpected. | `Jun 21 10:31:35 vbox kernel: 10:31:35.375183 automount vbsvcAutomounterMountIt: Successfully mounted 'Capturas' on '/mnt/capturas'` |
| 60 | DNS or network issue | Low-Medium | Monitor | P3 | lab05_03_system_health_errors.txt | 232 | Operational issue observed. Monitor for recurrence and assess whether it affects updates, availability, collection or reporting reliability. | `Jun 21 17:37:33 vbox systemd-resolved[591]: Using degraded feature set UDP instead of UDP+EDNS0 for DNS server 192.168.1.1.` |
| 61 | DNS or network issue | Low-Medium | Monitor | P3 | lab05_03_system_health_errors.txt | 252 | Operational issue observed. Monitor for recurrence and assess whether it affects updates, availability, collection or reporting reliability. | `Jun 20 13:57:04 vbox snapd[683]: stateengine.go:161: state ensure error: persistent network error: Post "https://api.snapcraft.io/v2/snaps/refresh": dial tcp: lookup api.snapcraft.io: Temporary failure in name resolution` |
| 62 | VirtualBox shared-folder failure | Low | No escalation | P4 | lab05_03_system_health_errors.txt | 256 | Lab infrastructure or virtualization-related finding. Treat as baseline/noise unless combined with instability or other suspicious evidence. | `Jun 21 10:19:49 vbox kernel: [21637.375095] vboxsf: SHFL_FN_MAP_FOLDER failed for 'Capturas': share not found` |
| 63 | VirtualBox shared-folder failure | Low | No escalation | P4 | lab05_03_system_health_errors.txt | 257 | Lab infrastructure or virtualization-related finding. Treat as baseline/noise unless combined with instability or other suspicious evidence. | `Jun 21 10:20:33 vbox kernel: [21682.143793] vboxsf: SHFL_FN_MAP_FOLDER failed for 'Capturas': share not found` |
| 64 | VirtualBox shared-folder failure | Low | No escalation | P4 | lab05_03_system_health_errors.txt | 258 | Lab infrastructure or virtualization-related finding. Treat as baseline/noise unless combined with instability or other suspicious evidence. | `Jun 21 10:21:47 vbox kernel: [21755.257302] vboxsf: SHFL_FN_MAP_FOLDER failed for 'Capturas': share not found` |
| 65 | VirtualBox shared-folder failure | Low | No escalation | P4 | lab05_03_system_health_errors.txt | 259 | Lab infrastructure or virtualization-related finding. Treat as baseline/noise unless combined with instability or other suspicious evidence. | `Jun 21 10:23:35 vbox kernel: [21864.033130] vboxsf: SHFL_FN_MAP_FOLDER failed for 'Capturas': share not found` |
| 66 | DNS or network issue | Low-Medium | Monitor | P3 | lab05_03_system_health_errors.txt | 272 | Operational issue observed. Monitor for recurrence and assess whether it affects updates, availability, collection or reporting reliability. | `Jun 21 10:32:06 vbox snapd[684]: stateengine.go:161: state ensure error: persistent network error: Get "https://api.snapcraft.io/api/v1/snaps/sections": dial tcp: lookup api.snapcraft.io: Temporary failure in name resolution` |
| 67 | DNS or network issue | Low-Medium | Monitor | P3 | lab05_03_system_health_errors.txt | 275 | Operational issue observed. Monitor for recurrence and assess whether it affects updates, availability, collection or reporting reliability. | `Jun 21 10:42:06 vbox snapd[684]: autorefresh.go:640: Cannot prepare auto-refresh change due to a permanent network error: persistent network error: Post "https://api.snapcraft.io/v2/snaps/refresh": dial tcp: lookup api.snapcraft.io: Tempora...` |
| 68 | DNS or network issue | Low-Medium | Monitor | P3 | lab05_03_system_health_errors.txt | 276 | Operational issue observed. Monitor for recurrence and assess whether it affects updates, availability, collection or reporting reliability. | `Jun 21 10:42:06 vbox snapd[684]: stateengine.go:161: state ensure error: persistent network error: Post "https://api.snapcraft.io/v2/snaps/refresh": dial tcp: lookup api.snapcraft.io: Temporary failure in name resolution` |
| 69 | VirtualBox shared-folder success | Informational | Document | P4 | lab05_03_system_health_errors.txt | 321 | Expected or useful audit-trail activity. Keep as context, but do not escalate unless user, command, timing or frequency is unexpected. | `[Sun Jun 21 16:41:19 2026] 10:31:35.375183 automount vbsvcAutomounterMountIt: Successfully mounted 'Capturas' on '/mnt/capturas'` |
| 70 | Storage capacity warning | Medium | Needs analyst attention | P2 | lab05_03_system_health_errors.txt | 342 | Event may affect security review or evidence collection. Analyst should confirm context, repetition, affected user/system and operational impact. | `Capturas        465G  396G   69G  86% /mnt/capturas` |

## Action guidance

- **Needs analyst attention**: review first; validate impact, repetition and context.
- **Review**: inspect user, origin, timing, frequency and expected activity.
- **Monitor**: watch recurrence and operational impact before escalating.
- **Document**: keep as audit trail or operational context.
- **No escalation**: treat as lab/environment noise unless correlated with other suspicious indicators.

## SOC interpretation

This classifier represents a basic SOC L1 triage layer. It helps translate technical events into initial operational actions, but it does not replace human analyst judgment or a production SIEM workflow.

A real production workflow would require correlation across time, users, source IPs, asset criticality, authentication sources, endpoint telemetry and business context.

## Limitations

- Static rules only; no behavioural baseline or adaptive scoring.
- No ticket creation, alert dispatching or incident response action.
- No enrichment with IP reputation, threat intelligence or asset inventory.
- Findings come from a controlled lab environment.
- Priorities are educational and conservative, not production SLA definitions.

## Conclusion

Mission 6.5 demonstrates how Python can support a SOC workflow by assigning initial analyst actions to extracted security and operational events. The output helps move from evidence extraction to triage decision support.

## Mission status

Mission 6.5 validated.
