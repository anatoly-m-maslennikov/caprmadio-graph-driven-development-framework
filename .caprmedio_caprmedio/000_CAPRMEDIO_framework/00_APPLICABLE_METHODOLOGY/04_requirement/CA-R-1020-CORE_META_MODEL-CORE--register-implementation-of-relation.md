---
subjects:
  governs: "Implementation Of Relation"
  depends_on:
    - "atom-boundary"
    - "relation-model"
version: 15
updated_at: "2026-10-01 21:41:08 +0400"
relations: {}
atom_id: "CA-R-1020"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1020-CORE_META_MODEL-CORE--register-implementation-of-relation.md
---
# Summary

Register implementation_of relation

## Scope

the `implementation_of` direct relation owned by a governed Implementation carrier.

## Claim

`implementation_of` **must** be registered as a direct relation owned by a governed Implementation carrier **and** directed **to** **`=1`** specification Atom that the carrier implements.

## Details
