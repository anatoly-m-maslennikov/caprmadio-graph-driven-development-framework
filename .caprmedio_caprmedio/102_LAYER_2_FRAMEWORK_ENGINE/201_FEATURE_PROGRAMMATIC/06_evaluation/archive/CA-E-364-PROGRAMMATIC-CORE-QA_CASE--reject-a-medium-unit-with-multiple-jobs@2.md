---
atom_id: CA-E-364
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - executable-unit-size
  depends_on:
    continuant:
      - programmatic software
version: 2
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-162
  derived_from:
    - CA-A-053
---
# Reject a medium unit with multiple jobs

## Claim checked

One changed executable unit between 26 and 40 logical lines performs exactly
one coherent job.

## Test case

Evaluate one 30-line changed function whose accurate name and branches reveal
two independently reusable responsibilities.

## Acceptance criteria

Pass only when the unit is rejected until the two responsibilities are split.

## Failure disposition

Block the unit from claiming the 26-to-40-line allowance.

## Sources

- [CA-M-162 — Ratchet hand-authored Python source boundaries](../05_method/CA-M-162-PROGRAMMATIC-CORE-METHOD--ratchet-hand-authored-python-source-boundaries.md)
