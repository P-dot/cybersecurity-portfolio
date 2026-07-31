-- Ownership
SELECT schemaname AS esquema,
       tablename  AS tabla,
       tableowner AS propietario
FROM pg_tables
WHERE schemaname IN ('bank_core','bank_app','bank_audit')
ORDER BY schemaname, tablename;

-- Usage vs select
SELECT rolname AS rol,
       has_schema_privilege(rolname, 'bank_app', 'USAGE') AS usage_app,
       has_table_privilege(rolname, 'bank_app.payment_requests', 'SELECT') AS select_app,
       has_schema_privilege(rolname, 'bank_audit', 'USAGE') AS usage_audit,
       has_table_privilege(rolname, 'bank_audit.access_events', 'SELECT') AS select_audit
FROM pg_roles
WHERE rolname IN ('bank_owner','bank_app_rw','bank_analyst_ro','bank_auditor_ro','bank_misconfigured_lab')
ORDER BY rolname;

-- Final least privilege matrix
SELECT rolname AS rol,
       has_table_privilege(rolname, 'bank_app.payment_requests', 'SELECT') AS app_select,
       has_table_privilege(rolname, 'bank_app.payment_requests', 'INSERT') AS app_insert,
       has_table_privilege(rolname, 'bank_app.payment_requests', 'UPDATE') AS app_update,
       has_table_privilege(rolname, 'bank_app.payment_requests', 'DELETE') AS app_delete,
       has_table_privilege(rolname, 'bank_audit.access_events', 'SELECT') AS audit_select,
       has_table_privilege(rolname, 'bank_core.customer_accounts', 'SELECT') AS core_select
FROM pg_roles
WHERE rolname IN ('bank_owner','bank_app_rw','bank_analyst_ro','bank_auditor_ro','bank_misconfigured_lab')
ORDER BY rolname;
