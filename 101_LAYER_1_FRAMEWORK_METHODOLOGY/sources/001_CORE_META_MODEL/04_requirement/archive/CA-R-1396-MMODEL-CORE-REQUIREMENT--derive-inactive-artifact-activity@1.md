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
      - Entity/Type/Status
version: 1
updated_at: 2026-09-04 03:36:02 +0400
relations: {}
---
# Derive Inactive Artifact Activity

an Artifact's Activity **must** be Inactive **if** its current type-qualified Status **`!=`** Active.
