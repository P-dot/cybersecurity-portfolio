\set ON_ERROR_STOP on

-- Remove global object-creation rights from the shared public schema.
REVOKE CREATE ON SCHEMA public FROM PUBLIC;

-- Create three isolated security zones owned by the technical owner role.
CREATE SCHEMA IF NOT EXISTS bank_core AUTHORIZATION bank_owner;
CREATE SCHEMA IF NOT EXISTS bank_app AUTHORIZATION bank_owner;
CREATE SCHEMA IF NOT EXISTS bank_audit AUTHORIZATION bank_owner;

-- Enforce the expected owner even when the schemas already exist.
ALTER SCHEMA bank_core OWNER TO bank_owner;
ALTER SCHEMA bank_app OWNER TO bank_owner;
ALTER SCHEMA bank_audit OWNER TO bank_owner;

-- Start from a closed baseline and remove inherited or previous grants.
REVOKE ALL ON SCHEMA bank_core, bank_app, bank_audit FROM PUBLIC;
REVOKE ALL ON SCHEMA bank_core, bank_app, bank_audit
FROM bank_app_rw,
     bank_analyst_ro,
     bank_auditor_ro,
     bank_misconfigured_lab;

-- CONNECT permits entry to the database, not access to schemas or tables.
GRANT CONNECT ON DATABASE bank_lab
TO bank_owner,
   bank_app_rw,
   bank_analyst_ro,
   bank_auditor_ro,
   bank_misconfigured_lab;

-- Application and analyst roles can reference objects only in bank_app.
GRANT USAGE ON SCHEMA bank_app
TO bank_app_rw,
   bank_analyst_ro;

-- The auditor can reference objects only in bank_audit.
GRANT USAGE ON SCHEMA bank_audit
TO bank_auditor_ro;
