---
atom_id: CA-E-390
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - golden-baseline
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
# Compare deterministic outputs with reviewed golden baselines

## Claim checked

A large deterministic output changes only through a reviewed semantic diff.

## Test case

Change one deterministic Markdown or machine-envelope output and invoke its
golden comparison with only declared volatile fields normalized.

## Acceptance criteria

Pass only when the unexplained difference fails, critical invariants remain
focused assertions, and a replacement baseline requires explicit diff review.

## Failure disposition

Reject automatic baseline refresh and return the semantic difference for
review.

## Sources

- [Syrupy snapshot testing](https://github.com/syrupy-project/syrupy)
- [CA-M-233 — Select software Evaluation techniques by failure mode](../05_method/CA-M-233-PROGRAMMATIC-CORE-METHOD--select-software-evaluation-techniques-by-failure-mode.md)
