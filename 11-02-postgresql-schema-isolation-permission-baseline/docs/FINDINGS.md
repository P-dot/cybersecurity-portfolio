# Findings — Lab 11.2

## F-01 — Shared schema creation permission removed

`CREATE` was revoked from `PUBLIC` on the default `public` schema. This reduces the risk of arbitrary object creation in a shared namespace.

## F-02 — Security zones isolated by schema

The database was divided into three logical zones:

- `bank_core`: internal and sensitive objects.
- `bank_app`: objects exposed to the application and analysts.
- `bank_audit`: audit evidence and review objects.

All three schemas are owned by `bank_owner`.

## F-03 — Role access follows least privilege

- `bank_app_rw` and `bank_analyst_ro` have `USAGE` only on `bank_app`.
- `bank_auditor_ro` has `USAGE` only on `bank_audit`.
- `bank_misconfigured_lab` can connect but has no schema access.
- `bank_owner` retains owner-level access to all three schemas.

## F-04 — CONNECT and USAGE are separate controls

The matrix proves that permission to connect to `bank_lab` does not imply permission to reference every schema.

```text
CONNECT != USAGE
```

Table-level privileges have not yet been granted. The next stage will demonstrate:

```text
USAGE != SELECT
```

## Troubleshooting note

An initial validation query used `bank-core` instead of `bank_core`, so the schema was omitted from that result. Re-running the query with the correct underscore returned all four schemas. This was a query typo, not a missing schema.
