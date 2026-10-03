---
atom_id: CA-E-370
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - logging-policy-materialization
  depends_on:
    continuant:
      - programmatic software
      - Logging Policy
version: 2
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-163
  derived_from:
    - CA-A-053
---
# Verify logging lifecycle materialization

## Claim checked

One production-relevant PROGRAMMATIC component materializes the active Logging
Policy's sink, retention, access, sampling, rotation, size, back-pressure,
unavailable-sink, and disk-pressure boundaries.

## Test case

Evaluate one production-relevant component whose logging materialization omits
its unavailable-sink behavior.

## Acceptance criteria

Pass only when deployment is rejected until the missing behavior is declared
without configuration, Implementation, or Delivery claiming policy authority.

## Failure disposition

Block the production logging path until its lifecycle materialization is
complete.

## Sources

- [CA-M-163 — Emit structured operational diagnostics](../05_method/CA-M-163-PROGRAMMATIC-CORE-METHOD--emit-structured-operational-diagnostics.md)
