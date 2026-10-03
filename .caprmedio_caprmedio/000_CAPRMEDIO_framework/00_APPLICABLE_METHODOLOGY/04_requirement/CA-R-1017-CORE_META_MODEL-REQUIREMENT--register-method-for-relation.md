---
atom_id: CA-R-1017
cce_version: cce_1
cce_form: definition
subjects:
  governs:
    continuant:
      - Method For Relation
  depends_on:
    continuant:
      - atom-boundary
      - relation-model
version: 6
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CAPRMEDIO-META-REQU-117--store-each-semantic-relation-once
    - CAPRMEDIO-META-REQU-121--store-only-direct-semantic-relations
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1017-CORE_META_MODEL-REQUIREMENT--register-method-for-relation.md
---
# Register method_for relation

GOVERNANCE **must** register `method_for` as a direct relation owned by a Method Atom **and** directed to one Requirement Atom that the Method serves.
