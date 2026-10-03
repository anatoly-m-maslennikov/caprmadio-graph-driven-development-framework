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
version: 1
updated_at: 2026-09-04 14:07:21 +0400
relations:
  child_of:
    - CA-R-1248
---
# Keep Entity Identity Independent of Graph Materialization

materializing, refreshing, **or** deleting a Graph Projection **must not** establish, change, **or** remove Entity identity.
