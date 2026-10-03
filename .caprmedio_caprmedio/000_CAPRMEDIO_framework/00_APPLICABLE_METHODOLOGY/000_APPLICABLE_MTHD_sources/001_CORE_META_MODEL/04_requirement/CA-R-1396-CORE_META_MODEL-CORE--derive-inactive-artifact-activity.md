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
---
# Summary

Derive Inactive Artifact Activity

## Scope

Artifacts for which Activity applies.

## Claim

an Artifact's Activity **must** be Inactive **if** Activity applies under CA-R-1307, its current Revision has **`=1`** valid Status from the applicable explicitly defined Status model, **and** that Status **`!=`** Active.

## Details
