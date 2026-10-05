---
subjects:
  governs: "Atom/Content Role: Requirement/Type: Demand/Direction"
  depends_on:
    - "Atom/Scope"
    - "Atom/Claim/Target Scope Unit"
version: 15
updated_at: "2026-10-02 21:52:05 +0400"
relations: {}
atom_id: "CA-R-1294"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1294-CORE_META_MODEL-CORE-REQUIREMENT--derive-demand-direction-without-another-relation-kind.md
  source_atom_id: CA-R-1294
  source_atom_revision: 15
  source_sha256: 1a4fb4af2ce6389a6545c2e29a7958d8f7eb9807772ceaf60c627728828ecc01
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Derive Demand Direction without Another Relation Kind

## Scope

Demand Atom directions.

## Claim

a Demand Atom **must not** introduce a graph Relation Kind for its direction because its Consumer Atom Scope Unit **and** Producer Claim Target Scope Unit references determine that direction.

## Details
