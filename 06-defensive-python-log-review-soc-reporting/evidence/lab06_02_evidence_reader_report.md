# Lab 06.2 — Defensive evidence reader report

Date: 2026-06-22 09:51:25 UTC

## Objective

Read Lab 05 evidence files with Python and generate a defensive summary including file presence, size, line count, keyword matches and sample lines.

## Evidence inventory

| File | Exists | Size | Lines |
|---|---|---:|---:|
| lab05_02_auth_sudo_sessions.txt | yes | 27.5 KB | 316 |
| lab05_03_system_health_errors.txt | yes | 37.7 KB | 352 |
| lab05_04_mini_triage_soc.md | yes | 4.9 KB | 35 |
| lab05_05_final_closure_summary.md | yes | 2.5 KB | 44 |

## Keyword summary

### lab05_02_auth_sudo_sessions.txt

| Keyword group | Matching lines |
|---|---:|
| sudo_activity | 198 |
| authentication_failures | 12 |
| ssh_activity | 3 |
| service_failures | 0 |
| dns_or_network_issues | 0 |
| virtualbox_or_lab_infrastructure | 29 |
| warnings_errors_timeouts | 12 |

### lab05_03_system_health_errors.txt

| Keyword group | Matching lines |
|---|---:|
| sudo_activity | 3 |
| authentication_failures | 3 |
| ssh_activity | 0 |
| service_failures | 28 |
| dns_or_network_issues | 24 |
| virtualbox_or_lab_infrastructure | 45 |
| warnings_errors_timeouts | 119 |

### lab05_04_mini_triage_soc.md

| Keyword group | Matching lines |
|---|---:|
| sudo_activity | 3 |
| authentication_failures | 2 |
| ssh_activity | 1 |
| service_failures | 1 |
| dns_or_network_issues | 2 |
| virtualbox_or_lab_infrastructure | 5 |
| warnings_errors_timeouts | 9 |

### lab05_05_final_closure_summary.md

| Keyword group | Matching lines |
|---|---:|
| sudo_activity | 4 |
| authentication_failures | 0 |
| ssh_activity | 0 |
| service_failures | 0 |
| dns_or_network_issues | 2 |
| virtualbox_or_lab_infrastructure | 2 |
| warnings_errors_timeouts | 4 |

## Sample matching lines

### lab05_02_auth_sudo_sessions.txt

#### sudo_activity

- Line 2: `LAB 05 - MISSION 5.2 - AUTHENTICATION, SESSIONS AND SUDO`
- Line 21: `uid=1000(vbox) gid=1000(vbox) groups=1000(vbox),27(sudo),999(vboxsf)`
- Line 91: `Jun 21 09:39:37 vbox sudo:     vbox : TTY=tty1 ; PWD=/home/vbox/lab05 ; USER=root ; COMMAND=/usr/bin/journalctl --list-boots`
- Line 92: `Jun 21 09:39:37 vbox sudo: pam_unix(sudo:session): session opened for user root(uid=0) by vbox(uid=1000)`
- Line 93: `Jun 21 09:39:37 vbox sudo: pam_unix(sudo:session): session closed for user root`

#### authentication_failures

- Line 149: `Jun 21 10:31:46 vbox login[702]: pam_unix(login:auth): authentication failure; logname=LOGIN uid=0 euid=0 tty=/dev/tty1 ruser= rhost=`
- Line 150: `Jun 21 10:31:49 vbox login[702]: FAILED LOGIN (1) on '/dev/tty1' FOR 'UNKNOWN', Authentication failure`
- Line 154: `Jun 21 10:59:45 vbox sudo: pam_unix(sudo:auth): authentication failure; logname=vbox uid=1000 euid=0 tty=/dev/tty1 ruser=vbox rhost=  user=vbox`
- Line 210: `Jun 21 10:59:45 vbox sudo: pam_unix(sudo:auth): authentication failure; logname=vbox uid=1000 euid=0 tty=/dev/tty1 ruser=vbox rhost=  user=vbox`
- Line 217: `### Authentication failures from auth.log`

#### ssh_activity

- Line 309: `### SSH service status`
- Line 311: `### SSH authentication events, if any`
- Line 312: `Jun 21 11:00:01 vbox sudo:     vbox : TTY=tty1 ; PWD=/home/vbox/lab05 ; USER=root ; COMMAND=/usr/bin/grep -Ei sshd|ssh /var/log/auth.log`

#### service_failures

No sample lines found.

#### dns_or_network_issues

No sample lines found.

#### virtualbox_or_lab_infrastructure

- Line 18: `Hardware Model: VirtualBox`
- Line 21: `uid=1000(vbox) gid=1000(vbox) groups=1000(vbox),27(sudo),999(vboxsf)`
- Line 109: `Jun 21 10:10:55 vbox sudo:     vbox : TTY=tty1 ; PWD=/home/vbox/lab05 ; USER=root ; COMMAND=/usr/bin/cp /home/vbox/lab05/evidencias/lab05_01_log_sources.txt /mnt/capturas/`
- Line 114: `Jun 21 10:18:47 vbox sudo:     vbox : TTY=tty1 ; PWD=/home/vbox/lab05 ; USER=root ; COMMAND=/usr/bin/mkdir -p /mnt/capturas`
- Line 117: `Jun 21 10:19:49 vbox sudo:     vbox : TTY=tty1 ; PWD=/home/vbox/lab05 ; USER=root ; COMMAND=/usr/bin/mount -t vboxsf Capturas /mnt/capturas`

#### warnings_errors_timeouts

- Line 149: `Jun 21 10:31:46 vbox login[702]: pam_unix(login:auth): authentication failure; logname=LOGIN uid=0 euid=0 tty=/dev/tty1 ruser= rhost=`
- Line 150: `Jun 21 10:31:49 vbox login[702]: FAILED LOGIN (1) on '/dev/tty1' FOR 'UNKNOWN', Authentication failure`
- Line 154: `Jun 21 10:59:45 vbox sudo: pam_unix(sudo:auth): authentication failure; logname=vbox uid=1000 euid=0 tty=/dev/tty1 ruser=vbox rhost=  user=vbox`
- Line 210: `Jun 21 10:59:45 vbox sudo: pam_unix(sudo:auth): authentication failure; logname=vbox uid=1000 euid=0 tty=/dev/tty1 ruser=vbox rhost=  user=vbox`
- Line 217: `### Authentication failures from auth.log`

### lab05_03_system_health_errors.txt

#### sudo_activity

- Line 135: `Mar 13 11:09:53 vbox sudo[14786]:     vbox : 2 incorrect password attempts ; TTY=tty1 ; PWD=/home/vbox ; USER=root ; COMMAND=/usr/bin/apt install x11/.`
- Line 136: `Mar 15 02:05:13 vbox sudo[26640]:     vbox : 3 incorrect password attempts ; TTY=tty1 ; PWD=/home/vbox ; USER=root ; COMMAND=/usr/sbin/dpkg-reconfigure keyboard-configuration`
- Line 137: `Mar 15 02:05:39 vbox sudo[26641]:     vbox : 3 incorrect password attempts ; TTY=tty1 ; PWD=/home/vbox ; USER=root ; COMMAND=/usr/sbin/dpkg-reconfigure keyboard-configuration`

#### authentication_failures

- Line 135: `Mar 13 11:09:53 vbox sudo[14786]:     vbox : 2 incorrect password attempts ; TTY=tty1 ; PWD=/home/vbox ; USER=root ; COMMAND=/usr/bin/apt install x11/.`
- Line 136: `Mar 15 02:05:13 vbox sudo[26640]:     vbox : 3 incorrect password attempts ; TTY=tty1 ; PWD=/home/vbox ; USER=root ; COMMAND=/usr/sbin/dpkg-reconfigure keyboard-configuration`
- Line 137: `Mar 15 02:05:39 vbox sudo[26641]:     vbox : 3 incorrect password attempts ; TTY=tty1 ; PWD=/home/vbox ; USER=root ; COMMAND=/usr/sbin/dpkg-reconfigure keyboard-configuration`

#### ssh_activity

No sample lines found.

#### service_failures

- Line 26: `● fwupd-refresh.service loaded failed failed Refresh fwupd metadata and update motd`
- Line 35: `● fwupd-refresh.service loaded failed failed Refresh fwupd metadata and update motd`
- Line 51: `Jun 19 10:20:38 vbox systemd[1]: fwupd-refresh.service: Failed with result 'exit-code'.`
- Line 52: `Jun 19 10:20:38 vbox systemd[1]: Failed to start Refresh fwupd metadata and update motd.`
- Line 59: `Jun 20 14:52:42 vbox systemd[1]: fwupd-refresh.service: Failed with result 'exit-code'.`

#### dns_or_network_issues

- Line 43: `Jun 18 15:43:25 vbox systemd-resolved[606]: Using degraded feature set TCP instead of UDP for DNS server 192.168.1.1.`
- Line 44: `Jun 18 16:13:50 vbox systemd-resolved[606]: Using degraded feature set UDP instead of UDP+EDNS0 for DNS server 192.168.1.1.`
- Line 120: `Jun 21 17:37:33 vbox systemd-resolved[591]: Using degraded feature set UDP instead of UDP+EDNS0 for DNS server 192.168.1.1.`
- Line 149: `May 18 20:29:38 vbox systemd-resolved[533]: Failed to save link data /run/systemd/resolve/netif/3: Permission denied`
- Line 150: `May 18 20:29:38 vbox systemd-resolved[533]: Failed to save link data /run/systemd/resolve/netif/3: Permission denied`

#### virtualbox_or_lab_infrastructure

- Line 18: `Hardware Model: VirtualBox`
- Line 67: `Jun 21 10:19:49 vbox kernel: vboxsf: g_fHostFeatures=0x8000000f g_fSfFeatures=0x1 g_uSfLastFunction=29`
- Line 68: `Jun 21 10:19:49 vbox kernel: vboxsf: Successfully loaded version 7.1.10 r169112 on 5.15.0-177-generic (LINUX_VERSION_CODE=0x50fc7)`
- Line 69: `Jun 21 10:19:49 vbox kernel: vboxsf: SHFL_FN_MAP_FOLDER failed for 'Capturas': share not found`
- Line 70: `Jun 21 10:20:33 vbox kernel: vboxsf: SHFL_FN_MAP_FOLDER failed for 'Capturas': share not found`

#### warnings_errors_timeouts

- Line 2: `LAB 05 - MISSION 5.3 - SYSTEM ERRORS, WARNINGS AND FAILED SERVICES`
- Line 24: `### Failed systemd services`
- Line 26: `● fwupd-refresh.service loaded failed failed Refresh fwupd metadata and update motd`
- Line 33: `### Failed service units only`
- Line 35: `● fwupd-refresh.service loaded failed failed Refresh fwupd metadata and update motd`

### lab05_04_mini_triage_soc.md

#### sudo_activity

- Line 7: `Classify the most relevant authentication, sudo, system health, service and infrastructure events observed during Missions 5.2 and 5.3.`
- Line 11: `- Found: /home/vbox/lab05/evidencias/lab05_02_auth_sudo_sessions.txt`
- Line 19: `| 2 | Sudo authentication failure | auth.log / sudo | Observed | Privilege/authentication event | Low | A sudo authentication failure indicates an incorrect password or failed privilege elevation attempt. In this lab context it is expected during manual work. Sample: Jun 21 10:59:45 vbox sudo: pam_unix(sudo:auth): authentication failure; logname=vbox uid=1000 euid=0 tty=/dev/tty1 ruser=vbox rhost=  user=vbox | Monitor if repeated, especially if associated with unexpected users or commands. |`

#### authentication_failures

- Line 18: `| 1 | Failed local login for unknown user | auth.log / login | Observed | Authentication failure | Low | A failed login for an unknown user was observed locally. In this lab context it is likely caused by manual input error, but in production it would require correlation if repeated. Sample: Jun 21 10:31:49 vbox login[702]: FAILED LOGIN (1) on '/dev/tty1' FOR 'UNKNOWN', Authentication failure | Document and monitor for repetition, remote origin or multiple affected users. |`
- Line 19: `| 2 | Sudo authentication failure | auth.log / sudo | Observed | Privilege/authentication event | Low | A sudo authentication failure indicates an incorrect password or failed privilege elevation attempt. In this lab context it is expected during manual work. Sample: Jun 21 10:59:45 vbox sudo: pam_unix(sudo:auth): authentication failure; logname=vbox uid=1000 euid=0 tty=/dev/tty1 ruser=vbox rhost=  user=vbox | Monitor if repeated, especially if associated with unexpected users or commands. |`

#### ssh_activity

- Line 21: `| 4 | SSH authentication activity | auth.log / SSH | Not observed | Remote access check | Informational | No clear SSH authentication activity is expected in this local Ubuntu lab unless SSH is enabled. Sample: N/A | If observed unexpectedly, review source IP, account, result and service exposure. |`

#### service_failures

- Line 22: `| 5 | fwupd-refresh.service failed | systemctl / journalctl | Observed | Technical issue | Low | fwupd metadata refresh failed. This is interpreted as a maintenance/update issue, not an indicator of compromise. Sample: ● fwupd-refresh.service loaded failed failed Refresh fwupd metadata and update motd | Review update/network conditions when convenient. Do not escalate as security incident by itself. |`

#### dns_or_network_issues

- Line 23: `| 6 | DNS or external update resolution failures | syslog / journalctl | Observed | Network/DNS technical issue | Low-Medium | The system showed DNS or external update resolution failures. This is consistent with lab networking, NAT or DNS configuration issues. Sample: Jun 18 15:43:25 vbox systemd-resolved[606]: Using degraded feature set TCP instead of UDP for DNS server 192.168.1.1. | Check DNS, gateway and internet path if updates are required. Correlate with network changes. |`
- Line 31: `The reviewed events do not provide clear evidence of compromise. Most findings are classified as expected lab activity, local authentication mistakes, technical network/DNS issues, VirtualBox shared-folder configuration issues, or virtualized environment warnings.`

#### virtualbox_or_lab_infrastructure

- Line 24: `| 7 | VirtualBox shared folder mount failure | kernel / vboxsf | Observed | Resolved technical issue | Low | The shared folder Capturas failed to mount before being correctly configured. Sample: Jun 21 10:19:49 vbox kernel: vboxsf: SHFL_FN_MAP_FOLDER failed for 'Capturas': share not found | No security escalation. Document as resolved operational issue. |`
- Line 25: `| 8 | VirtualBox shared folder mounted successfully | kernel / vboxsf | Observed | Positive validation | Informational | The shared folder was successfully mounted after configuration. Sample: Jun 21 10:31:35 vbox kernel: 10:31:35.375183 automount vbsvcAutomounterMountIt: Successfully mounted 'Capturas' on '/mnt/capturas' | Keep using /mnt/capturas as controlled evidence export path. |`
- Line 26: `| 9 | Kernel and virtualization warnings | journalctl / dmesg | Observed | Virtualized environment warning | Low | Kernel and VirtualBox-related warnings are common in lab VMs and do not indicate compromise by themselves. Sample: Jun 21 10:31:19 vbox kernel: RETBleed: WARNING: Spectre v2 mitigation leaves CPU vulnerable to RETBleed attacks, data leaks possible! | Keep as environmental baseline. Escalate only if combined with instability or suspicious activity. |`
- Line 27: `| 10 | Host shared folder storage usage high | df -h | Observed | Operational monitoring | Medium | The Windows shared folder used for evidence export showed high disk usage. Sample: Capturas        465G  396G   69G  86% /mnt/capturas | Monitor free space and clean old evidence/ZIPs to avoid future collection failures. |`
- Line 31: `The reviewed events do not provide clear evidence of compromise. Most findings are classified as expected lab activity, local authentication mistakes, technical network/DNS issues, VirtualBox shared-folder configuration issues, or virtualized environment warnings.`

#### warnings_errors_timeouts

- Line 12: `- Found: /home/vbox/lab05/evidencias/lab05_03_system_health_errors.txt`
- Line 18: `| 1 | Failed local login for unknown user | auth.log / login | Observed | Authentication failure | Low | A failed login for an unknown user was observed locally. In this lab context it is likely caused by manual input error, but in production it would require correlation if repeated. Sample: Jun 21 10:31:49 vbox login[702]: FAILED LOGIN (1) on '/dev/tty1' FOR 'UNKNOWN', Authentication failure | Document and monitor for repetition, remote origin or multiple affected users. |`
- Line 19: `| 2 | Sudo authentication failure | auth.log / sudo | Observed | Privilege/authentication event | Low | A sudo authentication failure indicates an incorrect password or failed privilege elevation attempt. In this lab context it is expected during manual work. Sample: Jun 21 10:59:45 vbox sudo: pam_unix(sudo:auth): authentication failure; logname=vbox uid=1000 euid=0 tty=/dev/tty1 ruser=vbox rhost=  user=vbox | Monitor if repeated, especially if associated with unexpected users or commands. |`
- Line 22: `| 5 | fwupd-refresh.service failed | systemctl / journalctl | Observed | Technical issue | Low | fwupd metadata refresh failed. This is interpreted as a maintenance/update issue, not an indicator of compromise. Sample: ● fwupd-refresh.service loaded failed failed Refresh fwupd metadata and update motd | Review update/network conditions when convenient. Do not escalate as security incident by itself. |`
- Line 23: `| 6 | DNS or external update resolution failures | syslog / journalctl | Observed | Network/DNS technical issue | Low-Medium | The system showed DNS or external update resolution failures. This is consistent with lab networking, NAT or DNS configuration issues. Sample: Jun 18 15:43:25 vbox systemd-resolved[606]: Using degraded feature set TCP instead of UDP for DNS server 192.168.1.1. | Check DNS, gateway and internet path if updates are required. Correlate with network changes. |`

### lab05_05_final_closure_summary.md

#### sudo_activity

- Line 14: `| lab05_02_auth_sudo_sessions.txt | Found |`
- Line 20: `This lab reviewed local Linux log sources on an Ubuntu virtual machine from a SOC Level 1 perspective. The review covered log source inventory, authentication and sudo activity, local sessions, failed services, system warnings, kernel messages, DNS/update-related errors, VirtualBox shared-folder events and basic disk and memory context.`
- Line 27: `- Review of authentication, sudo and session activity.`
- Line 40: `Lab 05 demonstrates basic Linux monitoring and SOC triage capability. The system was reviewed using local log sources, authentication records, sudo traces, systemd journal entries and system-health indicators. The resulting findings were classified with operational context, severity and recommended actions. The lab shows the ability to move from raw logs to structured analysis, which is a core skill for SOC L1 and security operations roles.`

#### authentication_failures

No sample lines found.

#### ssh_activity

No sample lines found.

#### service_failures

No sample lines found.

#### dns_or_network_issues

- Line 20: `This lab reviewed local Linux log sources on an Ubuntu virtual machine from a SOC Level 1 perspective. The review covered log source inventory, authentication and sudo activity, local sessions, failed services, system warnings, kernel messages, DNS/update-related errors, VirtualBox shared-folder events and basic disk and memory context.`
- Line 22: `The main outcome was a mini SOC triage table that classified relevant events by source, status, severity, interpretation and recommended action. No clear evidence of compromise was identified. The observed events were mainly expected lab activity, local authentication mistakes, technical network/DNS issues, VirtualBox shared-folder configuration issues, firmware/update service failure and virtualized environment warnings.`

#### virtualbox_or_lab_infrastructure

- Line 20: `This lab reviewed local Linux log sources on an Ubuntu virtual machine from a SOC Level 1 perspective. The review covered log source inventory, authentication and sudo activity, local sessions, failed services, system warnings, kernel messages, DNS/update-related errors, VirtualBox shared-folder events and basic disk and memory context.`
- Line 22: `The main outcome was a mini SOC triage table that classified relevant events by source, status, severity, interpretation and recommended action. No clear evidence of compromise was identified. The observed events were mainly expected lab activity, local authentication mistakes, technical network/DNS issues, VirtualBox shared-folder configuration issues, firmware/update service failure and virtualized environment warnings.`

#### warnings_errors_timeouts

- Line 15: `| lab05_03_system_health_errors.txt | Found |`
- Line 20: `This lab reviewed local Linux log sources on an Ubuntu virtual machine from a SOC Level 1 perspective. The review covered log source inventory, authentication and sudo activity, local sessions, failed services, system warnings, kernel messages, DNS/update-related errors, VirtualBox shared-folder events and basic disk and memory context.`
- Line 22: `The main outcome was a mini SOC triage table that classified relevant events by source, status, severity, interpretation and recommended action. No clear evidence of compromise was identified. The observed events were mainly expected lab activity, local authentication mistakes, technical network/DNS issues, VirtualBox shared-folder configuration issues, firmware/update service failure and virtualized environment warnings.`
- Line 29: `- Basic failed-service and system-health review.`

## SOC interpretation

This script does not determine whether an incident occurred. It prepares evidence for analyst review by identifying relevant patterns and summarising where they appear.

Keyword matches must be interpreted with context. For example, a single local authentication failure may be a manual mistake, while repeated remote failures could require further investigation.

## Mission status

Mission 6.2 completed pending review.
