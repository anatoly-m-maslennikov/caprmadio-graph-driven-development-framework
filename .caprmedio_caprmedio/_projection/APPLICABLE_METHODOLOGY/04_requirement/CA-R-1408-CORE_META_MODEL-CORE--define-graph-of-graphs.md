---
subjects:
  governs: "Graph of Graphs"
  depends_on:
    - "CAPRMEDIO Graph"
    - "Projection"
    - "Relation"
    - "Relation Kind"
    - "Single Source of Truth"
version: 7
updated_at: "2026-10-02 22:41:14 +0400"
relations: {}
atom_id: "CA-R-1408"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1408-CORE_META_MODEL-CORE--define-graph-of-graphs.md
  source_atom_id: CA-R-1408
  source_atom_revision: 7
  source_sha256: 62e1b2247723aebb08fa4c3a4a32acd208fbb58f38031ab2117c66726545d12b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Graph of Graphs

## Scope

Graph of Graphs compositions and any generated overview Artifact.

## Claim

a Graph of Graphs **means** a composition of CAPRMEDIO Graphs connected through graph-qualified typed references **or** shared source identities. secondary graphs **in** this composition remain Projections under CA-R-1471-CORE_META_MODEL-CORE-REQUIREMENT--keep-secondary-graphs-derived-from-source-authority, **and** their internal, cross-graph, **and** authoritative-source connections remain governed by CA-R-1472-CORE_META_MODEL-GENERAL-REQUIREMENT--admit-typed-secondary-graph-connections.

the composition does **not**, by itself, require another separately generated overview Artifact. **if** an overview is generated, its represented connections remain derived from the participating graphs **and** their sources **without** becoming another authority.

## Details
