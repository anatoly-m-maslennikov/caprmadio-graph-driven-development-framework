---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "cyclomatic-complexity"
  depends_on:
    - "programmatic software"
version: 8
updated_at: "2026-09-17 19:28:02 +0000"
relations:
  evaluation_for:
    - CA-M-162
    - CA-M-164
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject unchecked cyclomatic complexity

## Claim checked

**every** new **or** materially changed executable unit has a result from the admitted
cyclomatic-complexity lint **and** stays within its Method-owned maximum **or** one
accepted bounded exception.

## Test case

Evaluate one materially changed function for which no current complexity-lint
result exists.

## Acceptance criteria

pass **only** **when** conformance is rejected **until** **all** of the following hold:

- the admitted lint reports a value for the changed unit.
- that value satisfies the Method-owned maximum **or** an accepted bounded exception covers that value.

## Failure disposition

Block the changed unit from claiming source-boundary conformance.

## Sources

- [CA-M-162 — Ratchet hand-authored Python source boundaries](../05_method/CA-M-162-PROGRAMMATIC-CORE-METHOD--ratchet-hand-authored-python-source-boundaries.md)
- [CA-M-164 — Ratchet typing and automation adoption](../05_method/CA-M-164-PROGRAMMATIC-CORE-METHOD--ratchet-typing-and-automation-adoption.md)
