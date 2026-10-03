---
atom_id: CA-E-453
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "python-formatting-and-linting"
  depends_on:
    - "programmatic software"
version: 4
updated_at: "2026-09-11 20:58:34 +0400"
relations:
  evaluation_for:
    - CA-M-282
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify changed Python with Ruff

## Claim checked

Changed Python passes the one admitted Ruff format, lint, and complexity
profile or carries one bounded exception.

## Test case

Run the pinned Ruff profile against one changed module containing an executable
unit above the configured `C901` maximum.

## Acceptance criteria

Pass only when Ruff reports the unit and the change is rejected or one explicit
exception records the rule, value, reason, and review condition.

## Failure disposition

Reject the changed target until the diagnostic is resolved or bounded.

## Sources

- [Ruff: complex-structure rule](https://docs.astral.sh/ruff/rules/complex-structure/)
- [CA-M-282 — Use Ruff for Python formatting, linting, and complexity](../05_method/CA-M-282-PROGRAMMATIC-CORE-METHOD--use-ruff-for-python-formatting-linting-and-complexity.md)
