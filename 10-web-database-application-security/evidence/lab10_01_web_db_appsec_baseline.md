# LAB 10.1 — Web, Database & Application Security Baseline

Collection time: 2026-06-30 14:47:56
Scope: Local controlled toy application database
Execution mode: local Python + SQLite
Safety: no external targets, no exploitation against third-party systems, no real credentials

## 1. Database files

- Database created: `C:\Carrera_Ciberseguridad\05_Capturas\10_Web_Database_Application_Security\lab10_training_app.db`
- Backup created: `C:\Carrera_Ciberseguridad\05_Capturas\10_Web_Database_Application_Security\lab10_training_app_backup.db`

## 2. Schema inventory

- Table detected: `app_config`
- Table detected: `audit_log`
- Table detected: `sqlite_sequence`
- Table detected: `users`

## 3. User and role baseline

- Total users: 3
- Active users: 2
- Disabled users: 1

| Role | Count |
|---|---:|
| admin | 1 |
| analyst | 1 |
| viewer | 1 |

## 4. Audit logging baseline

- Audit events detected: 3

| Event type | Outcome | Count |
|---|---|---:|
| AUTH_ATTEMPT | FAILURE | 1 |
| AUTH_ATTEMPT | SUCCESS | 1 |
| CONFIG_REVIEW | INFO | 1 |

## 5. Security-relevant configuration

| Key | Value | Security relevance |
|---|---|---|
| audit_logging | enabled | Authentication and security-relevant events should be logged |
| auth_query_mode | parameterized_required | Authentication queries should use parameterized statements |
| backup_status | created_during_lab | Database backup should exist and be restorable |
| db_engine | sqlite | Database engine used for controlled local lab |
| least_privilege_review | pending | Roles and privileges require analyst review |

## 6. Initial analyst interpretation

- Authentication-related tables exist in a controlled lab database.
- Passwords are stored as hashes for this toy lab; no real credentials are used.
- Audit logging exists and contains baseline authentication/security events.
- A disabled account is present to demonstrate account lifecycle review.
- A database backup copy was created to demonstrate basic backup awareness.
- The configuration table explicitly requires parameterized authentication queries.

## 7. Initial risk notes

| Area | Observation | Initial action |
|---|---|---|
| Authentication | Login flow requires parameterized queries | Validate in Lab 10.2 |
| Account lifecycle | Disabled account exists | Document as expected control |
| Auditability | Audit table exists | Use for failed/successful login evidence |
| Backup | Backup copy created | Verify restore logic in future work |
| Least privilege | Roles exist but need review | Review role separation in Lab 10.3 |

## 8. Status

Lab 10.1 completed. Next step: controlled SQL injection demonstration and parameterized-query remediation in Lab 10.2.