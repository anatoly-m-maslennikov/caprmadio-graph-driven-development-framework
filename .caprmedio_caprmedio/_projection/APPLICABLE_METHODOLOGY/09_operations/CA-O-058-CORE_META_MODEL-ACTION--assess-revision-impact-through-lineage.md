---
subjects:
  governs: "Assess Lineage Impact"
  depends_on:
    - "Action"
    - "Atom"
    - "Artifact/Revision"
    - "Relation"
    - "Lineage Impact Analysis"
    - "Operator"
    - "AI Agent"
version: 6
updated_at: "2026-10-04 15:11:59 +0000"
relations: {"child_of":["CA-E-002"]}
atom_id: "CA-O-058"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-058-CORE_META_MODEL-ACTION--assess-revision-impact-through-lineage.md
  source_atom_id: CA-O-058
  source_atom_revision: 6
  source_sha256: 9a8d53c9f6d16a8a17675de50828fee6bf2e4bff15efc749cbecd0ed6857d22f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Assess revision impact through lineage

## Operation

Assess Lineage Impact **means** the reusable Action that assesses **every** reachable descendant lineage branch of **`=1`** changed Atom **until** **every** branch has an explicit impact disposition.

apply this Action **when** the Atom:

- receives a new accepted Revision;
- is replaced by a successor; **or**
- moves **to** the archive.

an Operator **or** AI Agent performs this Action within its existing authority. the assessment follows the existing lineage recursively; it does **not** create another cross-Scope Unit dependency graph.

## Details
