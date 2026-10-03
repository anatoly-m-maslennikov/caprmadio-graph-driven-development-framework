---
atom_id: CA-R-1307
cce_version: cce_1
cce_form: cardinality
subjects:
  governs:
    continuant:
      - Artifact/Activity
  depends_on:
    continuant:
      - Artifact
      - Artifact/Revision/Status
version: 6
updated_at: "2026-09-11 02:13:22 +0400"
relations: {}
---
# Limit Artifact Activity to explicit Status models

an Artifact **must** have **`=1`** Activity **in** (Active, Inactive) **if** an explicitly defined Status model applies **to** it, **and** **`=0`** Activity **otherwise**.
