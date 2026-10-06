---
subjects:
  governs: "IS_ALLOWED_VALUE_OF"
  depends_on:
    - "Property"
    - "Entities Graph"
    - "Relation"
version: 6
updated_at: "2026-09-11 04:09:00 +0400"
relations: {}
atom_id: "CA-R-1436"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Define IS_ALLOWED_VALUE_OF

an IS_ALLOWED_VALUE_OF Relation from value V **to** Property P **in** the Entities Graph **means** that governing authority admits V as a possible value of P **in** its qualified context; this Relation does **not** assign V **to** a particular Property occurrence **or** determine that Property's cardinality.
