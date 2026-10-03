---
atom_id: CA-R-1406
cce_version: cce_1
cce_form: prohibition
subjects:
  governs:
    continuant:
      - Entity/Identity
  depends_on:
    continuant:
      - Entity
      - CAPRMEDIO Graph
      - Projection
version: 2
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CA-R-1248
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1406-CORE_META_MODEL-CORE-REQUIREMENT--keep-entity-identity-independent-of-graph-materialization.md
---
# Keep Entity Identity Independent of Graph Materialization

materializing, refreshing, **or** deleting a Graph Projection **must not** establish, change, **or** remove Entity identity.
