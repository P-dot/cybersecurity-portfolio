\set ON_ERROR_STOP on
\pset pager off

-- Verify that all security-zone schemas exist and have the correct owner.
SELECT
    nspname AS schema_name,
    pg_get_userbyid(nspowner) AS owner
FROM pg_namespace
WHERE nspname IN (
    'public',
    'bank_core',
    'bank_app',
    'bank_audit'
)
ORDER BY nspname;

-- Verify CONNECT and schema USAGE independently for every lab role.
SELECT
    rolname AS role_name,
    has_database_privilege(
        rolname,
        'bank_lab',
        'CONNECT'
    ) AS can_connect,
    has_schema_privilege(
        rolname,
        'bank_core',
        'USAGE'
    ) AS core_usage,
    has_schema_privilege(
        rolname,
        'bank_app',
        'USAGE'
    ) AS app_usage,
    has_schema_privilege(
        rolname,
        'bank_audit',
        'USAGE'
    ) AS audit_usage
FROM pg_roles
WHERE rolname IN (
    'bank_owner',
    'bank_app_rw',
    'bank_analyst_ro',
    'bank_auditor_ro',
    'bank_misconfigured_lab'
)
ORDER BY rolname;
