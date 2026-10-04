---
atom_id: CA-R-1818
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 04:10:07 +0400"
subjects:
  governs: "Workflow Orchestrator/Docker runtime"
  depends_on: [Operator, Workflow Run, Action, Tool, Implementation, Journal, Atom]
relations:
  relates_to: [CA-R-1812, CA-R-1813, CA-R-1799]
---
# Summary

provide an explicitly managed Docker runtime

## Scope

the Docker execution option for WORKFLOW_ORCHESTRATOR **and** its MCP **and** Tool capabilities.

## Claim

the Docker runtime **must** preserve authorized Workflow behavior **and** durable execution evidence while providing explicit build, start, stop, restart, status **and** log capabilities.

## Details

- installation starts no Run. starting services is a separate Operator-authorized operation.
- stopping **or** replacing a container preserves the queue, admitted proposals, source Atoms, shared Journal **and** full reports.
- readiness, queue admission, Agent completion **and** accepted Workflow completion remain separate results.
- a new Docker queue does **not** silently import **or** execute a native queue's requests. an authorized pending request can be admitted explicitly with fresh source **and** rule bindings.
- interruption preserves uncertain dispatches for reconciliation rather than automatically repeating them.
