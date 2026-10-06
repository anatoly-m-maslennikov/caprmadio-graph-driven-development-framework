---
atom_id: CA-R-1408
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Graph of Graphs"
  depends_on:
    - "CAPRMEDIO Graph"
    - "Projection"
    - "Relation"
    - "Relation Kind"
    - "Single Source of Truth"
version: 3
updated_at: "2026-09-15 01:47:49 +0400"
relations: {}
---
# Define Graph of Graphs

a Graph of Graphs **means** a composition of CAPRMEDIO Graphs connected through graph-qualified typed references **or** shared source identities. secondary graphs **in** this composition remain Projections under CA-R-1471, **and** their internal, cross-graph, **and** authoritative-source connections remain governed by CA-R-1472.

the composition does **not**, by itself, require another separately generated overview Artifact. **if** an overview is generated, its represented connections remain derived from the participating graphs **and** their sources **without** becoming another authority.
