---
atom_id: CA-E-365
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - cyclomatic-complexity
  depends_on:
    continuant:
      - programmatic software
version: 2
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-162
    - CA-M-164
  derived_from:
    - CA-A-053
---
# Reject unchecked cyclomatic complexity

## Claim checked

Every new or materially changed executable unit has a result from the admitted
cyclomatic-complexity lint and stays within its Method-owned maximum or one
accepted bounded exception.

## Test case

Evaluate one materially changed function for which no current complexity-lint
result exists.

## Acceptance criteria

Pass only when conformance is rejected until the admitted lint reports a value
and that value passes the Method-owned maximum or its accepted exception.

## Failure disposition

Block the changed unit from claiming source-boundary conformance.

## Sources

- [CA-M-162 — Ratchet hand-authored Python source boundaries](../05_method/CA-M-162-PROGRAMMATIC-CORE-METHOD--ratchet-hand-authored-python-source-boundaries.md)
- [CA-M-164 — Ratchet typing and automation adoption](../05_method/CA-M-164-PROGRAMMATIC-CORE-METHOD--ratchet-typing-and-automation-adoption.md)
