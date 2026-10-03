---
atom_id: CA-R-1203
cce_version: cce_1
cce_form: requirement
subjects:
  governs:
    continuant:
      - Atom/Claim
  depends_on:
    continuant:
      - "Subject/Relation Kind: GOVERNS"
      - Entity
version: 5
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
---
# Split at Multiple Governed Entity Boundaries

an Atom **must** be split **if** its Claim governs more than one Entity.
