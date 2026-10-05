---
subjects:
  governs: "Project/normative authority graph"
  depends_on:
    - "Project"
    - "Relation"
    - "Normative Authority Relation Pair"
version: 5
updated_at: "2026-10-02 20:16:06 +0400"
relations: {"evaluation_for":["CA-R-833","CA-R-808","CA-R-879"]}
atom_id: "CA-E-481"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 10
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-481-CORE_META_MODEL-GENERAL-EVALUATION_APPROACH--validate-the-normative-authority-hierarchy.md
  source_atom_id: CA-E-481
  source_atom_revision: 5
  source_sha256: b1a06f071e884ebc30afade384f08d25f228f4730ff705def5b7a60f98cfdd71
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Validate the normative-authority hierarchy

## Scope

the active normative-authority subgraph.

## Claim

the Evaluation of the active normative-authority subgraph **must** fail **when** **any** declared authority-bearing direct edge lacks its registered typing **or** the directed subgraph **contains** a cycle under CA-R-833.

## Details

- the evaluated input is the active normative-authority subgraph selected under its registered direct Relation types. unresolved selection **or** typing **must not** be reported as a conforming hierarchy.
- retain the distinction between declared direct authority edges **and** inverse-derived views under CA-R-808 **and** CA-R-879. an inverse view **must not** become another independently declared edge **in** the cycle check.

this representation-independent criterion does **not** select a graph-construction implementation **or** a concrete test specimen.
