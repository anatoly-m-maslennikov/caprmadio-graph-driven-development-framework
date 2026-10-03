---
subjects:
  governs: "IS_CARRIED_BY"
  depends_on:
    - "Artifact/Revision"
    - "Structural Entity"
    - "Carrier"
    - "CARRIES"
version: 12
updated_at: "2026-09-28 22:47:05 +0000"
relations: {}
atom_id: "CA-D-257"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Archived"
author: "Anatoly Maslennikov"
type: "Delivery"
global_tier: 9
---
# Define IS_CARRIED_BY

IS_CARRIED_BY **means** the inverse of CARRIES, directed from the exact Artifact Revision **or** Structural Entity Revision **to** its Carrier. its endpoint domain follows CA-D-256; the applicable Carrier authority determines the permitted binding.
