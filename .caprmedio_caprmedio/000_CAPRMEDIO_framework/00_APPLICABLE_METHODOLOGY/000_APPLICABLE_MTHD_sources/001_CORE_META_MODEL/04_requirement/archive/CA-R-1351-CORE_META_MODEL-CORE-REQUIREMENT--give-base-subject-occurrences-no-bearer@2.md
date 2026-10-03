---
atom_id: CA-R-1351
cce_version: cce_1
cce_form: cardinality
subjects:
  governs:
    continuant:
      - IS_BORNE_BY
  depends_on:
    continuant:
      - Base Entity
      - Subject
version: 2
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
---
# Give Base Subject Occurrences No Bearer

a base Subject occurrence **must** have **`=0`** IS_BORNE_BY parents.
