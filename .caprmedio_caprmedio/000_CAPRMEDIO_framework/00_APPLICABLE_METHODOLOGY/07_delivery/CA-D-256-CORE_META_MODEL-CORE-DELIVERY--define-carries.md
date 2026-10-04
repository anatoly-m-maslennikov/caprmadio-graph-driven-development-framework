---
subjects:
  governs: "CARRIES"
  depends_on:
    - "Carrier"
    - "Entity"
    - "Entity/Carrier"
    - "Relation"
    - "Artifact/Revision"
version: 14
updated_at: "2026-09-28 22:47:05 +0000"
relations: {}
atom_id: "CA-D-256"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-256-CORE_META_MODEL-CORE-DELIVERY--define-carries.md
---
# Summary

Define CARRIES

## Scope

Carrier bindings of non-ephemeral Entities.

## Claim

CARRIES **means** the directed Relation from a Carrier **to** the non-ephemeral Entity that it stores **or** represents.

## Details

- the inverse direction exposes the Entity/Carrier binding.
- **when** the carried Entity has Revisions, the binding identifies the exact carried Revision, such as an Artifact Revision.
- the applicable Carrier definition determines how the Entity is represented.
