---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "PROGRAMMATIC/temporary-path configuration"
  depends_on:
    - "PROGRAMMATIC/software carriers"
    - "Project Settings"
llm_session_ids:
  - codex:01a0263a-7510-7672-bce4-58830bc4d184
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 6
updated_at: 2026-09-15 04:19:10 +0400
relations:
  delivery_for:
    - CA-R-1473
    - CA-M-289
---
# Materialize the Project temporary boundary

The PROGRAMMATIC Delivery **must** materialize one shared Project Temporary State
path boundary in canonical source under `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/`
and the selected `.caprmedio_runtime/tools/` release. Every Tool, App backend, MCP
component, test launcher, and dependency launcher **must** use that boundary to
allocate owned temporary descendants below `.caprmedio_tmp/`.

The root `pyproject.toml` **must** route admitted Python development and
Evaluation tool caches into `.caprmedio_tmp/`. Launch Carriers **must**
provide explicit run-specific temporary, staging, build, and cache locations
for dependencies that do not read `pyproject.toml`. Canonical source and
configuration **must not** select the repository root, source tree, Project
control root, `.caprmedio_runtime/`, or a host temporary root for those
Carriers.

Python entrypoints, test runners, **and** service launchers **must** route
bytecode caches into `.caprmedio_tmp/cache/python/` or disable bytecode writes.
The delivered Runtime State root **must not** contain `__pycache__/` Directory
Carriers or `.pyc` File Carriers.

The delivered boundary **must** preserve owner and run identity in retained
paths, support bounded cleanup without requiring it for correctness, and emit
one stable diagnostic containing the violating owner and path whenever safe
runtime placement cannot be established.
