---
subjects:
  governs: "Artifact/Activity: Active"
  depends_on:
    - "Artifact/Activity"
    - "Artifact/Revision/Status"
version: 10
updated_at: "2026-10-02 22:50:34 +0400"
relations: {}
atom_id: "CA-R-1395"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1395-CORE_META_MODEL-CORE--derive-active-artifact-activity.md
  source_atom_id: CA-R-1395
  source_atom_revision: 10
  source_sha256: 9491c0a5c6b7c2b3c51f593941b3bf6e2430c82b59027cb36bf0b7610401a1b0
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Derive Active Artifact Activity

## Scope

Artifacts for which Activity applies.

## Claim

an Artifact's Activity **must** be Active **if** Activity applies under CA-R-1307-CORE_META_MODEL-CORE-REQUIREMENT--limit-artifact-activity-to-explicit-status-models, its current Revision has **`=1`** valid Status from the applicable explicitly defined Status model, **and** that Status **`=`** Active.

## Details
