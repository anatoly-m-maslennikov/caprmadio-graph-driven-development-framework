---
subjects:
  governs: "Methodology Source/Expansion Boundary"
  depends_on:
    - "Core Meta-Model"
    - "Extension"
    - "Project Configuration"
    - "Atom/Claim"
    - "Framework Instance Settings"
version: 13
updated_at: "2026-10-02 22:23:29 +0400"
relations: {}
atom_id: "CA-R-1375"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1375-CORE_META_MODEL-CORE--restrict-methodology-source-expansion-to-core-permission.md
  source_atom_id: CA-R-1375
  source_atom_revision: 13
  source_sha256: 2c4a97c2d4c6c054ac8e5318641aa9e8e71c7627b37a32cd66885690ca132d75
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Restrict Methodology Source Expansion to Core Permission

## Scope

Methodology source expansion by an Extension **or** Project Configuration.

## Claim

an Extension **or** Project Configuration **must** add Claims, Terms, allowed values, Types, Methods, Evaluations, Deliveries, Operations, activation rules, compatibility rules, **or** priority rules **only** **where** one active CORE_META_MODEL Atom permits the addition **and** **must not** redefine, replace, shadow, weaken, delete, contradict, reinterpret, **or** mutate Core Meta-Model authority at **any** Local Tier; a higher-ranked local Claim grants no exception **to** this source authority boundary.

## Details

current Extension activation **and** selected Extension Revisions remain owned by Framework Instance Settings under CA-R-1207. permission **to** add a rule does **not** duplicate **or** transfer ownership of its current selection.
