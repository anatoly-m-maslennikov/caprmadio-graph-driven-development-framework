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
version: 9
updated_at: "2026-10-04 04:23:29 +0400"
relations:
  delivery_for:
    - CA-R-1473
    - CA-M-289
---
# Materialize the Project temporary boundary

the shared Project Temporary State path boundary **must** be carried **in**
canonical source under `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/` **and** the selected
`.caprmedio_runtime/tools/` release.

the root `pyproject.toml` carries the admitted development **and** Evaluation-tool
cache-path configuration. dependency launch Carriers carry explicit temporary,
staging, build, **and** cache-path parameters **when** that dependency does **not**
read `pyproject.toml`. those configured temporary Carriers occupy descendants
of `.caprmedio_tmp/`.

Python bytecode caches use `.caprmedio_tmp/cache/python/`; the corresponding
entrypoint, test-runner, **or** service-launcher Carrier stores that path **or** the
disabled-bytecode-write setting. the delivered Runtime State root **must not**
contain `__pycache__/` Directory Carriers **or** `.pyc` File Carriers.

temporary-path representations carry owner **and** run identity. the boundary
diagnostic representation carries the violating owner **and** path.

CA-R-1473 owns confinement, identity, cleanup-independence, **and** diagnostic
outcomes. CA-M-289 owns temporary-path construction **and** configuration
conventions; CA-E-467 checks their conformance.
