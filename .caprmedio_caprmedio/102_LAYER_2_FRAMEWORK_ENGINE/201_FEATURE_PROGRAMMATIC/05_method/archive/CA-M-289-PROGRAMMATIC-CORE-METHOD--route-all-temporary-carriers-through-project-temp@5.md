---
atom_id: CA-M-289
cce_version: cce_1
cce_form: method
subjects:
  governs: "PROGRAMMATIC/temporary execution state"
  depends_on:
    - "programmatic software"
    - "Project Settings"
llm_session_ids:
  - codex:01a0263a-7510-7672-bce4-58830bc4d184
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 5
updated_at: 2026-09-15 04:19:10 +0400
relations:
  method_for:
    - CA-R-1473
---
# Route all temporary Carriers through project temp

Resolve the configured Project Temporary State root before a PROGRAMMATIC
component creates a temporary Carrier or invokes a dependency that can create
one. Allocate a component-owned and, when concurrency is possible, run-specific
descendant below `.caprmedio_tmp/`. Pass that descendant explicitly to
temporary-file APIs and configure dependency cache, temporary, staging, build,
and Evaluation paths before invocation. Do not rely on an ambient host
temporary directory or the process working directory.

Route Python bytecode cache output to `.caprmedio_tmp/cache/python/` before
importing Project modules, or disable bytecode writes for an isolated process.
Do not create `__pycache__/` or `.pyc` Carriers below `.caprmedio_runtime/`.

For an atomic replacement, create its staging Carrier below the Project
Temporary State root and verify that the staging and destination Carriers satisfy the
required same-filesystem atomicity boundary before the first mutation. Stop
without falling back to a destination sibling or host temporary location when
that precondition is false.

Attempt bounded cleanup when the owning operation ends. Treat interrupted or
denied cleanup as retained non-authoritative temporary state, report its owned
path, and leave it confined below `.caprmedio_tmp/`. Never weaken placement
because cleanup is best-effort.

Keep executable releases, shared implementation libraries, registries, stable
launchers, Hook Carriers, runtime logs, sessions, databases, service state,
resumable state, and governed Artifacts outside the Temporary State root in
their applicable authority or runtime places.
