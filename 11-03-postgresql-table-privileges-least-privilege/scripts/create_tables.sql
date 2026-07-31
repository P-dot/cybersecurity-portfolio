BEGIN;
SET ROLE bank_owner;

CREATE TABLE IF NOT EXISTS bank_core.customer_accounts (
    customer_id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    iban_masked TEXT NOT NULL,
    balance NUMERIC(12,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS bank_app.payment_requests (
    request_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    amount NUMERIC(12,2) NOT NULL CHECK (amount > 0),
    status TEXT NOT NULL CHECK (status IN ('PENDING', 'APPROVED', 'REJECTED'))
);

CREATE TABLE IF NOT EXISTS bank_audit.access_events (
    event_id INTEGER PRIMARY KEY,
    event_time TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    actor TEXT NOT NULL,
    action TEXT NOT NULL
);

INSERT INTO bank_core.customer_accounts (customer_id, full_name, iban_masked, balance)
VALUES
    (101, 'Cliente Demo Uno', 'ES**0001', 4250.00),
    (102, 'Cliente Demo Dos', 'ES**0002', 1875.50)
ON CONFLICT (customer_id) DO NOTHING;

INSERT INTO bank_app.payment_requests (request_id, customer_id, amount, status)
VALUES
    (5001, 101, 150.00, 'PENDING'),
    (5002, 102, 275.50, 'APPROVED')
ON CONFLICT (request_id) DO NOTHING;

INSERT INTO bank_audit.access_events (event_id, actor, action)
VALUES
    (9001, 'lab_admin', 'INITIAL SECURITY BASELINE'),
    (9002, 'bank_owner', 'LAB TABLES CREATED')
ON CONFLICT (event_id) DO NOTHING;

RESET ROLE;

REVOKE ALL ON TABLE
    bank_core.customer_accounts,
    bank_app.payment_requests,
    bank_audit.access_events
FROM PUBLIC;

REVOKE ALL ON TABLE
    bank_core.customer_accounts,
    bank_app.payment_requests,
    bank_audit.access_events
FROM bank_app_rw,
     bank_analyst_ro,
     bank_auditor_ro,
     bank_misconfigured_lab;

COMMIT;
