---
subjects:
  governs: "relation-model"
  depends_on:
    - "atom-boundary"
version: 17
updated_at: "2026-10-02 21:01:00 +0400"
relations:
  child_of:
    - CA-R-913
atom_id: "CA-R-915"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-915-CORE_META_MODEL-CORE-REQUIREMENT--prohibit-order-derived-dependencies.md
  source_atom_id: CA-R-915
  source_atom_revision: 17
  source_sha256: 0b1c42d56318cc187ee18574919131d4d8d151ac6806074edcde63f1a5406a0c
  original_relations_sha256: 6f7d788a56b310c6a670268a37403be61a9ce286f37209823884838df0b22393
---
# Summary
Prohibit order-derived dependencies

## Scope

Dependencies between related Governed Entities.

## Claim

the Local Order of two Scope Units **or** the position of one canonical target reference **in** `relations.<RELATION_KIND>` **must not** establish **or** alter a dependency between related Governed Entities.

## Details
