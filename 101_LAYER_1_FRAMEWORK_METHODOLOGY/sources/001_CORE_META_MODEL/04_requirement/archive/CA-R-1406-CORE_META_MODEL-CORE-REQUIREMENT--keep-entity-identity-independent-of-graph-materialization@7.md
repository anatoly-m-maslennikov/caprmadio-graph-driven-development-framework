---
subjects:
  governs: "Entity/Identity"
  depends_on:
    - "Entity"
    - "CAPRMEDIO Graph"
    - "Projection"
version: 7
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CA-R-1248
atom_id: "CA-R-1406"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Keep Entity Identity Independent of Graph Materialization

materializing, refreshing, **or** deleting a Graph Projection **must not** establish, change, **or** remove Entity identity.
