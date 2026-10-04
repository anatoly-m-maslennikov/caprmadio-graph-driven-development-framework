---
subjects:
  governs: "Set-valued Property Membership Evaluation"
  depends_on:
    - "CCE Condition Expression Evaluation"
    - "Set-valued Property"
version: 15
updated_at: "2026-10-01 21:38:15 +0400"
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
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-127-CORE_META_MODEL-METHOD--evaluate-set-valued-property-membership.md
---
# Summary

Evaluate Set-valued Property Membership

## Scope

evaluation of **in** **or** **not in** for one set-valued governed property.

## Claim

**to** evaluate **in** **or** **not in** for one set-valued governed property, the Resolver **must** evaluate **in** as true exactly **when** **`>=1`** property member **`=`** one listed value **and** **must** evaluate **not in** as true exactly **when** no property member **`=`** **any** listed value.

## Details
