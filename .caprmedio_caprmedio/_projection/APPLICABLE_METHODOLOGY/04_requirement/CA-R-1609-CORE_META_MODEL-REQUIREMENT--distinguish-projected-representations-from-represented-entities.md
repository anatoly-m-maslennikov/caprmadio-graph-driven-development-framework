---
atom_id: CA-R-1609
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Projection"
  depends_on:
    - "Artifact"
    - "Entity"
    - "Scope Unit"
    - "Single Source of Truth"
version: 4
updated_at: "2026-10-03 00:55:03 +0400"
relations:
  relates_to:
    - CA-R-1470
    - CA-R-1568
    - CA-R-1746
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1609-CORE_META_MODEL-REQUIREMENT--distinguish-projected-representations-from-represented-entities.md
  source_atom_id: CA-R-1609
  source_atom_revision: 4
  source_sha256: 70e09266435f444236b0bb9769bd0103dd9a046b431902290a2a877dc6c173e8
  original_relations_sha256: 9530390b47050763ac35ad602a83916c10c7411ed485e78f67196c63606fcd2a
---
# Summary

Distinguish projected representations from represented Entities

## Scope

Representations inside a Projection and the Entities they represent.

## Claim

a representation inside a Projection **must** remain distinct from the Entity it represents.

- depicting an existing Artifact **or** Scope Unit does **not** create another authoritative Artifact **or** Scope Unit.
- a representation **may** identify a source Entity **or** a derived element admitted by the Projection specification; source identities **and** traceability remain governed by CA-R-1746.
- this boundary introduces no separate Projection Element Term, lifecycle, **or** independently maintained authority.

## Details
