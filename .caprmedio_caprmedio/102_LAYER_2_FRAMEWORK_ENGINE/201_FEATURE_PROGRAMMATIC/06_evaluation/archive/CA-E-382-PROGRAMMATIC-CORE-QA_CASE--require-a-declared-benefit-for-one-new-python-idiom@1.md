---
atom_id: CA-E-382
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - python-idiom-adoption
  depends_on:
    continuant:
      - programmatic software
version: 1
updated_at: 2026-09-01 02:10:00 +0400
relations:
  evaluation_for:
    - CA-M-228
  derived_from:
    - CA-A-053
---
# Require a declared benefit for one new Python idiom

## Claim checked

A runtime-dependent Python idiom is admitted only for a named benefit inside
the supported boundary.

## Test case

Replace an immediate trusted f-string with a t-string while providing no
interpolation processor or other correctness, clarity, safety, or measured
performance benefit.

## Acceptance criteria

Pass only when the change is rejected and the simpler supported idiom remains.

## Failure disposition

Reject novelty alone as a benefit and return the selection to CA-M-228.

## Sources

- [PEP 750 — Template Strings](https://peps.python.org/pep-0750/)
- [CA-M-228 — Adopt current Python idioms only for declared benefit](../05_method/CA-M-228-PROGRAMMATIC-CORE-METHOD--adopt-current-python-idioms-only-for-declared-benefit.md)
