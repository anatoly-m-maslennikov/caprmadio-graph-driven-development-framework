---
atom_id: CA-R-1396
cce_version: cce_1
cce_form: conditional
subjects:
  governs:
    continuant:
      - "Artifact/Activity: Inactive"
  depends_on:
    continuant:
      - Artifact/Activity
      - Artifact/Revision/Status
version: 4
updated_at: "2026-09-11 02:13:22 +0400"
relations: {}
---
# Derive Inactive Artifact Activity

an Artifact's Activity **must** be Inactive **if** Activity applies under CA-R-1307, its current Revision has **`=1`** valid Status from the applicable explicitly defined Status model, **and** that Status **`!=`** Active.
