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
      - Primary Entity
      - Subject
version: 3
updated_at: 2026-09-07 09:59:57 +0000
relations: {}
---
# Give Primary Entity Occurrences No Bearer

a Primary Entity referenced by a Subject **must** have **`=0`** IS_BORNE_BY parents.
