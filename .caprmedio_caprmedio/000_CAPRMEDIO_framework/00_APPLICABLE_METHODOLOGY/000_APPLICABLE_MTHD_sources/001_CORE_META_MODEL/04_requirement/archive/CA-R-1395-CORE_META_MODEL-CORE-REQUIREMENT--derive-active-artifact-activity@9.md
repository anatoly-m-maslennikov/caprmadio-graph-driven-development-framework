---
subjects:
  governs: "Artifact/Activity: Active"
  depends_on:
    - "Artifact/Activity"
    - "Artifact/Revision/Status"
version: 9
updated_at: "2026-09-11 02:13:22 +0400"
relations: {}
atom_id: "CA-R-1395"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Derive Active Artifact Activity

an Artifact's Activity **must** be Active **if** Activity applies under CA-R-1307, its current Revision has **`=1`** valid Status from the applicable explicitly defined Status model, **and** that Status **`=`** Active.
