---
atom_id: CA-M-229
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - python-technical-configuration
  depends_on:
    continuant:
      - programmatic software
version: 2
updated_at: 2026-09-01 02:35:00 +0400
relations:
  method_for:
    - CA-R-1047
  derived_from:
    - CA-A-053
---
# Declare one Python and software configuration boundary

Select the stable CPython `3.14.*` series and require one project-owned
technical configuration boundary for interpreter, formatting, linting, typing,
evaluation, and packaging. CA-D-250 owns the current carrier placement and
encoding in the root `pyproject.toml`; configuration and Implementation
materialize this Method's selections there. Keep that technical configuration
separate from CAPRMEDIO project settings.

## Applicable when

Apply when Python source or a development workflow depends on an interpreter,
dependency, formatter, linter, type checker, evaluator, or packager setting.

## Procedure

1. Resolve the current Delivery carrier, then materialize the selected
   interpreter series and admitted development-tool profiles through that
   boundary.
2. Keep one value for each setting and make local and automated workflows read
   that value rather than reproduce it.
3. Change the interpreter series or a selected tool profile only through its
   accepted Method before changing configuration.
4. Verify the selected stable series before using version-specific behavior.
5. Keep runtime project settings outside `pyproject.toml` and expose them only
   through the shared Settings Reader.

## Outcome

This Method owns one set of Python workflow selections; Delivery owns its
carrier, and configuration and Implementation reproduce the selections without
becoming another methodological authority.

## Failure or stop

Stop when two carriers disagree, a moving `latest` label replaces the selected
series, the materialization conflicts with its Delivery, or technical and
CAPRMEDIO project settings are mixed.

## Sources

- [Python 3.14 release notes](https://docs.python.org/3.14/whatsnew/3.14.html)
- [PyPA: `pyproject.toml` specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
- [CA-A-054 — Validate the Python 3.14 contract upgrade](../02_analysis/CA-A-054-PROGRAMMATIC-ANALYSIS_RPRT--validate-python-3-14-contract-upgrade.md)
