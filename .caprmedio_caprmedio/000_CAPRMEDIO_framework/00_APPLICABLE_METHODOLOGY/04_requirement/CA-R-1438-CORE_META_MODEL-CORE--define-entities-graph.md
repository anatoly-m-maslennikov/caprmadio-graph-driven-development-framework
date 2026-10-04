---
subjects:
  governs: "Projection/Type: Entities Graph"
  depends_on:
    - "Projection"
    - "Entity"
    - "Relation Kind"
    - "Relation"
    - "CAPRMEDIO Graph"
version: 8
updated_at: "2026-10-02 22:59:46 +0400"
relations: {}
atom_id: "CA-R-1438"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1438-CORE_META_MODEL-CORE--define-entities-graph.md
---
# Summary

Define Entities Graph

## Scope

the Entities Graph Type value under Projection.

## Claim

Entities Graph **means** the Type value under Projection whose instances are derived CAPRMEDIO Graphs with native Entity nodes **and** edges representing Relations admitted for that graph kind by their governing authority. their represented facts retain their appropriate source authority under CA-R-1746.

admitted external graph **or** source references under CA-R-1472 do **not** become native Entity nodes merely by being referenced. those references retain their own endpoint classes **and** graph-qualified Relation authority.

## Details
