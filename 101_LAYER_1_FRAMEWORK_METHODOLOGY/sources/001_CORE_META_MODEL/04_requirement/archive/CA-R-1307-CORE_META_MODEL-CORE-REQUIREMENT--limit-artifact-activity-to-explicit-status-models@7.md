---
atom_id: CA-R-1307
cce_version: cce_1
cce_form: cardinality
subjects:
  governs: "Artifact/Activity"
  depends_on:
    - "Artifact"
    - "Artifact/Revision/Status"
version: 7
updated_at: "2026-09-16 23:48:40 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Limit Artifact Activity to explicit Status models

an Artifact **must** have **`=1`** Activity **in** (Active, Inactive) **if** an explicitly defined Status model applies **to** it, **and** **`=0`** Activity **otherwise**.
