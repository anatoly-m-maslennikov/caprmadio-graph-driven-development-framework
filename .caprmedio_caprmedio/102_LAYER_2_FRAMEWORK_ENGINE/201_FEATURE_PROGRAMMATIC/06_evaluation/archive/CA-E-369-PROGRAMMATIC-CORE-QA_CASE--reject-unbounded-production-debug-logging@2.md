---
atom_id: CA-E-369
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - production-debug
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
# Reject unbounded production DEBUG logging

## Claim checked

Production DEBUG logging is disabled by default and may be enabled only through
a bounded selector with automatic expiry and unchanged redaction.

## Test case

Evaluate one production component configuration that enables DEBUG globally
without an expiry.

## Acceptance criteria

Pass only when the configuration is rejected before deployment.

## Failure disposition

Block production DEBUG until component, subject, run, entity, or equivalent
scope and automatic expiry are present.

## Sources

- [CA-M-163 — Emit structured operational diagnostics](../05_method/CA-M-163-PROGRAMMATIC-CORE-METHOD--emit-structured-operational-diagnostics.md)
