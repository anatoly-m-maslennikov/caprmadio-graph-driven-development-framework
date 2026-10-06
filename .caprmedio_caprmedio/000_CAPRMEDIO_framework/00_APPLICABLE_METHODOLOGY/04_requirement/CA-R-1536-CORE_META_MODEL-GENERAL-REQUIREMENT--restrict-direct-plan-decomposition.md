---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Decomposition"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
version: 5
updated_at: "2026-10-03 00:05:13 +0400"
relations: {"relates_to": ["CA-R-1576", "CA-R-1579", "CA-R-1590"]}
atom_id: "CA-R-1536"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1536-CORE_META_MODEL-GENERAL-REQUIREMENT--restrict-direct-plan-decomposition.md
  source_atom_id: CA-R-1536
  source_atom_revision: 5
  source_sha256: c7804dc0ef3ba6b3a1439203182b33aa21e83d84d82e7a1c84cc5da37590044a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Restrict Direct Plan Decomposition

## Scope

direct `DECOMPOSES_INTO` relations between Plan Atoms.

## Claim

`DECOMPOSES_INTO` **must** connect **only** distinct Plan Atoms; **any** Plan **may** decompose into other Plans regardless of their Labels, **without** requiring incoming decomposition.

## Details
