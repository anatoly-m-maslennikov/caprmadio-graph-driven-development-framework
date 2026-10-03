---
atom_id: CA-E-269
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - diagnostic-failure
  depends_on:
    continuant:
      - programmatic software
      - Logging Policy
version: 4
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-163
  derived_from:
    - CA-A-053
---
# Observe one diagnostic emission failure

## Claim checked

One failure to emit a PROGRAMMATIC operational diagnostic is observable and
does not silently break the primary work.

## Applicable conditions

Apply when a component has a declared operational-diagnostic path and a
separate primary work outcome.

## Test case

Cause one declared diagnostic emission to fail while the associated primary
work remains otherwise executable.

## Acceptance criteria

Pass only when the primary work reaches its declared outcome or failure
boundary, and the diagnostic-emission failure is itself observable through its
declared recovery or reporting path.

## Failure disposition

Reject the diagnostic path when it hides its own failure or silently changes
the primary work result.

## Sources

- [CA-M-163 — Emit structured operational diagnostics](../05_method/CA-M-163-PROGRAMMATIC-CORE-METHOD--emit-structured-operational-diagnostics.md)
