---
subjects:
  governs: "project-containment graph"
  depends_on:
    - "Primary Entity"
    - "Artifact"
    - "Structural Entity"
version: 18
updated_at: "2026-10-02 20:52:00 +0400"
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
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-834-CORE_META_MODEL-CORE-REQUIREMENT--partition-project-graph-nodes.md
---
# Summary

Partition project-graph nodes

## Scope

Primary Entity nodes **in** the governed project-containment graph.

## Claim

**every** Primary Entity node **in** the governed project-containment graph **must** belong **to** **`=1`** of the disjoint partitions Artifact **or** Structural Entity.

## Details
