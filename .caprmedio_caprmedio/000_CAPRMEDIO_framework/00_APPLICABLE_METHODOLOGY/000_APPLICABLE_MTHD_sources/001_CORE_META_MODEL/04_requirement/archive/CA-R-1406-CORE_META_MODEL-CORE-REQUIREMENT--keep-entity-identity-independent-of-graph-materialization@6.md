---
subjects:
  governs: "Entity/Identity"
  depends_on:
    - "Entity"
    - "CAPRMEDIO Graph"
    - "Projection"
version: 6
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CA-R-1248
---
# Keep Entity Identity Independent of Graph Materialization

materializing, refreshing, **or** deleting a Graph Projection **must not** establish, change, **or** remove Entity identity.
