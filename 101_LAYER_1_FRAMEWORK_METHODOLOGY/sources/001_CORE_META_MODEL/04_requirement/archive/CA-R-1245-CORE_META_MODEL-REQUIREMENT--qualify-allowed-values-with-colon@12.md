---
subjects:
  governs: "Subject Expression"
  depends_on:
    - "IS_ALLOWED_VALUE_OF"
    - "Property"
version: 12
updated_at: "2026-09-17 17:16:39 +0000"
relations: {}
atom_id: "CA-R-1245"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Qualify Allowed Values with Colon

**in** a Subject Expression, `:` **must** express **only** one IS_ALLOWED_VALUE_OF relation from the following value **to** the immediately preceding Property occurrence.
