---
atom_id: CA-R-1014
cce_version: cce_1
cce_form: requirement
subjects:
  governs:
    continuant:
      - Atom/Scope
  depends_on:
    continuant:
      - Scope Unit/Scope
      - Operator
      - Atom/Subjects/Subject/Entity
      - Atom/Claim/Scope
version: 10
updated_at: 2026-09-04 23:11:19 +0400
relations:
  child_of:
    - CA-R-919
    - CA-R-1013
---
# Resolve Atom Scope Contextually

an Atom Scope **must** include its current Scope Unit Scope **or** named Operator fallback, the Entity referenced by its **`=1`** GOVERNS Subject, **and** any explicit Scope constraints in its Claim.
