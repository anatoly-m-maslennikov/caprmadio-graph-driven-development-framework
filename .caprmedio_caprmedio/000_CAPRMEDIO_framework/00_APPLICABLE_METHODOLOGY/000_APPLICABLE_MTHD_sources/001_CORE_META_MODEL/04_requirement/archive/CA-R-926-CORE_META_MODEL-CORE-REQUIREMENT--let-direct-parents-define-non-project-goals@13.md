---
subjects:
  governs: "Atom/Content Role: Requirement/Type: Goal"
  depends_on:
    - "Scope Unit"
    - "Project Structure"
    - "Atom/Claim/Scope"
    - "Structural Parent Relation"
atom_id: CA-R-926
cce_version: cce_1
cce_form: obligation
version: 13
updated_at: "2026-09-15 00:05:45 +0000"
relations:
  child_of:
    - CA-R-925
---
# Let Direct Parents Define Non-Project Goals

**every** non-Project Scope Unit **must** have **`>=1`** accepted Goal Atom owned by its declared direct parent Scope Unit. this is a Goal-coverage obligation, **not** the source of the child's structural identity; a missing accepted Goal is a reported gap **and** **must not** remove **or** conceal the declared Scope Unit.
