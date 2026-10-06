---
atom_id: CA-R-1275
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Subject"
  depends_on:
    - "Atom"
    - "Entity"
    - "Action"
    - "Process"
    - "Term"
    - "Relation"
    - "GOVERNS"
    - "DEPENDS_ON"
    - "Subject Path"
version: 8
updated_at: "2026-09-14 04:00:22 +0400"
relations: {}
---
# Define Subject

a Subject **means** a direct typed Relation from an Atom **to** its canonical Entity, Action, **or** Process target, using GOVERNS **or** DEPENDS_ON. the Subject is the Relation, **not** its target, the path identifying that target, **or** a Term used **in** the path. this Relation does **not** create a separately identified intermediate object, make its target bearer-dependent on the Atom, **or** make a reusable Action **or** Process interchangeable with a particular execution.
