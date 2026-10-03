---
subjects:
  governs: "Artifact/Revision/Status: Archived"
  depends_on:
    - "Artifact/Revision"
    - "Artifact/Activity"
version: 8
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
atom_id: "CA-R-1419"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 9
---
# Restrict Archived Status to Non-Current Revisions

an Artifact Revision **may** have Status Archived **only** **if** it is a prior Revision **or** the final Revision of a replaced, absorbed, **or** retired Artifact.
