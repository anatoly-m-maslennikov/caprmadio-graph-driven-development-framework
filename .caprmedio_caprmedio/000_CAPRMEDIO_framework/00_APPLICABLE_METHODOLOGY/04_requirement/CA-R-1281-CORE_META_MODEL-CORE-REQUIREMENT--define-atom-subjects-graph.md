---
subjects:
  governs: "Projection/Type: Atom Subjects Graph"
  depends_on:
    - "Projection"
    - "Atom"
    - "Atom/Subjects"
    - "Subject Path"
    - "Entity"
    - "GOVERNS"
    - "DEPENDS_ON"
    - "Relation"
    - "Relation Kind"
    - "CAPRMEDIO Graph"
    - "Artifact/Revision"
    - "Subject"
    - "Term"
version: 12
updated_at: "2026-10-02 21:52:05 +0400"
relations: {}
atom_id: "CA-R-1281"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1281-CORE_META_MODEL-CORE-REQUIREMENT--define-atom-subjects-graph.md
  source_atom_id: CA-R-1281
  source_atom_revision: 12
  source_sha256: 7630a993ef9c9f370f0c8e56a5721ae6cb5589ad643beb35f78fecb6ad67dfcc
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Atom Subjects Graph

## Scope

Atom Subjects Graph Type values under Projection.

## Claim

Atom Subjects Graph **means** the Type value under Projection whose instances are non-authoritative CAPRMEDIO Graphs derived from selected current Atom Subjects, with Atom nodes linked by direct GOVERNS **and** DEPENDS_ON Subject Relations **to** their canonical Entity target nodes. the Subjects are the links, **not** the target nodes **or** intermediate Subject nodes.

## Details

**every** represented link retains the source Atom identity, exact Subject Path, canonical target identity, Relation Kind, direction, **and** source Artifact Revision. its Relation Kinds **and** endpoint constraints remain governed by their existing graph-qualified authority; naming this Projection Type does **not** admit another Relation Kind owner **or** an independently authored relation fact. represented targets retain their Entity identities **without** an intermediate Subject object **or** duplicated target definitions.
