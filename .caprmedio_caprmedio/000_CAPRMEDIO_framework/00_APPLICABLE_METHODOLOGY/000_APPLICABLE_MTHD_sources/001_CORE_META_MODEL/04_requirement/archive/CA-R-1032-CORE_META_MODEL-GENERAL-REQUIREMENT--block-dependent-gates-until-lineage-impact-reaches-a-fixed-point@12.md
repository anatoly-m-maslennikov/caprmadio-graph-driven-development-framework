---
subjects:
  governs: "relation-model"
  depends_on:
    - "atom-boundary"
    - "lifecycle-traceability"
version: 12
updated_at: "2026-09-10 06:39:08 +0400"
relations: {}
atom_id: "CA-R-1032"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Block dependent gates until Lineage Impact reaches a fixed point

**every** release **or** downstream gate that requires a revised Atom **must** remain blocked **until** its Lineage Impact Analysis concludes that **every** affected branch has reached a fixed point.
