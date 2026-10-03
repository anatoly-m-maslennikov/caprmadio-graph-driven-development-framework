---
cce_version: cce_1
cce_form: obligation
atom_id: CA-R-836
subjects:
  governs: "project-containment graph"
  depends_on:
    - "Primary Entity"
    - "Artifact"
    - "Structural Entity"
version: 12
updated_at: "2026-09-10 07:15:17 +0400"
relations:
  child_of:
    - CA-R-834-CORE_META_MODEL-CORE-REQUIREMENT--partition-project-graph-nodes
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Encode project-graph node partitions

the project-containment graph **must** derive **`=1`** partition for **every** governed Primary Entity node from its Artifact **or** Structural Entity classification **and** reject a node whose partition count is **`!=1`**.
