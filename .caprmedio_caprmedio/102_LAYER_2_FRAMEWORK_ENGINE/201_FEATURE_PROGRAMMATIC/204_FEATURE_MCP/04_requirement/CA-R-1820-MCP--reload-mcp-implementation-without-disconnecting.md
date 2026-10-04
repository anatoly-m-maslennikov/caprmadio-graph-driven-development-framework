---
atom_id: CA-R-1820
content_role: Requirement
current_scope_unit: MCP
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
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

reload MCP implementation **without** disconnecting

## Scope

server-side hot reload for the Project-local MCP gateway.

automatic file watching **and** operating-system startup hooks are outside this initial capability.

## Claim

the MCP gateway **must** provide Operator-requested implementation reload while preserving the established transport connection **and** its fixed Project boundary.

the reload capability has these required outcomes:

- a successful reload makes **`=1`** validated implementation generation available for new calls.
- a failed reload retains the previously serving generation **and** reports the failure.
- an in-flight call retains its admitted generation **until** it finishes; reload does **not** replay, cancel **or** migrate that call.

## Details

- reload **only** changes executable capability availability; it grants **no** new authority **to** mutate Atoms, start Workflows **or** launch workers.

