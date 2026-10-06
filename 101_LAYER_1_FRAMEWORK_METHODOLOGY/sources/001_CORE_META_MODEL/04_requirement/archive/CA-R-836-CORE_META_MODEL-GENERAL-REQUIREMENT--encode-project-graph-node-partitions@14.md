---
subjects:
  governs: "project-containment graph"
  depends_on:
    - "Primary Entity"
    - "Artifact"
    - "Structural Entity"
version: 14
updated_at: "2026-09-10 07:15:17 +0400"
relations:
  child_of:
    - CA-R-834-CORE_META_MODEL-CORE-REQUIREMENT--partition-project-graph-nodes
---
# Encode project-graph node partitions

the project-containment graph **must** derive **`=1`** partition for **every** governed Primary Entity node from its Artifact **or** Structural Entity classification **and** reject a node whose partition count is **`!=1`**.
