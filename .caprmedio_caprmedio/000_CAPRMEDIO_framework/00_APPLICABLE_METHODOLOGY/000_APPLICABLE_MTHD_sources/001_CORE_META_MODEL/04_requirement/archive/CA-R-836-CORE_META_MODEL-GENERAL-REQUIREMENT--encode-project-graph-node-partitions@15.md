---
subjects:
  governs: "project-containment graph"
  depends_on:
    - "Primary Entity"
    - "Artifact"
    - "Structural Entity"
version: 15
updated_at: "2026-09-10 07:15:17 +0400"
relations:
  child_of:
    - CA-R-834-CORE_META_MODEL-CORE-REQUIREMENT--partition-project-graph-nodes
atom_id: "CA-R-836"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Encode project-graph node partitions

the project-containment graph **must** derive **`=1`** partition for **every** governed Primary Entity node from its Artifact **or** Structural Entity classification **and** reject a node whose partition count is **`!=1`**.
