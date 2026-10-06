---
subjects:
  governs:
    continuant:
      - Atom/Claim/Scope
  depends_on:
    continuant:
      - "Atom/Content Role: Requirement/Type: Goal"
      - Atom/Scope
      - Atom/Claim/Scope/Scope Unit Set
      - Structural Parent Relation
      - Project
atom_id: CA-R-947
cce_version: cce_1
cce_form: obligation
version: 13
updated_at: 2026-09-04 01:04:00 +0400
relations:
  child_of:
    - CA-R-925
    - CA-R-926
    - CA-R-927
---
# Validate Goal Claim Scope

a Goal Atom Claim Scope Unit Set **must** **contain** **`=1`** Scope Unit that is a direct child of its Atom Scope Unit **or** the Project Scope Unit **if** its Atom Scope **contains** no Scope Unit.
