---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "python-formatting-and-linting"
  depends_on:
    - "programmatic software"
version: 9
updated_at: "2026-10-04 04:23:29 +0400"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Use Ruff for Python formatting, linting, and complexity

use Ruff as the selected formatter **and** linter for hand-authored PROGRAMMATIC
Python source, including cyclomatic-complexity lint for changed executable
units.

## Applicable when

apply **to** new **or** materially changed Python source within Tools, App, **or** MCP.

## Procedure

1. materialize one pinned Ruff profile **in** `pyproject.toml`.
2. run Ruff formatting **and** linting through the selected uv workflow.
3. enable the Ruff `C901` rule **and** materialize the applicable Evaluation-owned
   complexity maximum under CA-E-539.
4. provide rule diagnostics, measured values, **and** exception rationale **to**
   CA-E-539 for its acceptance **and** disposition decision.
5. keep Ruff evidence distinct from typing **and** behavioral evidence.

## Outcome

mechanical style, lint, **and** cyclomatic-complexity checks use one reproducible
Method-owned selection **and** one materialized profile.

## Failure or stop

return unavailable configuration **when** Ruff is unpinned **or** the current profile
is absent. changed-source acceptance **and** exception admission follow CA-E-539.

## Sources

- [Ruff documentation](https://docs.astral.sh/ruff/)
- [Ruff: configuration](https://docs.astral.sh/ruff/configuration/)
- [Ruff: complex-structure rule](https://docs.astral.sh/ruff/rules/complex-structure/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
