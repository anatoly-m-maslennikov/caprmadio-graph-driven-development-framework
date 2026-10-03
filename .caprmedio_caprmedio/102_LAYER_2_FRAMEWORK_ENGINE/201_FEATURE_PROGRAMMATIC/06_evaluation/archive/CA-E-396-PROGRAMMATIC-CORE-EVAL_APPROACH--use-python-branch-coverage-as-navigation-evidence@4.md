---
atom_id: CA-E-396
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "branch-coverage"
  depends_on:
    - "programmatic software"
version: 4
updated_at: "2026-09-11 20:58:34 +0400"
relations:
  evaluation_for:
    - CA-M-285
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
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
- [CA-M-285 — Select software Evaluation techniques by failure mode](../05_method/CA-M-285-PROGRAMMATIC-CORE-METHOD--select-software-evaluation-techniques-by-failure-mode.md)
