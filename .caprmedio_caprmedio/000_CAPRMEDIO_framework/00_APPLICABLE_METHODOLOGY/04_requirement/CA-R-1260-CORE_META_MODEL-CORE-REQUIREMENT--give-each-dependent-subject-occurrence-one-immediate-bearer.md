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
version: 5
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1260-CORE_META_MODEL-CORE-REQUIREMENT--give-each-dependent-subject-occurrence-one-immediate-bearer.md
---
# Give Each Dependent Subject Occurrence One Immediate Bearer

a dependent Subject occurrence **must** have **`=1`** immediate IS_BORNE_BY parent.
