---
subjects:
  governs: "Structural Entity/Containment"
  depends_on:
    - "Containment Relation Pair"
    - "Directory Carrier/Nesting"
version: 11
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
atom_id: "CA-D-266"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
---
# Prohibit Persisting Derived Containment

`CONTAINS` **and** `IS_CONTAINED_BY` relations derived from canonical Carrier nesting **must not** be persisted as independent relation declarations.
