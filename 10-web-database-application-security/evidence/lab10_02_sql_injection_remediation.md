# LAB 10.2 — Controlled SQL Injection Demonstration and Parameterized Remediation

Collection time: 2026-06-30 14:54:42
Scope: Local controlled SQLite training database
Execution mode: local Python + SQLite
Safety: no external targets, no network activity, no third-party systems, no real credentials

## 1. Objective

This mission demonstrates how SQL injection can affect a poorly implemented authentication query and how parameterized queries remediate the issue.

The test is performed only against the local toy SQLite database created in Lab 10.1.

## 2. Test cases

| Test case | Vulnerable result count | Safe result count | Analyst interpretation |
|---|---:|---:|---|
| Valid login | 1 | 1 | Expected success in both implementations |
| Wrong password | 0 | 0 | Expected failure in both implementations |
| Controlled SQL injection input | 1 | 0 | Vulnerable pattern is bypassable; parameterized query blocks the input |

## 3. Vulnerable pattern observed

The vulnerable function builds SQL by concatenating user-controlled input into the query string.

Example vulnerable query shape:

```sql
SELECT id, username, role, is_active FROM users WHERE username = 'analyst.training' OR '1'='1' AND password_hash = '<HASHED_PASSWORD_VALUE>' AND is_active = 1
```

Analyst note: this pattern is unsafe because input is interpreted as part of the SQL statement.

## 4. Remediated pattern

The safe function uses a parameterized query. User input is passed as data, not concatenated into the SQL syntax.

Safe query template:

```sql
SELECT id, username, role, is_active FROM users WHERE username = ? AND password_hash = ? AND is_active = 1
```

Parameters are provided separately by the database driver.

## 5. Security outcome

| Control | Result |
|---|---|
| Vulnerable authentication bypass demonstrated in controlled lab | True |
| Parameterized query blocked controlled injection input | True |
| Real credentials used | False |
| External systems touched | False |
| Network activity performed | False |

## 6. Risk classification

| Finding | Likelihood | Impact | Severity | Recommended action |
|---|---|---|---|---|
| Authentication query vulnerable to SQL injection when string concatenation is used | High in affected code path | High | High | Replace concatenated SQL with parameterized queries |
| Parameterized query implementation resists the controlled injection input | Low residual risk | Positive control | Informational | Maintain parameterized query pattern and code review |

## 7. Remediation guidance

- Never concatenate user input into SQL statements.
- Use parameterized queries or prepared statements.
- Hash passwords before comparison and never store plaintext passwords.
- Log authentication and security-relevant events.
- Review roles and apply least privilege.
- Add application security tests for authentication flows.

## 8. Evidence handling

- The evidence uses toy users and toy password material only.
- No real credentials are included.
- No hostname, IP address or external target is included.
- The test is fully local and controlled.

## 9. Status

Lab 10.2 completed. Next step: roles, privileges and least privilege review in Lab 10.3.