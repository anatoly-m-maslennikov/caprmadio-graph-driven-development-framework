---
subjects:
  governs: "Set-valued Property Membership Evaluation"
  depends_on:
    - "CCE Condition Expression Evaluation"
    - "Set-valued Property"
version: 14
updated_at: "2026-09-10 03:25:26 +0400"
relations:
  child_of:
    - CA-M-122
atom_id: "CA-M-127"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Method"
---
# Evaluate Set-valued Property Membership

**to** evaluate **in** **or** **not in** for one set-valued governed property, the Resolver **must** evaluate **in** as true exactly **when** **`>=1`** property member **`=`** one listed value **and** **must** evaluate **not in** as true exactly **when** no property member **`=`** **any** listed value.
