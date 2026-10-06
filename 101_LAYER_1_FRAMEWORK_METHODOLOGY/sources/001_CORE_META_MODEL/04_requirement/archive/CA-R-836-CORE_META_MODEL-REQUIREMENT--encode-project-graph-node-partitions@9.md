---
cce_version: cce_1
cce_form: obligation
atom_id: CA-R-836
subjects:
  governs:
    continuant:
      - project-containment graph
  depends_on:
    continuant:
      - Primary Entity
      - Artifact
      - Structural Entity
version: 9
updated_at: 2026-09-07 09:59:57 +0000
relations:
  child_of:
    - CA-R-834-CORE_META_MODEL-CORE-REQUIREMENT--partition-project-graph-nodes
---
# Encode project-graph node partitions

the project-containment graph **must** derive **`=1`** partition for **every** governed Primary Entity node from its Artifact **or** Structural Entity classification **and** reject a node whose partition count is **`!=1`**.
