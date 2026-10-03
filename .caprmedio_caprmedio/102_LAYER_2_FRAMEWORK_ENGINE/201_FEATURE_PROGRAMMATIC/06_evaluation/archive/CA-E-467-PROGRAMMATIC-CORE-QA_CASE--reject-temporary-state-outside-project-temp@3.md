---
atom_id: CA-E-467
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - PROGRAMMATIC/temporary execution state
  depends_on:
    continuant:
      - programmatic software
llm_session_ids:
  - codex:01a0263a-7510-7672-bce4-58830bc4d184
version: 3
updated_at: 2026-09-15 04:19:10 +0400
relations:
  evaluation_for:
    - CA-R-1473
    - CA-M-289
---
# Reject temporary state outside project temp

## Claim checked

One CAPRMEDIO-controlled PROGRAMMATIC execution confines every temporary
Carrier created by its components and configured dependencies below the
Project Temporary State root.

## Test case

Set the process working directory and ambient host temporary location to
repository locations outside `.caprmedio_tmp/`. Run representative Tool,
App backend, and MCP fixtures, including their test runner and one configured
dependency. Exercise Python bytecode and dependency cache creation, a temporary
workspace, atomic staging, and an interrupted or denied cleanup. Compare the complete path frontier
outside the Temporary State root before and after execution, and inspect the
applicable source and technical configuration for unredirected temporary-path
creation.

## Acceptance criteria

Pass only when every created temporary, scratch, staging, cache, build,
Evaluation, and cleanup-remnant File or Directory Carrier is below the
configured `.caprmedio_tmp/` root; each concurrent owner uses its declared
component or run-specific descendant; no applicable source or configuration
uses an ambient or hard-coded host temporary fallback; and deleting the Runtime
State root cannot delete governed authority, Project Journal history, selected
runtime releases, logs, sessions, databases, service state, or resumable state.
No `__pycache__/` Directory Carrier or `.pyc` File Carrier exists below
`.caprmedio_runtime/` after the execution.

## Failure disposition

Reject the changed component, test workflow, dependency configuration, or
release until every observed and statically detectable temporary Carrier is
redirected to the Project Temporary State root. Report each violating path and
its creating owner.
