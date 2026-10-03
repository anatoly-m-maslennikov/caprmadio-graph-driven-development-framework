---
atom_id: CA-E-391
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "mutation-testing"
  depends_on:
    - "programmatic software"
version: 3
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-M-285
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Detect weak Python assertions through mutation testing

## Claim checked

Decision-dense changed Python has assertions strong enough to distinguish its
relevant alternative behavior.

## Test case

Run a pinned mutation profile after normal cases pass and preserve one
surviving relevant mutant in a manager or validator.

## Acceptance criteria

Pass only when the mutant is classified as missing assertion, unreachable,
equivalent, or intentionally uncovered, and the frontier and replay command are
preserved.

## Failure disposition

Reject unexplained survivors; keep this expensive campaign outside synchronous
Hooks.

## Sources

- [Mutmut documentation](https://mutmut.readthedocs.io/en/latest/)
- [CA-M-285 — Select software Evaluation techniques by failure mode](../05_method/CA-M-285-PROGRAMMATIC-CORE-METHOD--select-software-evaluation-techniques-by-failure-mode.md)
