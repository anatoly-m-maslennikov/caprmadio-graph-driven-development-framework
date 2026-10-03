---
atom_id: CA-E-452
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "python-technical-configuration"
  depends_on:
    - "programmatic software"
version: 3
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-M-281
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify one Python technical configuration boundary

## Claim checked

The selected Python series and development-tool profiles have one canonical
technical materialization distinct from CAPRMEDIO project settings.

## Test case

Compare the root `pyproject.toml`, local workflow, and automated workflow
selections for the interpreter and one admitted development tool.

## Acceptance criteria

Pass only when all consumers resolve the same `3.14.*` boundary and profile,
and no CAPRMEDIO runtime setting is duplicated in `pyproject.toml`.

## Failure disposition

Reject the conflicting carrier or workflow until one Method-owned selection is
materialized once.

## Sources

- [PyPA: `pyproject.toml` specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
- [CA-M-281 — Declare one Python and software configuration boundary](../05_method/CA-M-281-PROGRAMMATIC-CORE-METHOD--declare-one-python-and-software-configuration-boundary.md)
