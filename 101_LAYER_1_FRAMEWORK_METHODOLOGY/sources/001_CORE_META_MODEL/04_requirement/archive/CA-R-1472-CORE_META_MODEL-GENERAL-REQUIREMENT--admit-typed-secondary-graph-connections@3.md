---
subjects:
  governs: "CAPRMEDIO Graph/Connectivity"
  depends_on:
    - "CAPRMEDIO Graph"
    - "Projection"
    - "Atom"
    - "Structural Entity"
    - "Journal"
    - "Relation"
    - "Relation Kind"
    - "Relation Kind/Metadata"
version: 3
updated_at: "2026-09-15 01:47:49 +0400"
relations: {}
---
# Admit typed secondary graph connections

a secondary CAPRMEDIO Graph **may** represent typed Relations between its own nodes, **to** another secondary graph **or** its nodes, **and** **to** source Atoms **or** other admitted authoritative sources.

**every** connection **must** use **`=1`** graph-qualified Relation Kind whose governing authority admits its endpoint classes, endpoint graph contexts, direction, **and** cardinality. crossing a graph boundary **must not** transfer Relation Kind ownership, import a foreign Relation Kind as native, **or** make a referenced external endpoint a native node of the receiving graph. a cross-graph reference preserves the referenced identity **without** copying its source fact into independent authority. these permissions do **not** admit concrete Relation Kinds **or** authorize inference beyond their declared rules.
