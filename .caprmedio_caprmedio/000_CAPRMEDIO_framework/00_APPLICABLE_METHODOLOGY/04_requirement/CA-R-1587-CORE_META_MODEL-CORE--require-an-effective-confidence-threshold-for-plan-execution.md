---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Autonomous Confidence Threshold"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Autonomous Confidence Threshold"
    - "Operator"
    - "Framework Instance Settings"
version: 4
updated_at: "2026-10-03 00:40:46 +0400"
relations: {"relates_to": ["CA-M-271", "CA-R-1044"]}
atom_id: "CA-R-1587"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1587-CORE_META_MODEL-CORE--require-an-effective-confidence-threshold-for-plan-execution.md
  source_atom_id: CA-R-1587
  source_atom_revision: 4
  source_sha256: e2c13e07ba539b05959868169d761d18746b26e583abbccde1d55b1ee64b4523
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Require an effective confidence threshold for Plan execution

## Scope

autonomous Plan execution decisions.

## Claim

**every** autonomous Plan execution decision **must** resolve **=1** effective Autonomous Confidence Threshold from its applicable explicit **or** inherited source under CA-M-271.

## Details
