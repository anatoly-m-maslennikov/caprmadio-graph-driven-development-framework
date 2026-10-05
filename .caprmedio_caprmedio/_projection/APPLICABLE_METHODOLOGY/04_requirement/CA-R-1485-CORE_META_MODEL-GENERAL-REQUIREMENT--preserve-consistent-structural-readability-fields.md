---
subjects:
  governs: "Project Structure"
  depends_on:
    - "Scope Unit"
    - "Structural Parent Relation"
    - "Structural Level"
    - "Navigational Order Number"
    - "Carrier"
version: 5
updated_at: "2026-10-02 23:35:16 +0400"
relations: {}
atom_id: "CA-R-1485"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1485-CORE_META_MODEL-GENERAL-REQUIREMENT--preserve-consistent-structural-readability-fields.md
  source_atom_id: CA-R-1485
  source_atom_revision: 5
  source_sha256: e58b909c4ef55a69b3426e23e936c0fd4bc2d63f17714e206581e8a3e22b1e4c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Preserve consistent structural readability fields

## Scope

derived structural readability representations retained by a Project Structure.

## Claim

Project Structure **may** retain derived structural representations for readability **only** **when** their authoritative inputs **and** consistency constraints are explicit. retained Structural Level **must** **`=`** declared parent depth from Project level **`0`**; a retained authority path **must** satisfy applicable Carrier naming **and** placement rules, including admitted exceptions. inconsistent representations **must** produce a reported conflict **without** an automatic choice of a new Name, parent, order, **or** binding. readability does **not** establish another source of authority.

## Details
