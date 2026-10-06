---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Subject"
  depends_on:
    - "Atom"
    - "Entity"
    - "Action"
    - "Workflow"
    - "Term"
    - "Relation"
    - "GOVERNS"
    - "DEPENDS_ON"
    - "Subject Path"
version: 10
updated_at: "2026-09-18 14:16:20 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Define Subject

a Subject **means** a direct typed Relation from an Atom **to** its canonical Entity, Action, **or** Workflow target, using GOVERNS **or** DEPENDS_ON. the Subject is the Relation, **not** its target, the path identifying that target, **or** a Term used **in** the path. this Relation does **not** create a separately identified intermediate object, make its target bearer-dependent on the Atom, **or** make a reusable Action **or** Workflow interchangeable with a particular execution.
