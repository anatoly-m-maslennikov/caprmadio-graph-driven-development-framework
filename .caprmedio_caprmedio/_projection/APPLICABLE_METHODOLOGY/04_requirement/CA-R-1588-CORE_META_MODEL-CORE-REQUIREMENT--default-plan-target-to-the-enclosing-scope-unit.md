---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Claim/Target Scope Unit"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Claim/Target Scope Unit"
    - "Scope Unit"
    - "Hub Atom"
    - "Atom/Content Role: Plan/Type: Plan/Label"
version: 6
updated_at: "2026-10-03 00:40:46 +0400"
relations: {"relates_to": ["CA-R-1574", "CA-D-482"]}
atom_id: "CA-R-1588"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1588-CORE_META_MODEL-CORE-REQUIREMENT--default-plan-target-to-the-enclosing-scope-unit.md
  source_atom_id: CA-R-1588
  source_atom_revision: 6
  source_sha256: b621eba0c817ab1f581675b0f6b07fbd610f2c7133abcbb484855e425f85e248
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Default Plan target to the enclosing Scope Unit

## Scope

Plans with no separately selected Claim Target Scope Unit during authoring.

## Claim

during authoring, a Plan with no separately selected Claim Target Scope Unit **must** select its owning Scope Unit as the target, independently of decomposition **or** Label; a Hub does **not** become that default target. carry the resolved target under CA-D-482.

## Details
