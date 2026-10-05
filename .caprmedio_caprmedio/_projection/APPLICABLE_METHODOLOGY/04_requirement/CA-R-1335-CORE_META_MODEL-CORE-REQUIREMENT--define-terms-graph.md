---
subjects:
  governs: "Projection/Type: Terms Graph"
  depends_on:
    - "Projection"
    - "Term"
    - "Relation Kind"
    - "Relation"
    - "CAPRMEDIO Graph"
version: 13
updated_at: "2026-10-02 22:05:04 +0400"
relations: {}
atom_id: "CA-R-1335"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1335-CORE_META_MODEL-CORE-REQUIREMENT--define-terms-graph.md
  source_atom_id: CA-R-1335
  source_atom_revision: 13
  source_sha256: 98ef6a5058ada19dd51563545a1c3ad46e8b18a637305dce90dde15eb5bfddf1
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Terms Graph

## Scope

Terms Graph projections **and** their represented graph facts.

## Claim

Terms Graph **means** the Type value under Projection whose instances are derived CAPRMEDIO Graphs with native Term nodes **and** edges representing Relations admitted for that graph kind by their governing authority. their represented facts retain their appropriate source authority under CA-R-1746.

## Details

admitted external graph **or** source references under CA-R-1472 do **not** become native Term nodes merely by being referenced. those references retain their own endpoint classes **and** graph-qualified Relation authority.
