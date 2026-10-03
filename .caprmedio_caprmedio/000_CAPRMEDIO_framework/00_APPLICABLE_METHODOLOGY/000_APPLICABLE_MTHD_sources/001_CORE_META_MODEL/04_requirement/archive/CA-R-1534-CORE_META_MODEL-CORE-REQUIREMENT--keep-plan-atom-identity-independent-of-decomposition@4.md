---
subjects:
  governs: "Atom/Content Role: Plan/Identity"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
version: 4
updated_at: "2026-09-22 14:41:44 +0000"
relations: {"relates_to": ["CA-R-1578"]}
atom_id: "CA-R-1534"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Keep Plan Atom Identity Independent from Decomposition

adding, removing, reordering, **or** changing a decomposed Plan Atom **must not** establish **or** replace the Hub Atom's identity; **every** related Atom retains its independent Claim **and** lifecycle.
