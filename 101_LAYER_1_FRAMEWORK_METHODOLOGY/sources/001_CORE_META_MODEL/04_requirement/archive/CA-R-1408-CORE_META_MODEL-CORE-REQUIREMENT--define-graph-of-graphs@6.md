---
subjects:
  governs: "Graph of Graphs"
  depends_on:
    - "CAPRMEDIO Graph"
    - "Projection"
    - "Relation"
    - "Relation Kind"
    - "Single Source of Truth"
version: 6
updated_at: "2026-09-15 01:47:49 +0400"
relations: {}
atom_id: "CA-R-1408"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Define Graph of Graphs

a Graph of Graphs **means** a composition of CAPRMEDIO Graphs connected through graph-qualified typed references **or** shared source identities. secondary graphs **in** this composition remain Projections under CA-R-1471, **and** their internal, cross-graph, **and** authoritative-source connections remain governed by CA-R-1472.

the composition does **not**, by itself, require another separately generated overview Artifact. **if** an overview is generated, its represented connections remain derived from the participating graphs **and** their sources **without** becoming another authority.
