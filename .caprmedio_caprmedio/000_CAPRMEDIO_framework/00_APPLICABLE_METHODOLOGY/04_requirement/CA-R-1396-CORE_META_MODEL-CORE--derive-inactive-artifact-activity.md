---
subjects:
  governs: "Artifact/Activity: Inactive"
  depends_on:
    - "Artifact/Activity"
    - "Artifact/Revision/Status"
version: 10
updated_at: "2026-10-02 22:41:14 +0400"
relations: {}
atom_id: "CA-R-1396"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1396-CORE_META_MODEL-CORE--derive-inactive-artifact-activity.md
  source_atom_id: CA-R-1396
  source_atom_revision: 10
  source_sha256: 683c9054bbab9d98fa980f496267f7195fc7158487a8c59944203b12970c8f3c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Derive Inactive Artifact Activity

## Scope

Artifacts for which Activity applies.

## Claim

an Artifact's Activity **must** be Inactive **if** Activity applies under CA-R-1307, its current Revision has **`=1`** valid Status from the applicable explicitly defined Status model, **and** that Status **`!=`** Active.

## Details
