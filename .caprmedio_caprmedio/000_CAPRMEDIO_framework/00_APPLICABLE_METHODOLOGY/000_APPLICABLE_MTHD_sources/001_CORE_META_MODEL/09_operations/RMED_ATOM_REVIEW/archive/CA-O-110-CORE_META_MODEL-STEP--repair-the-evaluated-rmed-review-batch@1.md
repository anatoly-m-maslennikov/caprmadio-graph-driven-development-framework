---
atom_id: CA-O-110
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
  governs: "RMED Review Repair Step"
  depends_on:
    - "Step"
    - "Action"
    - "Step/Agentic Execution Context"
    - "Workflow Run"
    - "Step Run"
relations: {"relates_to":["CA-O-107"]}
---
# Summary

Repair the evaluated RMED review batch

## Operation

RMED Review Repair Step **means** the Workflow node invoking **=1** Action, CA-O-107, **in** Integrated context.

- bind inputs from the verified manifest, complete per-Atom reports, source **and** authority bindings, admitted mutation boundary, confidence **and** retry policy, **and** the same implemented Evaluation.
- use native file, command, **and** session capabilities; no MCP server is required. missing capability returns `blocked`, **not** a silent context substitution.
- pass the Action result **and** retained evidence **to** the caller for Workflow routing; do **not** independently copy its behavior.

## Details

the Step binding does **not** authorize mutations beyond the supplied Action permissions.
