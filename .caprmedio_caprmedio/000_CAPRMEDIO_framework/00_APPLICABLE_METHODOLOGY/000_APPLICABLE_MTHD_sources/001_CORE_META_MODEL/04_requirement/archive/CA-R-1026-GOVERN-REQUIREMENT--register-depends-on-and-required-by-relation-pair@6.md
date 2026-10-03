---
atom_id: CA-R-1026
cce_version: cce_1
cce_form: definition
subjects:
  governs:
    continuant:
      - Dependency Relation Pair
  depends_on:
    continuant:
      - atom-boundary
      - relation-model
version: 6
updated_at: 2026-08-29 02:40:41 +0400
relations:
  child_of:
    - CA-R-1054
---
# Register depends_on and required_by relation pair

GOVERNANCE **must** register `depends_on` as the declared upstream relation **and** `required_by` as its inverse-derived downstream relation **in** the dependency ordering domain.
