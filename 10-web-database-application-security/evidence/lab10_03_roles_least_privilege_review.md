# LAB 10.3 — Roles, Privileges and Least Privilege Review

Collection time: 2026-06-30 15:01:02
Scope: Local controlled SQLite training database
Execution mode: local Python + SQLite
Safety: no external targets, no network activity, no third-party systems, no real credentials

## 1. Objective

This mission reviews the role and permission model of the controlled training application database.

The review focuses on least privilege, account lifecycle, separation of duties and auditability.

## 2. Account baseline

- Total accounts reviewed: 3
- Active accounts: 2
- Disabled accounts: 1

| Username | Role | Status | Created at |
|---|---|---|---|
| admin.training | admin | Active | 2026-06-30 14:47:56 |
| analyst.training | analyst | Active | 2026-06-30 14:47:56 |
| disabled.training | viewer | Disabled | 2026-06-30 14:47:56 |

## 3. Role-permission model

| Role | Permission | Risk level | Business justification |
|---|---|---|---|
| admin | app_config:read | Low | Administrative role for controlled lab management |
| admin | app_config:write | High | Administrative role for controlled lab management |
| admin | audit_log:read | Low | Administrative role for controlled lab management |
| admin | audit_log:write | Low | Administrative role for controlled lab management |
| admin | backup:execute | High | Administrative role for controlled lab management |
| admin | users:read | Low | Administrative role for controlled lab management |
| admin | users:write | High | Administrative role for controlled lab management |
| analyst | app_config:read | Low | Security analyst role for reading evidence and writing audit notes |
| analyst | audit_log:read | Low | Security analyst role for reading evidence and writing audit notes |
| analyst | audit_log:write | Low | Security analyst role for reading evidence and writing audit notes |
| analyst | users:read | Low | Security analyst role for reading evidence and writing audit notes |
| viewer | app_config:read | Low | Read-only role for limited review |
| viewer | audit_log:read | Low | Read-only role for limited review |

## 4. High-impact permissions

| Role | Permission | Reason for review |
|---|---|---|
| admin | app_config:write | High-impact permission requiring periodic review |
| admin | backup:execute | High-impact permission requiring periodic review |
| admin | users:write | High-impact permission requiring periodic review |

## 5. Least privilege findings

| Finding ID | Role | Permission | Severity | Observation | Recommended action |
|---|---|---|---|---|---|
| LP-01 | admin | users:write / app_config:write / backup:execute | Medium | Active administrative account detected: admin.training. Admin rights are expected but high-impact. | Keep admin account justified, monitored and reviewed periodically. |
| LP-02 | viewer | N/A | Informational | Disabled account detected: disabled.training. This supports account lifecycle control. | Keep disabled account disabled unless there is a documented business need. |
| LP-03 | analyst | N/A | Informational | Analyst role does not have administrative write or backup permissions in this model. | Maintain separation between analyst and administrator permissions. |
| LP-04 | viewer | N/A | Informational | Viewer role remains limited to audit/config read access in this model. | Maintain read-only viewer role design. |

## 6. Security-relevant configuration after review

| Key | Value | Security relevance |
|---|---|---|
| audit_logging | enabled | Authentication and security-relevant events should be logged |
| auth_query_mode | parameterized_required | Authentication queries should use parameterized statements |
| backup_status | created_during_lab | Database backup should exist and be restorable |
| db_engine | sqlite | Database engine used for controlled local lab |
| least_privilege_review | reviewed_in_lab10_3 | Roles and privileges require analyst review |

## 7. Analyst interpretation

- The role model separates administrator, analyst and viewer responsibilities.
- Administrative write and backup permissions are high-impact and should be periodically reviewed.
- The analyst role can read evidence and write audit notes but does not receive administrative write permissions.
- The viewer role remains limited and read-only in this model.
- Disabled accounts are visible in the review and should remain disabled unless justified.
- The review was logged in the local audit table.

## 8. Risk classification

| Area | Risk | Severity | Treatment |
|---|---|---|---|
| Administrative privileges | Admin role has high-impact rights | Medium | Keep justified, logged and periodically reviewed |
| Analyst role | No excessive administrative write permission detected | Informational | Maintain separation of duties |
| Viewer role | Read-only model maintained | Informational | Keep limited scope |
| Disabled account | Account lifecycle control visible | Informational | Keep disabled unless reactivation is documented |
| Permission model | Explicit role-permission mapping exists | Informational | Maintain as part of application security documentation |

## 9. Status

Lab 10.3 completed. Next step: audit, backup validation and remediation summary in Lab 10.4.