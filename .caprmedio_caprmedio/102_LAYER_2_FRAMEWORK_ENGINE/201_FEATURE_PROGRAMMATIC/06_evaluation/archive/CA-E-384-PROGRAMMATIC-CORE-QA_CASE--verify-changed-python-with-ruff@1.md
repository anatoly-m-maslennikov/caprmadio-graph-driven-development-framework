---
atom_id: CA-E-384
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - python-formatting-and-linting
  depends_on:
    continuant:
      - programmatic software
version: 1
updated_at: 2026-09-01 02:10:00 +0400
relations:
  evaluation_for:
    - CA-M-230
  derived_from:
    - CA-A-053
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
- [CA-M-230 — Use Ruff for Python formatting, linting, and complexity](../05_method/CA-M-230-PROGRAMMATIC-CORE-METHOD--use-ruff-for-python-formatting-linting-and-complexity.md)
