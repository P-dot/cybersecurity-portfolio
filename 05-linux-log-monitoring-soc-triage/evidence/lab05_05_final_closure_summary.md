# Lab 05 - Mission 5.5 - Final professional closure

Date: Mon Jun 22 07:53:48 AM UTC 2026

## Objective

Close Lab 05 with a professional SOC-style summary, evidence index, demonstrated competencies, limitations and final conclusion.

## Evidence inventory

| Evidence file | Status |
|---|---|
| lab05_01_log_sources.txt | Found |
| lab05_02_auth_sudo_sessions.txt | Found |
| lab05_03_system_health_errors.txt | Found |
| lab05_04_mini_triage_soc.md | Found |

## Executive summary

This lab reviewed local Linux log sources on an Ubuntu virtual machine from a SOC Level 1 perspective. The review covered log source inventory, authentication and sudo activity, local sessions, failed services, system warnings, kernel messages, DNS/update-related errors, VirtualBox shared-folder events and basic disk and memory context.

The main outcome was a mini SOC triage table that classified relevant events by source, status, severity, interpretation and recommended action. No clear evidence of compromise was identified. The observed events were mainly expected lab activity, local authentication mistakes, technical network/DNS issues, VirtualBox shared-folder configuration issues, firmware/update service failure and virtualized environment warnings.

## Demonstrated competencies

- Linux log source identification.
- Review of authentication, sudo and session activity.
- Use of auth.log, syslog, journalctl, systemctl, dmesg, df and free.
- Basic failed-service and system-health review.
- Differentiation between expected activity, technical issues and potentially security-relevant events.
- Evidence handling through a controlled shared-folder export path.
- SOC-style triage table creation with severity and recommended action.

## Limitations

This lab was performed in a local virtualized environment. It does not represent a full enterprise SOC environment, does not include centralized SIEM ingestion, EDR telemetry, production alert rules or real incident response workflows. The analysis is therefore limited to local Linux logs and lab-generated activity.

## Final SOC conclusion

Lab 05 demonstrates basic Linux monitoring and SOC triage capability. The system was reviewed using local log sources, authentication records, sudo traces, systemd journal entries and system-health indicators. The resulting findings were classified with operational context, severity and recommended actions. The lab shows the ability to move from raw logs to structured analysis, which is a core skill for SOC L1 and security operations roles.

## Mission status

Mission 5.5 validated.
