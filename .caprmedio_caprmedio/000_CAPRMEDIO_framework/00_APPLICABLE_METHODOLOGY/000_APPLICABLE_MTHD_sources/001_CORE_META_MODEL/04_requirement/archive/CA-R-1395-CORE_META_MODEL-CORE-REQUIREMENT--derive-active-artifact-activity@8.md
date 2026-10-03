---
subjects:
  governs: "Artifact/Activity: Active"
  depends_on:
    - "Artifact/Activity"
    - "Artifact/Revision/Status"
version: 8
updated_at: "2026-09-11 02:13:22 +0400"
relations: {}
---
# Derive Active Artifact Activity

an Artifact's Activity **must** be Active **if** Activity applies under CA-R-1307, its current Revision has **`=1`** valid Status from the applicable explicitly defined Status model, **and** that Status **`=`** Active.
