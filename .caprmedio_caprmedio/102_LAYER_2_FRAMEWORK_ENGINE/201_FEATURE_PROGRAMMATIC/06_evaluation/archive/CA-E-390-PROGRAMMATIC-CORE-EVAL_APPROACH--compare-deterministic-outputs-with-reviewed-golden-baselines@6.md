---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "golden-baseline"
  depends_on:
    - "programmatic software"
version: 6
updated_at: "2026-09-11 20:58:34 +0400"
relations:
  evaluation_for:
    - CA-M-285
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Compare deterministic outputs with reviewed golden baselines

## Claim checked

A large deterministic output changes **only** through a reviewed semantic diff.

## Test case

Change one deterministic Markdown **or** machine-envelope output **and** invoke its
golden comparison with **only** declared volatile fields normalized.

## Acceptance criteria

pass **only** **when** the unexplained difference fails, critical invariants remain
focused assertions, **and** a replacement baseline requires explicit diff review.

## Failure disposition

Reject automatic baseline refresh **and** return the semantic difference for
review.

## Sources

- [Syrupy snapshot testing](https://github.com/syrupy-project/syrupy)
- [CA-M-285 — Select software Evaluation techniques by failure mode](../05_method/CA-M-285-PROGRAMMATIC-CORE-METHOD--select-software-evaluation-techniques-by-failure-mode.md)
