---
subjects:
  governs: "Atom/Content Role: Requirement/Type: Demand/Direction"
  depends_on:
    - "Local Order"
    - "Scope Unit/Type: Ordered"
version: 10
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
atom_id: "CA-R-1293"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Prohibit Demands to Later Ordered Siblings

a Demand Atom owned by an Ordered Scope Unit **must not** target a later Ordered sibling under the same direct parent.
