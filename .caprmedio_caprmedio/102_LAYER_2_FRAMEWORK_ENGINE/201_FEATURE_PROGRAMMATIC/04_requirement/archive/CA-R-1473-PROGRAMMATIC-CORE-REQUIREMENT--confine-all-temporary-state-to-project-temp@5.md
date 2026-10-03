---
atom_id: CA-R-1473
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "PROGRAMMATIC/temporary execution state"
  depends_on:
    - "Temporary State"
    - "Project Settings"
llm_session_ids:
  - codex:01a0263a-7510-7672-bce4-58830bc4d184
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 5
updated_at: 2026-09-15 04:19:10 +0400
relations: {}
---
# Confine all temporary state to project temp

Every temporary File or Directory Carrier created by a CAPRMEDIO-controlled
PROGRAMMATIC execution **must** be located below the configured Project
Temporary State root `.caprmedio_tmp/`. This obligation applies to Tools, App backend
services, MCP components, their tests and Evaluations, their launchers, and
dependencies whose execution they configure. It includes temporary, scratch,
staging, cache, intermediate build or Evaluation, and interrupted-cleanup
Carriers.
Python bytecode caches, including every `__pycache__/` Directory Carrier and
`.pyc` File Carrier, are temporary cache state under this obligation.

A PROGRAMMATIC component **must not** use the repository root, the process
working directory, a source or Delivery Carrier, the Project control root,
`.caprmedio_runtime/`, or a host temporary root as a fallback. If the Project
Temporary State root is unavailable, an invoked dependency cannot be redirected,
or a required same-filesystem atomicity precondition cannot be satisfied, the
component **must** stop before the affected effect and report the boundary
failure.

Temporary state **must not** become authority or installed implementation.
Deleting `.caprmedio_tmp/` **may** discard caches, diagnostics, disposable
workspaces, or interrupted-cleanup remnants, but **must not** discard a governed
Artifact, Project Journal history, an installed release, or resumable runtime
progress.
