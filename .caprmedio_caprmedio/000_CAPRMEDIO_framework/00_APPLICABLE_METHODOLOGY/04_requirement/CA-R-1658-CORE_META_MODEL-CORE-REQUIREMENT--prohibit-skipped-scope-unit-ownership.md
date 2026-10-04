---
subjects:
  governs: "scope-topology"
  depends_on:
    - "authority"
version: 17
updated_at: "2026-10-03 01:42:39 +0400"
relations: {}
atom_id: "CA-R-1658"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1658-CORE_META_MODEL-CORE-REQUIREMENT--prohibit-skipped-scope-unit-ownership.md
---
# Summary

Prohibit skipped Scope Unit ownership

## Scope

Scope Unit ownership through a stored structural-parent relation.

## Claim

a Scope Unit **must not** own a descendant Scope Unit through a stored structural-parent relation **when** another active Scope Unit lies between them.

## Details
