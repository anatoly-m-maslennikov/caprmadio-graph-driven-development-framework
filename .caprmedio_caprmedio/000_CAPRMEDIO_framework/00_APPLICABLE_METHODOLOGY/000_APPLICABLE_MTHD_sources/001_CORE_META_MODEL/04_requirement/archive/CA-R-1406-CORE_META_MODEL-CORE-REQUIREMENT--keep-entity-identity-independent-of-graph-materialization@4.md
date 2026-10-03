---
atom_id: CA-R-1406
cce_version: cce_1
cce_form: prohibition
subjects:
  governs: "Entity/Identity"
  depends_on:
    - "Entity"
    - "CAPRMEDIO Graph"
    - "Projection"
version: 4
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CA-R-1248
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Keep Entity Identity Independent of Graph Materialization

materializing, refreshing, **or** deleting a Graph Projection **must not** establish, change, **or** remove Entity identity.
