---
subjects:
  governs: "relation-model"
  depends_on:
    - "atom-boundary"
version: 18
updated_at: "2026-10-03 01:42:14 +0400"
relations: {}
atom_id: "CA-R-1657"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1657-CORE_META_MODEL-CORE-REQUIREMENT--require-acyclic-structural-ownership.md
  source_atom_id: CA-R-1657
  source_atom_revision: 18
  source_sha256: e20f9b5f022621de57a7efe519c5ebbf24a6e69d4f4aa4ce70516b2a2ce6b468
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Require acyclic structural ownership

## Scope

the directed graph formed by active `structural_parent` relations.

## Claim

the directed graph formed by active `structural_parent` relations **must** be acyclic.

## Details
