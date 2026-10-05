---
subjects:
  governs: "relation-model"
  depends_on:
    - "atom-boundary"
version: 17
updated_at: "2026-10-03 01:43:25 +0400"
relations:
  child_of:
    - CA-R-1756
atom_id: "CA-R-1659"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1659-CORE_META_MODEL-REQUIREMENT--derive-inverse-structural-ownership.md
  source_atom_id: CA-R-1659
  source_atom_revision: 17
  source_sha256: d693f0772b0a5e8f2cab511e0aa15fc4472d815ab97cd71869fd3935d9bb9a0c
  original_relations_sha256: 0ba2502dcab70b9da25a5744a2bab269022fa8dd08fb0b792c5596652adf2fc1
---
# Summary

Derive inverse structural ownership

## Scope

the inverse `structural_children` view derived from stored `structural_parent` relations.

## Claim

CAPRMEDIO **must** derive the inverse `structural_children` view from stored `structural_parent` relations **and** **must not** persist that inverse separately.

## Details
