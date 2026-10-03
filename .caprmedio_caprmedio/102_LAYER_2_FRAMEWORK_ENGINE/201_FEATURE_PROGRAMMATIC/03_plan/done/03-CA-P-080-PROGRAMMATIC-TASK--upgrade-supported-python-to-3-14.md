---
cce_version: cce_1
cce_form: obligation
subjects:
  - python-runtime
  - programmatic-delivery
  - compatibility
version: 2
updated_at: 2026-08-23 16:37:00
autonomous_confidence_threshold: 98
---
# Upgrade supported Python to 3.14

WHEN the Operator accepts CPython 3.14 as the supported stable series, THE Assignee MUST replace the accepted CPython 3.12 technical selection with CPython `3.14.*`, align every current checked-in support carrier, and record exact-revision validation under a stable 3.14 release.

## Scope

`(Atom ID IN (CA-A-054, CA-R-1047, CA-M-110, CA-E-250, CA-D-250) OR Path IN (pyproject.toml, .github/workflows/publish-release.yml))`

## Definition of Done

THE Task is NOT DONE IF (`pyproject.toml` does not select `==3.14.*` OR a current checked-in Python support carrier still selects 3.12 OR validation does not record the exact CPython 3.14 patch release, source frontier, commands, and outcomes OR validation writes Python cache files into governed source directories OR the default standard-library-first dependency boundary changes without separate authority OR completed CA-P-071 history is rewritten OR the Task claims that workflow configuration alone proves a successful hosted run).

## Details

Use the stable CPython 3.14 series rather than the moving phrase `latest stable`. Preserve the existing R/M/E/D ownership: `pyproject.toml` owns the selected technical value while CA-R-1047, CA-M-110, CA-E-250, and CA-D-250 govern its meaning, method, evaluation boundary, and delivery.

Update the configured workflow interpreter to 3.14, but distinguish the declared workflow boundary from hosted execution evidence. Validate the current Programmatic Python source and installed read-only Tool interfaces with the local stable 3.14 interpreter. Do not run the repository's suspended test suite as part of this Task.

## Source

- [Python 3.14.7](https://www.python.org/downloads/release/python-3147/), released 2026-08-05.

## Execution evidence

- `pyproject.toml` selects `supported_python = "==3.14.*"` and preserves `required_runtime_dependencies = []`.
- `.github/workflows/publish-release.yml` selects `python-version: "3.14"`.
- CA-A-054 records exact bounded local validation under CPython 3.14.7 on Darwin arm64 at Git revision `26e3575635e5764d24590165106cf7480d06e67f`.
- All 65 current Programmatic Python source files compiled in memory without a syntax failure.
- All 15 installed launchers returned successful read-only `describe` envelopes.
- The suspended test suite and hosted workflow were not run, and no claim of their success is made.
- The validation created no source-tree bytecode cache. Four pre-existing source cache directories are recorded as a separate source-hygiene issue in CA-A-054.

The selected series, checked-in workflow selector, local validation boundary, limitations, and unchanged dependency contract satisfy this Task.
