---
subjects:
  governs: "Artifact/Activity"
  depends_on:
    - "Artifact"
    - "Artifact/Revision/Status"
version: 12
updated_at: "2026-10-02 21:52:05 +0400"
relations: {}
atom_id: "CA-R-1307"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Limit Artifact Activity to explicit Status models

## Scope

Artifacts to which explicitly defined Status models apply.

## Claim

an Artifact **must** have **`=1`** Activity **in** (Active, Inactive) **if** an explicitly defined Status model applies **to** it, **and** **`=0`** Activity **otherwise**.

## Details
