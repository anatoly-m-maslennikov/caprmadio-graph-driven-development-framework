---
atom_id: CA-R-1019
cce_version: cce_1
cce_form: definition
subjects:
  governs:
    continuant:
      - Delivery For Relation
  depends_on:
    continuant:
      - atom-boundary
      - relation-model
version: 7
updated_at: "2026-09-09 21:56:59 +0400"
relations:
  child_of:
    - CAPRMEDIO-META-REQU-117--store-each-semantic-relation-once
    - CAPRMEDIO-META-REQU-121--store-only-direct-semantic-relations
---
# Register delivery_for relation

`delivery_for` **must** be registered as a direct relation owned by a Delivery Atom **and** directed to one Requirement **or** Method Atom that the Delivery realizes.
