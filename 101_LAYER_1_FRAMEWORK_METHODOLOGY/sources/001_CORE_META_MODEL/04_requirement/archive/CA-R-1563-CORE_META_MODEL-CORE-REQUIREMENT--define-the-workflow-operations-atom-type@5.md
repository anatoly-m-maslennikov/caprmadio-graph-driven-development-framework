---
subjects:
  governs: "Atom/Content Role: Operations/Type: Workflow"
  depends_on:
    - "Atom/Content Role: Operations"
    - "Type"
    - "Atom/Claim"
    - "Workflow"
    - "Step"
    - "Atom/Content Role: Operations/Type: Step"
version: 5
updated_at: "2026-09-22 20:07:50 +0000"
relations: {"relates_to": ["CA-R-1530", "CA-R-1565"]}
atom_id: "CA-R-1563"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Define the Workflow Operations Atom Type

the Operations Atom Type Workflow **means** the Type of an Operations Atom whose Claim specifies **`=1`** Workflow graph scheme for that same Atom using references **to** Step Atoms **and** typed directed Relations between those Steps.
