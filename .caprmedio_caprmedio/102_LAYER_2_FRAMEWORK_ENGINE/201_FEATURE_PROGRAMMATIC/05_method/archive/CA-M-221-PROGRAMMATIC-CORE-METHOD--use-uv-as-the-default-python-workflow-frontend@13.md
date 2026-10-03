---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "python-workflow-frontend"
  depends_on:
    - "Journal/Record"
    - "Atom/Content Role: Operations"
    - "programmatic software"
version: 13
updated_at: "2026-09-17 19:02:49 +0000"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Use uv as the default Python workflow frontend

use uv as the default frontend for **every** admitted Python workflow capability
that uv provides. this Method owns that tool selection; configuration **and**
Implementation materialize it, Delivery governs its carriers, Operations defines reusable workflow behavior,
**and** Journal Records carry evidence of actual workflow execution.

## Applicable when

apply **when** developing, evaluating, building, **or** packaging PROGRAMMATIC Python
source. installed CAPRMEDIO runtime execution remains outside this Method.

## Procedure

1. resolve the supported Python boundary from its accepted Method **and** canonical
   Project technical-configuration materialization, **then** install **or** select it
   through `uv python`.
2. materialize dependencies selected by accepted Methods **in** `pyproject.toml`;
   change them through `uv add` **or** `uv remove` so the declaration **and** `uv.lock`
   change together.
3. reproduce the project environment with `uv sync --locked` **and** execute
   governed Python commands with `uv run --locked`.
4. run an isolated Python CLI through `uv tool run` **only** with a pinned tool
   version **and** command **when** it is **not** an admitted project dependency.
   Unpinned ephemeral execution cannot supply acceptance evidence.
5. use `uv build` **or** `uv publish` **only** **when** an accepted Delivery authorizes a
   package **or** publication target.
6. do **not** mix pip, venv, virtualenv, pipx, Poetry, Conda, **or** another overlapping
   Python workflow manager into the same governed path **unless** uv lacks a
   required capability **or** an external boundary requires the alternative.
7. record an exception with its capability, bounded carriers, exact commands,
   added operational cost, cleanup **or** recovery procedure, **and** Operator
   acceptance.
8. keep uv outside the installed CAPRMEDIO runtime contract. installed Tools
   remain self-contained under `.caprmedio_runtime/tools` **and** execute **without** uv, a
   project virtual environment, **or** another dependency outside that selected
   runtime release. route uv cache, build, **and** staging state into
   `.caprmedio_tmp/`.

## Outcome

one declared Python boundary **and** one reviewed lockfile reproduce the admitted
Python environment **and** commands **without** an undeclared manager **or** dependency
source.

## Failure or stop

stop **when** the supported interpreter cannot be resolved, the lockfile is stale,
a command would update the environment implicitly during evidence collection,
**or** an exception lacks its accepted boundary.

## Sources

- [uv: Features](https://docs.astral.sh/uv/getting-started/features/)
- [uv: Installing and managing Python](https://docs.astral.sh/uv/guides/install-python/)
- [uv: Locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/)
- [uv: Tools](https://docs.astral.sh/uv/concepts/tools/)
- [uv: Configuring projects](https://docs.astral.sh/uv/concepts/projects/config/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
