---
subjects:
  governs: "Entity/Identity"
  depends_on:
    - "Entity"
    - "CAPRMEDIO Graph"
    - "Projection"
version: 9
updated_at: "2026-10-02 22:41:14 +0400"
relations:
  child_of:
    - CA-R-1248
atom_id: "CA-R-1406"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1406-CORE_META_MODEL-CORE--keep-entity-identity-independent-of-graph-materialization.md
  source_atom_id: CA-R-1406
  source_atom_revision: 9
  source_sha256: 9f02a3b4585c3c9debced436702c083bf7b4d626d1c28705783d63cb303b8898
  original_relations_sha256: 0f1e5f7c7498d6b33c2ed22fb4783b2833b7862d1dd85cabba8ed0441099db31
---
# Summary

Keep Entity Identity Independent of Graph Materialization

## Scope

Entity identity while a Graph Projection is materialized, refreshed, or deleted.

## Claim

materializing, refreshing, **or** deleting a Graph Projection **must not** establish, change, **or** remove Entity identity.

## Details
