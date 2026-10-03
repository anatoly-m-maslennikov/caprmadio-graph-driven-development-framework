---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "installed-toolset"
  depends_on: []
version: 8
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-M-103
    - CA-M-221
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Evaluate the installed Toolset across supported boundaries

## Claim checked

The Operator-installed Toolset is self-contained and usable within every
declared Python and platform boundary without depending on development-only uv
state or project-source imports.

## Test case

Apply to the same content-addressed Tool release and installation shape that an
Operator uses.

## Check

Build or install that deliverable and run its public evaluations under every
declared Python and platform boundary. Inspect imports and runtime access for
undeclared state outside the selected release under `.caprmedio_runtime/tools`,
persistent operational state under `.caprmedio_runtime`, and disposable state
under `.caprmedio_tmp`.

## Acceptance

Pass only when every supported combination succeeds without project-source
imports, a project environment, uv, or undeclared external state. Report every
unsupported combination explicitly.

## Failure and stop

Fail when only the local source tree passes, an installed boundary fails, or
the release depends on an undeclared source, environment, runtime place, or
temporary place.

## Sources

- [Pytest: tests outside application code and installed-package testing](https://docs.pytest.org/en/stable/explanation/goodpractices.html)
- [PyPA: requires-python](https://packaging.python.org/en/latest/specifications/core-metadata/#requires-python)
