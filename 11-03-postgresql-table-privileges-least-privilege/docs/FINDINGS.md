# Findings

1. **Object ownership**: the three lab tables belong to `bank_owner`, not to the administrative `postgres` user.
2. **Layered access control**: `CONNECT` to the database and `USAGE` on a schema do not imply `SELECT` on a table.
3. **Role separation**:
   - `bank_app_rw`: `SELECT`, `INSERT`, `UPDATE` on `bank_app.payment_requests`; `DELETE` denied.
   - `bank_analyst_ro`: `SELECT` only on `bank_app.payment_requests`.
   - `bank_auditor_ro`: `SELECT` only on `bank_audit.access_events`.
   - `bank_misconfigured_lab`: no effective access.
   - `bank_owner`: full technical ownership.
4. **Sensitive data isolation**: no operational role can traverse `bank_core` or read `bank_core.customer_accounts`.
5. **Real execution validation**: every permission set was validated with allowed and denied operations, not just by catalog inspection.
