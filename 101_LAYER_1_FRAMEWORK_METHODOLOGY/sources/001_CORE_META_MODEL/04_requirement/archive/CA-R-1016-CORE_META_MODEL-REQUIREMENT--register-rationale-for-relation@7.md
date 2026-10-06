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
version: 7
updated_at: "2026-09-09 21:56:59 +0400"
relations:
  child_of:
    - CAPRMEDIO-META-REQU-117--store-each-semantic-relation-once
    - CAPRMEDIO-META-REQU-119-CORE_META_MODEL-REQUIREMENT--requirement-create-rationale-after-its-subject
    - CAPRMEDIO-META-REQU-121--store-only-direct-semantic-relations
---
# Register rationale_for relation

`rationale_for` **must** be registered as a direct relation owned by a Rationale Analysis Atom **and** directed to one Requirement, Method, Evaluation, **or** Delivery Atom that it explains.
