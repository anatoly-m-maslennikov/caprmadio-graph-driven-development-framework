---
atom_id: CA-E-396
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - branch-coverage
  depends_on:
    continuant:
      - programmatic software
version: 1
updated_at: 2026-09-01 02:10:00 +0400
relations:
  evaluation_for:
    - CA-M-233
  derived_from:
    - CA-A-053
---
# Use Python branch coverage as navigation evidence

## Claim checked

Branch coverage locates unobserved alternatives without being treated as proof
of correctness.

## Test case

Collect branch coverage for one changed decision unit with one intentionally
unobserved failure branch.

## Acceptance criteria

Pass only when the missing branch is reported for review, the target and
omissions are stated, and acceptance depends on public-outcome assertions rather
than a percentage alone.

## Failure disposition

Reject reliance based solely on the coverage percentage.

## Sources

- [Coverage.py: branch coverage](https://coverage.readthedocs.io/en/latest/branch.html)
- [CA-M-233 — Select software Evaluation techniques by failure mode](../05_method/CA-M-233-PROGRAMMATIC-CORE-METHOD--select-software-evaluation-techniques-by-failure-mode.md)
