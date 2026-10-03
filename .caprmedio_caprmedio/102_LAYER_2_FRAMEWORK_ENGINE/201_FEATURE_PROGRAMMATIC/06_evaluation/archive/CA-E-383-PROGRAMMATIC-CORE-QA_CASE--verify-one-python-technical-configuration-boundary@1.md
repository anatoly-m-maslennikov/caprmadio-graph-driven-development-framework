---
atom_id: CA-E-383
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - python-technical-configuration
  depends_on:
    continuant:
      - programmatic software
version: 1
updated_at: 2026-09-01 02:10:00 +0400
relations:
  evaluation_for:
    - CA-M-229
  derived_from:
    - CA-A-053
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
- [CA-M-229 — Declare one Python and software configuration boundary](../05_method/CA-M-229-PROGRAMMATIC-CORE-METHOD--declare-one-python-and-software-configuration-boundary.md)
