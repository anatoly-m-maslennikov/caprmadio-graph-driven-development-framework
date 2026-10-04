---
subjects:
  governs: "IS_CARRIED_BY"
  depends_on:
    - "CARRIES"
    - "Entity"
    - "Entity/Carrier"
    - "Carrier"
version: 13
updated_at: "2026-09-28 22:47:05 +0000"
relations: {}
atom_id: "CA-D-257"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-257-CORE_META_MODEL-CORE-DELIVERY--define-is-carried-by.md
---
# Summary

Define IS_CARRIED_BY

## Scope

the inverse direction of Carrier bindings.

## Claim

IS_CARRIED_BY **means** the inverse of CARRIES, directed from a non-ephemeral Entity **to** its Carrier.

## Details

the Entity/Carrier binding exposes this direction. its endpoints follow CARRIES, including the exact carried Revision **when** the Entity has Revisions.
