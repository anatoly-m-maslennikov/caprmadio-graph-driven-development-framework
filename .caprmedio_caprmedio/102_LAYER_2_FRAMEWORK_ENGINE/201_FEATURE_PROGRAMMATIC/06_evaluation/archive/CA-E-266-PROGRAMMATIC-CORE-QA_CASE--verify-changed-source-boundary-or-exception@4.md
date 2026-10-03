---
atom_id: CA-E-266
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - source-boundary
  depends_on:
    continuant:
      - programmatic software
version: 4
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-162
  derived_from:
    - CA-A-053
---
# Verify changed source boundary or exception

## Claim checked

One changed hand-authored PROGRAMMATIC Python executable unit above 40 logical
lines has one specific bounded exception that preserves a single
responsibility.

## Applicable conditions

Apply to a new or materially changed hand-authored Python file. Generated
Runtime and Delivery outputs are not applicable.

## Test case

Evaluate one changed executable unit exceeding 40 logical lines without a
documented exception.

## Acceptance criteria

Pass only when the unit is rejected until it is split, reduced, or supplied
with one exception recording its measured size, reason, bounded scope, single
responsibility, and condition for reconsideration.

## Failure disposition

Block the changed source from claiming source-boundary conformance.

## Sources

- [CA-M-162 — Ratchet hand-authored Python source boundaries](../05_method/CA-M-162-PROGRAMMATIC-CORE-METHOD--ratchet-hand-authored-python-source-boundaries.md)
