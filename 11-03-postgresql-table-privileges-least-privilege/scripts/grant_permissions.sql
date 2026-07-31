BEGIN;

GRANT SELECT, INSERT, UPDATE
ON TABLE bank_app.payment_requests
TO bank_app_rw;

GRANT SELECT
ON TABLE bank_app.payment_requests
TO bank_analyst_ro;

GRANT SELECT
ON TABLE bank_audit.access_events
TO bank_auditor_ro;

REVOKE ALL
ON TABLE bank_core.customer_accounts
FROM bank_app_rw,
     bank_analyst_ro,
     bank_auditor_ro,
     bank_misconfigured_lab;

REVOKE ALL
ON TABLE bank_app.payment_requests,
         bank_audit.access_events
FROM bank_misconfigured_lab;

COMMIT;
