## Mission 5.1 — Linux log source inventory

### Objective

Identify the main Linux log sources available on the Ubuntu/vbox lab machine before performing SOC-style event review.

### Evidence collected

The following information was collected:

- Hostname and operating system information.
- Kernel version.
- Network interfaces and current IP address.
- Inventory of `/var/log`.
- Journal boot history.
- `systemd-journald` service status.
- Authentication log availability.
- System log availability.

### Results

The target system was identified as `vbox`, running Ubuntu 22.04.5 LTS on VirtualBox.

The main network interface was `enp0s3`, with IP address `192.168.1.135/24`.

The `/var/log` directory contains relevant log files, including:

- `auth.log`
- `syslog`
- `kern.log`
- `dmesg`
- `lastlog`
- `wtmp`
- `btmp`
- service and package-related logs

The `systemd-journald` service was active and running.

The command `journalctl --list-boots` showed several recorded system boots, including the current boot session.

The file `/var/log/auth.log` exists and contains authentication-related events, including sudo activity and session opening/closing records.

The file `/var/log/syslog` exists and contains general system events, including network interface activity, DHCP assignment, systemd service activity and kernel messages.

### Initial SOC interpretation

The Ubuntu/vbox machine provides sufficient local log sources for basic SOC-style review.

The most relevant sources for the next missions are:

- `/var/log/auth.log` for authentication, sudo and privilege-related activity.
- `/var/log/syslog` for general system and service events.
- `journalctl` for systemd journal review.
- `journalctl --list-boots` for correlating events with system boot sessions.
- `systemctl status` for service-level status and operational context.

No suspicious activity is concluded at this stage. This mission only establishes available log sources and confirms that the system is ready for deeper log review.

### Evidence

- `lab05_01_log_sources.txt`
- `lab05_00_extructura_creada.PNG`

### Status

Mission 5.1 validated.
## Mission 5.2 — Authentication, sessions and sudo review

### Objective

Review authentication-related activity on the Ubuntu/vbox lab machine, focusing on user sessions, sudo activity, authentication failures and SSH-related events.

### Evidence collected

The following sources were reviewed:

- Recent login sessions with `last`.
- Last login information with `lastlog`.
- Current logged users with `who`.
- Authentication records in `/var/log/auth.log`.
- Sudo events from `/var/log/auth.log`.
- Authentication failure patterns.
- Sudo-related events from `journalctl`.
- SSH service status and SSH-related log entries.

### Initial SOC interpretation

This mission focuses on identifying who accessed the system, when the access occurred, whether privilege elevation was used, and whether authentication failures are present.

From a SOC/SecOps perspective, these logs are useful to distinguish expected administrative activity from potentially suspicious behaviour such as repeated failed logins, unexpected sudo usage, direct root access attempts, unknown users, or SSH-related anomalies.

### Evidence

- `lab05_02_auth_sudo_sessions.txt`

### Status

Mission 5.2 completed pending review.

## Mission 5.3 — System warnings, errors and failed services

### Objective

Review Linux system health signals from a SOC/SecOps perspective by inspecting failed services, recent warnings, recent errors, kernel messages and general system context.

### Evidence collected

The following checks were performed:

- Failed systemd services with `systemctl --failed`.
- Failed service units with `systemctl list-units --type=service --state=failed`.
- Recent warning-level events from `journalctl`.
- Recent error-level events from `journalctl`.
- Warning and alert events from the current boot.
- Error, warning, failure and timeout keywords from `/var/log/syslog`.
- Kernel warnings and errors through `dmesg`.
- Disk and memory context.

### SOC interpretation approach

The goal of this mission is not to assume that every error is a security incident. The objective is to classify observations into three categories:

- Expected activity: normal system behavior or known lab activity.
- Technical issue: configuration, service, boot, network or resource issue.
- Security-relevant event: authentication abuse, repeated failures, suspicious service behavior, unexpected denial, unusual process or unexplained anomaly.

### Evidence

- `lab05_03_system_health_errors.txt`

### Status

Mission 5.3 validated.

## Mission 5.4 — Mini SOC triage

### Objective

Classify the most relevant events collected during Missions 5.2 and 5.3 using a basic SOC triage structure.

### Evidence reviewed

The following evidence files were reviewed:

- `lab05_02_auth_sudo_sessions.txt`
- `lab05_03_system_health_errors.txt`
- `lab05_04_mini_triage_soc.md`

### Triage criteria

Each event was classified using the following fields:

- Event observed
- Log source
- Status
- Classification
- Severity
- SOC interpretation
- Recommended action

### Results

The triage classified the main findings as authentication events, expected system activity, technical issues, resolved VirtualBox configuration issues, virtualized environment warnings and operational monitoring points.

The reviewed events included:

- failed local login for an unknown user;
- sudo authentication failure;
- root cron session activity;
- SSH authentication activity check;
- `fwupd-refresh.service` failure;
- DNS or external update resolution failures;
- VirtualBox shared-folder mount failure;
- successful VirtualBox shared-folder mount;
- kernel and virtualization warnings;
- host shared folder storage usage.

### SOC interpretation

No clear evidence of compromise was identified.

The failed authentication events were local and consistent with lab activity. The service and DNS-related issues were classified as technical issues. The VirtualBox shared-folder errors were classified as a resolved operational issue. Kernel and virtualization warnings were interpreted as expected in a virtualized lab environment unless correlated with instability or suspicious activity.

### Conclusion

Mission 5.4 demonstrates basic SOC triage: collecting logs is not enough; each event must be classified by source, context, severity and recommended action.

### Evidence

- `lab05_04_mini_triage_soc.md`

### Status

Mission 5.4 validated.

## Mission 5.5 — Final professional closure

### Objective

Close Lab 05 with a professional SOC-style summary, evidence index, demonstrated competencies, limitations and final conclusion.

### Executive summary

This lab reviewed local Linux log sources on an Ubuntu virtual machine from a SOC Level 1 perspective.

The review covered:

- Linux log source inventory.
- Authentication events.
- Local login sessions.
- Sudo activity and privilege elevation traces.
- Failed authentication events.
- Failed systemd services.
- System warnings and errors.
- Kernel and VirtualBox-related messages.
- DNS and update-related issues.
- Disk and memory context.
- Mini SOC triage of relevant findings.

The main outcome was a mini SOC triage table that classified relevant events by source, status, severity, interpretation and recommended action.

No clear evidence of compromise was identified. The observed events were mainly expected lab activity, local authentication mistakes, technical network/DNS issues, VirtualBox shared-folder configuration issues, firmware/update service failure and virtualized environment warnings.

### Evidence reviewed

The following evidence files were produced during the lab:

- `lab05_01_log_sources.txt`
- `lab05_02_auth_sudo_sessions.txt`
- `lab05_03_system_health_errors.txt`
- `lab05_04_mini_triage_soc.md`
- `lab05_05_final_closure_summary.md`

### Demonstrated competencies

This lab demonstrates the following operational cybersecurity competencies:

- Linux log source identification.
- Review of authentication, sudo and session activity.
- Use of `/var/log/auth.log`, `/var/log/syslog`, `journalctl`, `systemctl`, `dmesg`, `df` and `free`.
- Basic failed-service and system-health review.
- Differentiation between expected activity, technical issues and potentially security-relevant events.
- Evidence handling through a controlled shared-folder export path.
- SOC-style triage table creation with severity, interpretation and recommended action.

### Limitations

This lab was performed in a local virtualized environment.

It does not represent a full enterprise SOC environment and does not include:

- Centralized SIEM ingestion.
- EDR telemetry.
- Production alert rules.
- Real enterprise identity sources.
- Full incident response workflow.

The analysis is therefore limited to local Linux logs and lab-generated activity.

### Final SOC conclusion

Lab 05 demonstrates basic Linux monitoring and SOC triage capability.

The system was reviewed using local log sources, authentication records, sudo traces, systemd journal entries and system-health indicators. The resulting findings were classified with operational context, severity and recommended actions.

The lab shows the ability to move from raw logs to structured analysis, which is a core skill for SOC L1 and security operations roles.

### Portfolio wording

Built a Linux log monitoring and mini SOC triage lab, reviewing authentication, sudo, failed services, system warnings and infrastructure events, then classifying findings by source, severity, operational context and recommended action.

### Status

Mission 5.5 validated.
