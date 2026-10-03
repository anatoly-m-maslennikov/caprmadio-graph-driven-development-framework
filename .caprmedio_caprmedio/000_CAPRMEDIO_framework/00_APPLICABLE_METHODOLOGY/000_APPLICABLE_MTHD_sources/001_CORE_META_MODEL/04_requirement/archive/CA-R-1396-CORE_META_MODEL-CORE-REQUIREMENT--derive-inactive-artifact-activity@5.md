---
atom_id: CA-R-1396
cce_version: cce_1
cce_form: conditional
subjects:
  governs: "Artifact/Activity: Inactive"
  depends_on:
    - "Artifact/Activity"
    - "Artifact/Revision/Status"
version: 5
updated_at: "2026-09-16 23:48:40 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Derive Inactive Artifact Activity

an Artifact's Activity **must** be Inactive **if** Activity applies under CA-R-1307, its current Revision has **`=1`** valid Status from the applicable explicitly defined Status model, **and** that Status **`!=`** Active.
