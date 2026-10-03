---
subjects:
  governs: "project-containment graph"
  depends_on:
    - "Primary Entity"
    - "Artifact"
    - "Structural Entity"
version: 16
updated_at: "2026-10-02 20:52:00 +0400"
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
global_tier: 10
---
# Summary

Encode project-graph node partitions

## Scope

governed project-containment graph nodes.

## Claim

the project-containment graph **must** derive **`=1`** partition for **every** governed Primary Entity node from its Artifact **or** Structural Entity classification **and** reject a node whose partition count is **`!=1`**.

## Details
