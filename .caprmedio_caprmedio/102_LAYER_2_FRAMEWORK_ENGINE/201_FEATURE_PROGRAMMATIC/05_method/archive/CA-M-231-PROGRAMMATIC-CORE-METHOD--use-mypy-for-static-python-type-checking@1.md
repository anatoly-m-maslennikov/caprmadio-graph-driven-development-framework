---
atom_id: CA-M-231
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - python-static-typing
  depends_on:
    continuant:
      - programmatic software
version: 1
updated_at: 2026-09-01 01:50:00 +0400
relations:
  method_for:
    - CA-R-1047
  derived_from:
    - CA-A-053
---
# Use Mypy for static Python type checking

Use Mypy as the selected static type checker for hand-authored PROGRAMMATIC
Python source and ratchet changed targets toward the strict admitted profile.

## Applicable when

Apply to new or materially changed Python source within Tools, App, or MCP.

## Procedure

1. Materialize one pinned Mypy profile and bounded target set in
   `pyproject.toml`.
2. Run Mypy through the selected uv workflow.
3. Require new targets to pass the strict admitted profile and prevent changed
   targets from regressing below their passing baseline.
4. Explain every suppression at the narrowest affected line or symbol; reject
   an unexplained broad suppression.
5. Keep static typing evidence distinct from runtime validation and behavioral
   evidence.

## Outcome

Changed Python interfaces become more explicit without making untyped legacy
source an unrelated whole-project blocker.

## Failure or stop

Stop claiming conformance when the profile or target set is absent, a changed
target regresses, or a new unexplained suppression hides the defect.

## Sources

- [Mypy documentation](https://mypy.readthedocs.io/en/stable/)
- [Mypy: using Mypy with an existing codebase](https://mypy.readthedocs.io/en/stable/existing_code.html)
- [Mypy: strict mode](https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-strict)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
