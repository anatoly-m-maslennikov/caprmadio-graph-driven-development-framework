---
atom_id: CA-R-1018
cce_version: cce_1
cce_form: definition
subjects:
  governs:
    continuant:
      - Evaluation For Relation
  depends_on:
    continuant:
      - atom-boundary
      - relation-model
version: 5
updated_at: 2026-08-29 02:40:41 +0400
relations:
  child_of:
    - CAPRMEDIO-META-REQU-117--store-each-semantic-relation-once
    - CAPRMEDIO-META-REQU-121--store-only-direct-semantic-relations
---
# Register evaluation_for relation

GOVERNANCE **must** register `evaluation_for` as a direct relation owned by an Evaluation Atom **and** directed to one Requirement **or** Method Atom that the Evaluation checks.
