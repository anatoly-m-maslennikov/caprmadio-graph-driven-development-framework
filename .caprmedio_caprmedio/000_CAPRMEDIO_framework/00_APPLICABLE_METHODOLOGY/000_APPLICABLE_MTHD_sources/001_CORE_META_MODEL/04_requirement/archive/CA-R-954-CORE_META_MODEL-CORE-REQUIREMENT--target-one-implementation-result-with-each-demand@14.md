---
subjects:
  governs: "Atom/Content Role: Requirement/Type: Demand/Producer Result"
  depends_on:
    - "Atom/Content Role: Implementation"
version: 14
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CA-R-933
atom_id: "CA-R-954"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Target one Implementation result with each Demand

**every** Demand Atom **must** constrain **`=1`** Implementation result produced by its Claim Scope.
