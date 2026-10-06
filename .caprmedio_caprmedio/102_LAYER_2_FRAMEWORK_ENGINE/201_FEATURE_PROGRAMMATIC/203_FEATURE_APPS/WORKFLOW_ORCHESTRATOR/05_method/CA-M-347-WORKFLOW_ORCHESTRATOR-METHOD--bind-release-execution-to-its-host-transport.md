---
atom_id: CA-M-347
content_role: Method
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 01:01:23 +0000"
subjects:
  governs: "Release Version/Host Executor/Transport Binding"
  depends_on: [Release Version, Workflow Run, Operator, Queue, DBOS, Source, Implementation]
relations:
  method_for: [CA-R-1891]
  relates_to: [CA-O-164]
---
# Summary

bind Release execution to its host transport

## Scope

transport selection for source-admitted Release Version Runs in WORKFLOW_ORCHESTRATOR.

## Claim

the Host Executor **must** bind **every** admitted Release Run **to** its exact frozen request **and** isolated host transport before scheduling it.

## Details

- validate the existing selected-route seals **and** current Source bindings before accepting a new Run.
- use the dedicated host Queue **and** worker; verify the frozen Release route again at worker dispatch.
- pass the fixed host namespace **to** the executor subprocess. do **not** change the MCP process's shared environment **to** select a transport.
- observation **and** recovery use the Run's retained transport binding. a Run bound **to** another executor is **not** adopted.
- unchanged requests can reuse their exact binding idempotently. a conflicting request, missing worker readiness **or** uncertain prior effect blocks continuation.
