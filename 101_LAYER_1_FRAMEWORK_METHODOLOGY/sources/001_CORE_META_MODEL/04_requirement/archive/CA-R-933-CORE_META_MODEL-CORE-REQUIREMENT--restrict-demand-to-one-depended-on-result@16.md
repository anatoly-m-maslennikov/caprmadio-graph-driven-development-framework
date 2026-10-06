---
subjects:
  governs: "Atom/Content Role: Requirement/Type: Demand/Producer Result"
  depends_on:
    - "Consumer/Goal"
    - "Producer/Result"
version: 16
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CA-R-932
atom_id: "CA-R-933"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 9
---
# Restrict Demand to one depended-on result

**every** Demand Atom **must** constrain **`=1`** Producer result on which its Consumer's accepted Goal depends.
