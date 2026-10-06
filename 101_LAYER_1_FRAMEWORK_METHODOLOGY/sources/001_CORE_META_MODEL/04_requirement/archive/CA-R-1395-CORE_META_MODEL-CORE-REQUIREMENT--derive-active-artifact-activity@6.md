---
atom_id: CA-R-1395
cce_version: cce_1
cce_form: conditional
subjects:
  governs: "Artifact/Activity: Active"
  depends_on:
    - "Artifact/Activity"
    - "Artifact/Revision/Status"
version: 6
updated_at: "2026-09-11 02:13:22 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Derive Active Artifact Activity

an Artifact's Activity **must** be Active **if** Activity applies under CA-R-1307, its current Revision has **`=1`** valid Status from the applicable explicitly defined Status model, **and** that Status **`=`** Active.
