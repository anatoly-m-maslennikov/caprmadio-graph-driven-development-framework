---
atom_id: CA-O-108
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-09-28 16:14:59 +0400"
subjects:
  governs: "RMED Review Selection Step"
  depends_on:
    - "Step"
    - "Action"
    - "Step/Agentic Execution Context"
    - "Workflow Run"
    - "Step Run"
relations: {"relates_to":["CA-O-105"]}
---
# Summary

Select the RMED review batch

## Operation

RMED Review Selection Step **means** the Workflow node invoking **=1** Action, CA-O-105, **in** Integrated context.

- bind inputs from the request, source frontier, applicable authority, settings, effective permissions, budgets, **and** admitted temporary Run directory.
- use native file, command, **and** session capabilities; no MCP server is required. missing capability returns `blocked`, **not** a silent context substitution.
- pass the Action result **and** retained evidence **to** the caller for Workflow routing; do **not** independently copy its behavior.

## Details

the Step binding does **not** authorize mutations beyond the supplied Action permissions.
