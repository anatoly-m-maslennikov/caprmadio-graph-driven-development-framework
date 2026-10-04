---
subjects:
  governs: "Structural Entity/Containment"
  depends_on:
    - "Containment Relation Pair"
    - "Directory Carrier/Nesting"
version: 13
updated_at: "2026-10-02 18:57:51 +0400"
relations: {}
atom_id: "CA-D-266"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-266-CORE_META_MODEL-CORE-DELIVERY--prohibit-persisting-derived-containment.md
---
# Summary

Prohibit Persisting Derived Containment

## Scope

`CONTAINS` **and** `IS_CONTAINED_BY` relations derived from canonical Carrier nesting.

## Claim

`CONTAINS` **and** `IS_CONTAINED_BY` relations derived from canonical Carrier nesting **must not** be persisted as independent relation declarations.

## Details
