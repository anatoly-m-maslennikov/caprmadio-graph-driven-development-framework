---
subjects:
  governs: "requirement-topology"
  depends_on: []
version: 16
updated_at: "2026-10-03 01:51:15 +0400"
relations:
  child_of:
    - CAPRMEDIO-REQU-037-REQUIREMENT--require-parent-coverage-without-claiming-topology-completeness
    - "CA-R-1767"
atom_id: "CA-R-1671"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1671-CORE_META_MODEL-REQUIREMENT--permit-orphan-implementation-decisions.md
  source_atom_id: CA-R-1671
  source_atom_revision: 16
  source_sha256: 021856089fca024124250c3bd2519f3037b7d993d9719db07d026af9c5cfb5d1
  original_relations_sha256: fce039eb6fcf49a774bafbc3997d585ccfddedd08c2eb207f8d2ec7578da9892
---
# Summary

Permit orphan Implementation Decisions

## Scope

orphan permission for an active Implementation Decision in strict authority mode.

## Claim

`implementation_decision` **must** be registered as orphan-permitted, so an active Implementation Decision **may** have no parent Implementation Method even **in** strict authority mode.

## Details
