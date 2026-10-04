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
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1657-CORE_META_MODEL-CORE-REQUIREMENT--require-acyclic-structural-ownership.md
---
# Summary

Require acyclic structural ownership

## Scope

the directed graph formed by active `structural_parent` relations.

## Claim

the directed graph formed by active `structural_parent` relations **must** be acyclic.

## Details
