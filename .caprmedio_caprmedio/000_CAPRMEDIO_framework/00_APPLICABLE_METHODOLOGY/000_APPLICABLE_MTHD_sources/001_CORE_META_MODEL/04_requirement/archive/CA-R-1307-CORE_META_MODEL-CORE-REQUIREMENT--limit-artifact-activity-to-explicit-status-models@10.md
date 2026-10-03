---
subjects:
  governs: "Artifact/Activity"
  depends_on:
    - "Artifact"
    - "Artifact/Revision/Status"
version: 10
updated_at: "2026-09-11 02:13:22 +0400"
relations: {}
---
# Limit Artifact Activity to explicit Status models

an Artifact **must** have **`=1`** Activity **in** (Active, Inactive) **if** an explicitly defined Status model applies **to** it, **and** **`=0`** Activity **otherwise**.
