---
atom_id: CA-R-1016
cce_version: cce_1
cce_form: definition
subjects:
  governs:
    continuant:
      - Rationale For Relation
  depends_on:
    continuant:
      - atom-boundary
      - relation-model
version: 6
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CAPRMEDIO-META-REQU-117--store-each-semantic-relation-once
    - CAPRMEDIO-META-REQU-119-CORE_META_MODEL-REQUIREMENT--requirement-create-rationale-after-its-subject
    - CAPRMEDIO-META-REQU-121--store-only-direct-semantic-relations
---
# Register rationale_for relation

GOVERNANCE **must** register `rationale_for` as a direct relation owned by a Rationale Analysis Atom **and** directed to one Requirement, Method, Evaluation, **or** Delivery Atom that it explains.
