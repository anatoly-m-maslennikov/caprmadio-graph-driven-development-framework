---
atom_id: CA-R-1260
cce_version: cce_1
cce_form: cardinality
subjects:
  governs:
    continuant:
      - IS_BORNE_BY
  depends_on:
    continuant:
      - Dependent Entity
      - Subject
version: 4
updated_at: 2026-08-29 04:33:13 +0400
relations: {}
---
# Give Each Dependent Subject Occurrence One Immediate Bearer

a dependent Subject occurrence **must** have **`=1`** immediate IS_BORNE_BY parent.
