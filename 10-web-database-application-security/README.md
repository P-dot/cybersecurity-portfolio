# Lab 10 — Web, Database & Application Security

## Overview

This lab documents a controlled Web, Database and Application Security workflow using a local SQLite training database.

The purpose is to demonstrate defensive application/database security fundamentals: baseline creation, SQL injection risk identification, parameterized-query remediation, role and privilege review, auditability, backup validation and remediation reporting.

## Scope and safety

- Local controlled lab only.
- No external targets.
- No third-party systems.
- No real credentials.
- No network activity.
- Toy SQLite database created only for training and documentation.

## Lab missions

| Mission | Description | Evidence |
|---|---|---|
| 10.1 — Web/DB/AppSec Baseline | Created a local SQLite training database with users, roles, configuration and audit logging | `evidence/lab10_01_web_db_appsec_baseline.md` |
| 10.2 — SQL Injection Remediation | Demonstrated a controlled SQL injection issue against vulnerable string concatenation and remediated it with parameterized queries | `evidence/lab10_02_sql_injection_remediation.md` |
| 10.3 — Roles and Least Privilege | Reviewed users, roles, permissions, high-impact privileges, account lifecycle and separation of duties | `evidence/lab10_03_roles_least_privilege_review.md` |
| 10.4 — Audit and Backup | Reviewed audit events, validated backup readability, documented integrity references and consolidated remediation actions | `evidence/lab10_04_audit_backup_remediation.md` |
| 10.5 — Final Closure | Consolidated the final portfolio package and professional CV wording | `evidence/lab10_05_final_closure_summary.md` |

## Key findings and remediation

| Area | Finding | Severity | Remediation / Control |
|---|---|---|---|
| Application security | SQL query built with string concatenation can be bypassed in the controlled lab | High | Use parameterized queries / prepared statements |
| Authentication | Authentication events need audit visibility | Medium | Maintain audit logging for success, failure and security-relevant events |
| Identity and access | Administrative privileges are high-impact | Medium | Keep admin rights justified, monitored and periodically reviewed |
| Least privilege | Roles require separation of responsibilities | Medium | Separate administrator, analyst and viewer permissions |
| Backup | Backup must be readable and identifiable | Medium | Validate backup readability and record integrity references |
| Account lifecycle | Disabled accounts should remain controlled | Low | Keep disabled unless a documented business need exists |

## Skills demonstrated

- Application security fundamentals.
- Database security baseline review.
- SQL injection risk understanding in a controlled environment.
- Parameterized-query remediation.
- Role and permission modelling.
- Least privilege review.
- Audit log analysis.
- Backup validation.
- Risk classification and remediation reporting.
- Professional evidence handling and safety boundaries.

## Tools and technologies

- Python
- SQLite
- Markdown reporting
- SHA256 integrity references
- Local Windows lab environment

## Professional relevance

This lab supports junior technical cybersecurity, Security Operations, SecOps, infrastructure security and vulnerability management profiles by showing a complete defensive cycle: baseline, finding, remediation, access review, audit review, backup validation and closure.

It also extends the portfolio beyond systems and network monitoring by adding application and database security evidence.

## Evidence files

- `evidence/lab10_01_web_db_appsec_baseline.md`
- `evidence/lab10_02_sql_injection_remediation.md`
- `evidence/lab10_03_roles_least_privilege_review.md`
- `evidence/lab10_04_audit_backup_remediation.md`
- `evidence/lab10_05_final_closure_summary.md`
