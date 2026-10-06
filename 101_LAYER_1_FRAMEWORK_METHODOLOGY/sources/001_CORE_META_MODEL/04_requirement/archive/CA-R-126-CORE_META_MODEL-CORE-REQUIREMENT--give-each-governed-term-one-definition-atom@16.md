---
subjects:
  governs: "Governed Term"
  depends_on:
    - "Definition Atom"
version: 16
updated_at: "2026-09-22 17:59:17 +0000"
relations:
  child_of:
    - CA-R-918
    - CA-R-1596
atom_id: "CA-R-126"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Give each governed term one Definition Atom

**every** Governed Term **must** resolve **to** **`=1`** active Definition Atom **in** its applicable Claim Scope.
