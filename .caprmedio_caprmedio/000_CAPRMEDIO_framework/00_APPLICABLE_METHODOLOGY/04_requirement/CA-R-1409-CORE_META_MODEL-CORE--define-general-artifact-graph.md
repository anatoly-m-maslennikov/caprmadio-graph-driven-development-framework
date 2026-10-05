---
subjects:
  governs: "General Artifact Graph"
  depends_on:
    - "Artifact"
    - "Structural Entity"
    - "Scope Unit"
    - "Atom Collection"
    - "Carrier"
    - "CAPRMEDIO Graph"
    - "Structural Entity/Direct Containment"
    - "Atom"
    - "Journal"
    - "Projection"
version: 8
updated_at: "2026-10-02 22:41:14 +0400"
relations: {}
atom_id: "CA-R-1409"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1409-CORE_META_MODEL-CORE--define-general-artifact-graph.md
  source_atom_id: CA-R-1409
  source_atom_revision: 8
  source_sha256: 3a076773130957430f7c9ee585d8199643cb83edba9e90d60b049ce3d0880069
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define General Artifact Graph

## Scope

the General Artifact Graph and its represented governed Artifacts and Structural Entities.

## Claim

a General Artifact Graph **means** the derived CAPRMEDIO Graph that represents governed Artifacts **and** Structural Entities as nodes, locates them by their authoritative Carriers, **and** connects them through the existing direct containment relations. its Structural Entity nodes include Scope Units **and** Atom Collections; its Artifact nodes include Atoms, Journals, **and** Projections.

node identities, Carrier locations, **and** containment come from existing authoritative sources **and** registered containment rules, **not** independently maintained graph declarations. an administrative directory does **not** become a Structural Entity merely because it is a folder. the graph provides their shared structural context **without** duplicating specialized graphs **or** becoming a separate source of authority.

## Details
