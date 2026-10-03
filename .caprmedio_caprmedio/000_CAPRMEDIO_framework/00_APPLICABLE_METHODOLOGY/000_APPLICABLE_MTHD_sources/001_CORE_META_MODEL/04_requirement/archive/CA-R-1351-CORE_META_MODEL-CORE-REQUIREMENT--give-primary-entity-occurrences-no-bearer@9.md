---
subjects:
  governs: "IS_BORNE_BY"
  depends_on:
    - "Primary Entity"
    - "Subject"
version: 9
updated_at: 2026-09-07 09:59:57 +0000
relations: {}
atom_id: "CA-R-1351"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 9
---
# Give Primary Entity Occurrences No Bearer

a Primary Entity referenced by a Subject **must** have **`=0`** IS_BORNE_BY parents.
