---
cce_version: "cce_1"
cce_form: "obligation"
subjects:
  governs: "project-containment graph"
  depends_on:
    - "Primary Entity"
    - "Artifact"
    - "Structural Entity"
version: 14
updated_at: 2026-09-07 09:59:57 +0000
relations:
  child_of:
    - "CA-R-1407"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Partition project-graph nodes

**every** Primary Entity node **in** the governed project-containment graph **must** belong **to** **`=1`** of the disjoint partitions Artifact **or** Structural Entity.
