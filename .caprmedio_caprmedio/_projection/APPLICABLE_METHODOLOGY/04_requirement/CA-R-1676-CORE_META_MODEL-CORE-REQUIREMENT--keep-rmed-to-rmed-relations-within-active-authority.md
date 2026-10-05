---
subjects:
  governs: "relation-model"
  depends_on:
    - "atom-boundary"
version: 20
updated_at: "2026-10-01 21:44:50 +0400"
relations:
  child_of:
    - CA-R-1051
atom_id: "CA-R-1676"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1676-CORE_META_MODEL-CORE-REQUIREMENT--keep-rmed-to-rmed-relations-within-active-authority.md
  source_atom_id: CA-R-1676
  source_atom_revision: 20
  source_sha256: c08978c43d93b0d8b0a04f10a9f2087d51ab1432431336ae169ab6e98e5cb275
  original_relations_sha256: fe61d145e2f5d262fb51b9ad7918a9f53aec7113df1dcdbd7cd1717f12d807c7
---
# Summary

Keep RMED-to-RMED Relations within Active Authority

## Scope

direct relations authored by Active RMED Atoms that target RMED Atoms.

## Claim

**if** a direct relation is authored by an Active Atom with Content Role **in** (Requirement, Method, Evaluation, Delivery) **and** targets an Atom with Content Role **in** (Requirement, Method, Evaluation, Delivery), **then** the target Atom **must** be Active.

## Details
