---
atom_id: CA-M-221
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - python-workflow-frontend
  depends_on:
    continuant:
      - programmatic software
version: 4
updated_at: 2026-09-01 01:45:00 +0400
relations:
  method_for:
    - CA-R-1047
  derived_from:
    - CA-A-053
---
# Use uv as the default Python workflow frontend

Use uv as the default frontend for every admitted Python workflow capability
that uv provides. This Method owns that tool selection; configuration and
Implementation materialize it, Delivery governs its carriers, and Ops records
actual workflow execution and evidence.

## Applicable when

Apply when developing, evaluating, building, or packaging PROGRAMMATIC Python
source. Installed CAPRMEDIO runtime execution remains outside this Method.

## Procedure

1. Resolve the supported Python boundary from its accepted Method and canonical
   Project technical-configuration materialization, then install or select it
   through `uv python`.
2. Materialize dependencies selected by accepted Methods in `pyproject.toml`;
   change them through `uv add` or `uv remove` so the declaration and `uv.lock`
   change together.
3. Reproduce the project environment with `uv sync --locked` and execute
   governed Python commands with `uv run --locked`.
4. Run an isolated Python CLI through `uv tool run` only with a pinned tool
   version and command when it is not an admitted project dependency.
   Unpinned ephemeral execution cannot supply acceptance evidence.
5. Use `uv build` or `uv publish` only when an accepted Delivery authorizes a
   package or publication target.
6. Do not mix pip, venv, virtualenv, pipx, Poetry, Conda, or another overlapping
   Python workflow manager into the same governed path unless uv lacks a
   required capability or an external boundary requires the alternative.
7. Record an exception with its capability, bounded carriers, exact commands,
   added operational cost, cleanup or recovery procedure, and Operator
   acceptance.
8. Keep uv outside the installed CAPRMEDIO runtime contract. Installed Tools
   remain self-contained under `.caprmedio_install` and execute without uv, a
   project virtual environment, or another dependency outside that
   installation.

## Outcome

One declared Python boundary and one reviewed lockfile reproduce the admitted
Python environment and commands without an undeclared manager or dependency
source.

## Failure or stop

Stop when the supported interpreter cannot be resolved, the lockfile is stale,
a command would update the environment implicitly during evidence collection,
or an exception lacks its accepted boundary.

## Sources

- [uv: Features](https://docs.astral.sh/uv/getting-started/features/)
- [uv: Installing and managing Python](https://docs.astral.sh/uv/guides/install-python/)
- [uv: Locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/)
- [uv: Tools](https://docs.astral.sh/uv/concepts/tools/)
- [uv: Configuring projects](https://docs.astral.sh/uv/concepts/projects/config/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
