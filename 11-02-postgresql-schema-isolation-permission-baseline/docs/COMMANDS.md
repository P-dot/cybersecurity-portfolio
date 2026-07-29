# Commands — Lab 11.2

## Prerequisites

The following objects must already exist:

- Database: `bank_lab`
- Roles: `bank_owner`, `bank_app_rw`, `bank_analyst_ro`, `bank_auditor_ro`, `bank_misconfigured_lab`

## Apply the baseline

From Ubuntu:

```bash
sudo -iu postgres psql -d bank_lab -f scripts/apply_baseline.sql
```

## Verify the result

```bash
sudo -iu postgres psql -d bank_lab -f scripts/verify_baseline.sql
```

## Expected schema ownership

```text
bank_app   | bank_owner
bank_audit | bank_owner
bank_core  | bank_owner
public     | postgres
```

## Expected access matrix

| Role | CONNECT | bank_core | bank_app | bank_audit |
|---|---:|---:|---:|---:|
| `bank_analyst_ro` | true | false | true | false |
| `bank_app_rw` | true | false | true | false |
| `bank_auditor_ro` | true | false | false | true |
| `bank_misconfigured_lab` | true | false | false | false |
| `bank_owner` | true | true | true | true |

## Operational note

In `psql`, a prompt such as `bank_lab-#`, `bank_lab'>` or `bank_lab(#` means the SQL statement is incomplete. Cancel the current buffer with `Ctrl+C` or reset it with `\r`.
