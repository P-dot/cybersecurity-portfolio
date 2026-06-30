# LAB 10.4 — Audit, Backup Validation and Remediation Summary

Collection time: 2026-06-30 15:05:39
Scope: Local controlled SQLite training database
Execution mode: local Python + SQLite
Safety: no external targets, no network activity, no third-party systems, no real credentials

## 1. Objective

This mission validates security audit visibility, verifies that the local database backup is readable, and consolidates the remediation plan for Lab 10.

## 2. Audit visibility

- Audit events in live database: 7

| Event type | Outcome | Count |
|---|---|---:|
| AUDIT_BACKUP_REMEDIATION_REVIEW | INFO | 1 |
| AUTH_ATTEMPT | FAILURE | 1 |
| AUTH_ATTEMPT | SUCCESS | 1 |
| CONFIG_REVIEW | INFO | 1 |
| LEAST_PRIVILEGE_REVIEW | INFO | 1 |
| SQLI_CONTROLLED_TEST | INFO | 1 |
| SQLI_REMEDIATION_TEST | INFO | 1 |

## 3. Recent audit events

| Event time | Event type | Username | Outcome | Source context | Analyst note |
|---|---|---|---|---|---|
| 2026-06-30 15:05:39 | AUDIT_BACKUP_REMEDIATION_REVIEW | training_input | INFO | local_lab | Audit visibility, backup readability and remediation summary generated |
| 2026-06-30 15:01:02 | LEAST_PRIVILEGE_REVIEW | training_input | INFO | local_lab | Role and permission model reviewed in controlled local database |
| 2026-06-30 14:54:42 | SQLI_REMEDIATION_TEST | training_input | INFO | local_lab | Parameterized query remediation validated against controlled injection input |
| 2026-06-30 14:54:42 | SQLI_CONTROLLED_TEST | training_input | INFO | local_lab | Controlled SQL injection test executed against local toy database only |
| 2026-06-30 14:47:56 | CONFIG_REVIEW | N/A | INFO | local_lab | Initial application/database security baseline created |
| 2026-06-30 14:47:56 | AUTH_ATTEMPT | unknown.training | FAILURE | local_lab | Failed login used for baseline evidence |
| 2026-06-30 14:47:56 | AUTH_ATTEMPT | analyst.training | SUCCESS | local_lab | Expected successful login in controlled lab |

## 4. Backup validation

- Live database: `C:\Carrera_Ciberseguridad\05_Capturas\10_Web_Database_Application_Security\lab10_training_app.db`
- Backup database: `C:\Carrera_Ciberseguridad\05_Capturas\10_Web_Database_Application_Security\lab10_training_app_backup.db`
- Backup readable: True
- Backup has required tables: True
- Users count match: True
- App configuration count match: True

| Table | Live count | Backup count | Interpretation |
|---|---:|---:|---|
| users | 3 | 3 | Counts match |
| audit_log | 7 | 3 | Expected difference possible because audit events continued after backup creation |
| app_config | 5 | 5 | Counts match |

## 5. File integrity references

| File | SHA256 |
|---|---|
| Live database | `99329cd5539f6b0c3d2cd1c4f42ce51fc40773db07c8b26bd8cc6e76f0592767` |
| Backup database | `b69d07dacacb95451ee5c813dd80e9b4085fcfa906bc9404a763293b5519f21d` |

## 6. Remediation summary

| Finding | Severity | Remediation | Status |
|---|---|---|---|
| SQL query built with string concatenation can be bypassed | High | Replace with parameterized queries/prepared statements | Validated in Lab 10.2 |
| Authentication events need auditability | Medium | Maintain audit log for successful, failed and security-relevant events | Validated in Lab 10.1/10.4 |
| Administrative privileges are high-impact | Medium | Keep admin rights justified, monitored and periodically reviewed | Reviewed in Lab 10.3 |
| Roles require least-privilege separation | Medium | Separate admin, analyst and viewer permissions | Reviewed in Lab 10.3 |
| Backup must be readable and identifiable | Medium | Keep backup copy and integrity reference | Validated in Lab 10.4 |
| Disabled accounts require lifecycle control | Low | Keep disabled unless documented business need exists | Reviewed in Lab 10.3 |

## 7. Security controls demonstrated

- Controlled application/database security baseline.
- Vulnerability demonstration in a local authorized lab.
- Remediation through parameterized queries.
- Role and permission review.
- Least privilege interpretation.
- Account lifecycle awareness.
- Audit logging review.
- Backup readability and file integrity references.

## 8. Analyst conclusion

The controlled lab shows the full defensive cycle: baseline, vulnerable pattern identification, remediation, role review, audit review and backup validation.

The evidence is suitable for a professional cybersecurity portfolio because it documents scope, safety boundaries, technical findings, risk classification and remediation actions.

## 9. Status

Lab 10.4 completed. Next step: final Lab 10 README and portfolio publication package in Lab 10.5.