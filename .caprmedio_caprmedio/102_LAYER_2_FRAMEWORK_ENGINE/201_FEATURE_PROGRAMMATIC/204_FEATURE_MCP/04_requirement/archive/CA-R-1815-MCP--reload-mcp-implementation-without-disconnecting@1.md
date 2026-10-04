---
atom_id: CA-R-1815
content_role: Requirement
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: '2026-10-04T05:54:48.186357+04:00'
subjects:
  governs: MCP/implementation
  depends_on:
  - MCP
  - Tool
  - Operator
  - Project
  - Implementation
  - Workflow
  - Atom
---
# Summary

Reload MCP implementation without disconnecting

## Scope

server-side hot reload for the Project-local MCP gateway.

## Claim

the MCP gateway **must** provide Operator-requested implementation reload while preserving the established transport connection **and** its fixed Project boundary.

## Details

- a successful reload makes one validated implementation generation available for new calls.
- a failed reload retains the previously serving generation **and** reports the failure.
- an in-flight call retains its admitted generation until it finishes; reload does **not** replay, cancel **or** migrate that call.
- reload **only** changes executable capability availability; it grants **no** new authority to mutate Atoms, start Workflows **or** launch workers.
- automatic file watching **and** operating-system startup hooks are outside this initial capability.

