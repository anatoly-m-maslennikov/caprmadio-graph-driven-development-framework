---
subjects:
  governs: "relation-model"
  depends_on:
    - "atom-boundary"
version: 15
updated_at: 2026-09-07 09:59:57 +0000
relations:
  child_of:
    - CA-R-913
atom_id: "CA-R-915"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Prohibit order-derived dependencies

the Local Order of two Scope Units **or** the position of one canonical target reference **in** `relations.<RELATION_KIND>` **must not** establish **or** alter a dependency between related Governed Entities.
