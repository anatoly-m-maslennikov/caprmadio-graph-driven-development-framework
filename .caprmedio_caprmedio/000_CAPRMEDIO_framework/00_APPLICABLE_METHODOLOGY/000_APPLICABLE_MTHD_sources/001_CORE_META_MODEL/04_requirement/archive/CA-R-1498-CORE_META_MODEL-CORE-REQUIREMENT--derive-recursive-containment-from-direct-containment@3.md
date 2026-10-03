---
subjects:
  governs: "Structural Entity/Recursive Containment"
  depends_on:
    - "Structural Entity/Direct Containment"
version: 3
updated_at: "2026-09-17 04:41:41 +0000"
relations: {}
atom_id: "CA-R-1498"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Derive Recursive Containment from Direct Containment

recursive Structural Entity containment **must** **`=`** the transitive closure of direct Structural Entity containment.
