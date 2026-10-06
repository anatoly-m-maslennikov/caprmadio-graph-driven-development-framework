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
      - Artifact/Revision/Status
version: 2
updated_at: 2026-09-04 23:37:00 +0400
relations: {}
---
# Derive Inactive Artifact Activity

an Artifact's Activity **must** be Inactive **if** its current Revision Status **`!=`** Active.
