---
atom_id: "CA-M-230"
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs:
    continuant:
      - "python-formatting-and-linting"
  depends_on:
    continuant:
      - "programmatic software"
version: 2
updated_at: "2026-09-05 03:48:00 +0400"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
---
# Use Ruff for Python formatting, linting, and complexity

Use Ruff as the selected formatter and linter for hand-authored PROGRAMMATIC
Python source, including cyclomatic-complexity lint for changed executable
units.

## Applicable when

Apply to new or materially changed Python source within Tools, App, or MCP.

## Procedure

1. Materialize one pinned Ruff profile in `pyproject.toml`.
2. Run Ruff formatting and linting through the selected uv workflow.
3. Enable the Ruff `C901` rule and materialize one accepted complexity maximum.
4. Require changed source to pass the current profile or record one bounded
   exception with the failed rule, measured value, reason, and review condition.
5. Keep Ruff evidence distinct from typing and behavioral evidence.

## Outcome

Mechanical style, lint, and cyclomatic-complexity checks use one reproducible
Method-owned selection and one materialized profile.

## Failure or stop

Stop claiming conformance when Ruff is unpinned, the current profile is absent,
or a changed target fails without a bounded accepted exception.

## Sources

- [Ruff documentation](https://docs.astral.sh/ruff/)
- [Ruff: configuration](https://docs.astral.sh/ruff/configuration/)
- [Ruff: complex-structure rule](https://docs.astral.sh/ruff/rules/complex-structure/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
