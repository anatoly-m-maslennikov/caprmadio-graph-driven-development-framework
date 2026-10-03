---
atom_id: CA-E-363
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - source-file-size
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
# Reject an oversized changed Python file

## Claim checked

One new or materially changed hand-authored PROGRAMMATIC Python file remains at
or below 200 physical lines or has a specific bounded exception.

## Test case

Evaluate one changed 201-line hand-authored Python file with no file-size
exception.

## Acceptance criteria

Pass only when conformance is rejected until the file is reduced, split by
responsibility, or supplied with one accepted bounded exception.

## Failure disposition

Block the changed file from claiming source-boundary conformance.

## Sources

- [CA-M-162 — Ratchet hand-authored Python source boundaries](../05_method/CA-M-162-PROGRAMMATIC-CORE-METHOD--ratchet-hand-authored-python-source-boundaries.md)
