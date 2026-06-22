# Lab 05 - Mission 5.4 - Mini SOC triage

Date: Mon Jun 22 07:23:28 AM UTC 2026

## Objective

Classify the most relevant authentication, sudo, system health, service and infrastructure events observed during Missions 5.2 and 5.3.

## Evidence files reviewed

- Found: /home/vbox/lab05/evidencias/lab05_02_auth_sudo_sessions.txt
- Found: /home/vbox/lab05/evidencias/lab05_03_system_health_errors.txt

## Mini triage table

| ID | Event observed | Source | Status | Classification | Severity | SOC interpretation | Recommended action |
|---|---|---|---|---|---|---|---|
| 1 | Failed local login for unknown user | auth.log / login | Observed | Authentication failure | Low | A failed login for an unknown user was observed locally. In this lab context it is likely caused by manual input error, but in production it would require correlation if repeated. Sample: Jun 21 10:31:49 vbox login[702]: FAILED LOGIN (1) on '/dev/tty1' FOR 'UNKNOWN', Authentication failure | Document and monitor for repetition, remote origin or multiple affected users. |
| 2 | Sudo authentication failure | auth.log / sudo | Observed | Privilege/authentication event | Low | A sudo authentication failure indicates an incorrect password or failed privilege elevation attempt. In this lab context it is expected during manual work. Sample: Jun 21 10:59:45 vbox sudo: pam_unix(sudo:auth): authentication failure; logname=vbox uid=1000 euid=0 tty=/dev/tty1 ruser=vbox rhost=  user=vbox | Monitor if repeated, especially if associated with unexpected users or commands. |
| 3 | Root cron session activity | auth.log / CRON | Observed | Scheduled system activity | Informational | Cron sessions for root usually represent scheduled system tasks. Sample: Jun 19 10:17:02 vbox CRON[1315]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0) | No escalation. Keep as baseline system activity unless unusual frequency or command context appears. |
| 4 | SSH authentication activity | auth.log / SSH | Not observed | Remote access check | Informational | No clear SSH authentication activity is expected in this local Ubuntu lab unless SSH is enabled. Sample: N/A | If observed unexpectedly, review source IP, account, result and service exposure. |
| 5 | fwupd-refresh.service failed | systemctl / journalctl | Observed | Technical issue | Low | fwupd metadata refresh failed. This is interpreted as a maintenance/update issue, not an indicator of compromise. Sample: ● fwupd-refresh.service loaded failed failed Refresh fwupd metadata and update motd | Review update/network conditions when convenient. Do not escalate as security incident by itself. |
| 6 | DNS or external update resolution failures | syslog / journalctl | Observed | Network/DNS technical issue | Low-Medium | The system showed DNS or external update resolution failures. This is consistent with lab networking, NAT or DNS configuration issues. Sample: Jun 18 15:43:25 vbox systemd-resolved[606]: Using degraded feature set TCP instead of UDP for DNS server 192.168.1.1. | Check DNS, gateway and internet path if updates are required. Correlate with network changes. |
| 7 | VirtualBox shared folder mount failure | kernel / vboxsf | Observed | Resolved technical issue | Low | The shared folder Capturas failed to mount before being correctly configured. Sample: Jun 21 10:19:49 vbox kernel: vboxsf: SHFL_FN_MAP_FOLDER failed for 'Capturas': share not found | No security escalation. Document as resolved operational issue. |
| 8 | VirtualBox shared folder mounted successfully | kernel / vboxsf | Observed | Positive validation | Informational | The shared folder was successfully mounted after configuration. Sample: Jun 21 10:31:35 vbox kernel: 10:31:35.375183 automount vbsvcAutomounterMountIt: Successfully mounted 'Capturas' on '/mnt/capturas' | Keep using /mnt/capturas as controlled evidence export path. |
| 9 | Kernel and virtualization warnings | journalctl / dmesg | Observed | Virtualized environment warning | Low | Kernel and VirtualBox-related warnings are common in lab VMs and do not indicate compromise by themselves. Sample: Jun 21 10:31:19 vbox kernel: RETBleed: WARNING: Spectre v2 mitigation leaves CPU vulnerable to RETBleed attacks, data leaks possible! | Keep as environmental baseline. Escalate only if combined with instability or suspicious activity. |
| 10 | Host shared folder storage usage high | df -h | Observed | Operational monitoring | Medium | The Windows shared folder used for evidence export showed high disk usage. Sample: Capturas        465G  396G   69G  86% /mnt/capturas | Monitor free space and clean old evidence/ZIPs to avoid future collection failures. |

## Overall assessment

The reviewed events do not provide clear evidence of compromise. Most findings are classified as expected lab activity, local authentication mistakes, technical network/DNS issues, VirtualBox shared-folder configuration issues, or virtualized environment warnings.

## Mission status

Mission 5.4 validated.
