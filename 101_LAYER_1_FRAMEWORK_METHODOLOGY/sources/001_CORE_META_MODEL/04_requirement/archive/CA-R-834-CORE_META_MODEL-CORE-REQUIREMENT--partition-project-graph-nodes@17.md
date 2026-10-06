---
subjects:
  governs: "project-containment graph"
  depends_on:
    - "Primary Entity"
    - "Artifact"
    - "Structural Entity"
version: 17
updated_at: 2026-09-07 09:59:57 +0000
relations:
  child_of:
    - "CA-R-1407"
atom_id: "CA-R-834"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 9
---
# Partition project-graph nodes

**every** Primary Entity node **in** the governed project-containment graph **must** belong **to** **`=1`** of the disjoint partitions Artifact **or** Structural Entity.
