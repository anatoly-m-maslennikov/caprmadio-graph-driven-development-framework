---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "python-static-typing"
  depends_on:
    - "programmatic software"
version: 8
updated_at: "2026-09-11 20:58:34 +0400"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Use Mypy for static Python type checking

use Mypy as the selected static type checker for hand-authored PROGRAMMATIC
Python source **and** ratchet changed targets toward the strict admitted profile.

## Applicable when

apply **to** new **or** materially changed Python source within Tools, App, **or** MCP.

## Procedure

1. materialize one pinned Mypy profile **and** bounded target set **in**
   `pyproject.toml`.
2. run Mypy through the selected uv workflow.
3. require new targets **to** pass the strict admitted profile **and** prevent changed
   targets from regressing below their passing baseline.
4. explain **every** suppression at the narrowest affected line **or** symbol; reject
   an unexplained broad suppression.
5. keep static typing evidence distinct from runtime validation **and** behavioral
   evidence.

## Outcome

changed Python interfaces become more explicit **without** making untyped legacy
source an unrelated whole-project blocker.

## Failure or stop

stop claiming conformance **when** the profile **or** target set is absent, a changed
target regresses, **or** a new unexplained suppression hides the defect.

## Sources

- [Mypy documentation](https://mypy.readthedocs.io/en/stable/)
- [Mypy: using Mypy with an existing codebase](https://mypy.readthedocs.io/en/stable/existing_code.html)
- [Mypy: strict mode](https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-strict)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
