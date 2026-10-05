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
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-127-CORE_META_MODEL-METHOD--evaluate-set-valued-property-membership.md
  source_atom_id: CA-M-127
  source_atom_revision: 15
  source_sha256: bb09a5845cbff2aef2b4b36e84e452f0e798a9771e177150937453fef30bf64d
  original_relations_sha256: 565f63e574a87ad14f65da732f938c81a77229348647edb76e4491faccb0d844
---
# Summary

Evaluate Set-valued Property Membership

## Scope

evaluation of **in** **or** **not in** for one set-valued governed property.

## Claim

**to** evaluate **in** **or** **not in** for one set-valued governed property, the Resolver **must** evaluate **in** as true exactly **when** **`>=1`** property member **`=`** one listed value **and** **must** evaluate **not in** as true exactly **when** no property member **`=`** **any** listed value.

## Details
