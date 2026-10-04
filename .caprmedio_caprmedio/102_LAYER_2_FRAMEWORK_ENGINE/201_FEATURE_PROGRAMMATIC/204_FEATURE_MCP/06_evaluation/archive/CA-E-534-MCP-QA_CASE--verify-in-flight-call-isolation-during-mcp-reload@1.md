---
atom_id: CA-E-534
content_role: Evaluation
type: QA_CASE
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-03 20:41:31 +0400"
subjects:
  governs: "MCP/Tool invocation"
  depends_on: [MCP, Tool, Operator, Project, Implementation, Workflow, Atom]
---
# Summary

Verify in-flight call isolation during MCP reload

## Scope

server-side hot reload for the Project-local MCP gateway.

## Claim

the MCP Evaluation **must** verify that reload preserves admitted call identity, authority **and** truthful outcomes.

## Details

- hold a call on A while publishing B; verify that the old call completes on A **and** a new call executes on B.
- verify that old generations remain alive while their admitted calls are running.
- simulate child-process failure **after** a mutating call starts; verify an explicit uncertain outcome **and** no automatic replay.
- exercise concurrent reload requests, duplicate request IDs **and** drain limits; verify serialized publication **and** bounded explicit diagnostics.
- verify that reload does **not** start a Workflow, Codex Agent, independent worker **or** source mutation.
- retain existing MCP request validation **and** Project-boundary regression tests.
