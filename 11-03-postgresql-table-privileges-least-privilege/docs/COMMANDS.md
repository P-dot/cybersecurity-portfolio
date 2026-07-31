# Commands used

## Create tables and baseline
```bash
sudo -iu postgres psql \
  -v ON_ERROR_STOP=1 \
  -d bank_lab \
  -f scripts/create_tables.sql
```

## Grant least-privilege table permissions
```bash
sudo -iu postgres psql \
  -v ON_ERROR_STOP=1 \
  -d bank_lab \
  -f scripts/grant_permissions.sql
```

## Verify objects and privileges
```bash
sudo -iu postgres psql -d bank_lab -P pager=off -f scripts/verify_access.sql
```

## Real execution tests
```bash
# bank_app_rw can SELECT, INSERT, UPDATE but not DELETE
sudo -iu postgres psql -d bank_lab -P pager=off <<'SQL'
SET ROLE bank_app_rw;
SELECT * FROM bank_app.payment_requests ORDER BY request_id;
INSERT INTO bank_app.payment_requests (request_id, customer_id, amount, status)
VALUES (5003, 101, 99.90, 'PENDING')
ON CONFLICT (request_id) DO NOTHING;
UPDATE bank_app.payment_requests
SET status = 'APPROVED'
WHERE request_id = 5003;
DELETE FROM bank_app.payment_requests
WHERE request_id = 5003;
RESET ROLE;
SQL

# bank_analyst_ro can read but cannot insert
sudo -iu postgres psql -d bank_lab -P pager=off <<'SQL'
SET ROLE bank_analyst_ro;
SELECT * FROM bank_app.payment_requests ORDER BY request_id;
INSERT INTO bank_app.payment_requests (request_id, customer_id, amount, status)
VALUES (5004, 102, 80.00, 'PENDING');
RESET ROLE;
SQL

# bank_auditor_ro can read audit only
sudo -iu postgres psql -d bank_lab -P pager=off <<'SQL'
SET ROLE bank_auditor_ro;
SELECT * FROM bank_audit.access_events ORDER BY event_id;
SELECT * FROM bank_app.payment_requests;
RESET ROLE;
SQL

# operational roles cannot access bank_core
sudo -iu postgres psql -d bank_lab -P pager=off <<'SQL'
SET ROLE bank_app_rw;
SELECT * FROM bank_core.customer_accounts;
RESET ROLE;
SQL
```
