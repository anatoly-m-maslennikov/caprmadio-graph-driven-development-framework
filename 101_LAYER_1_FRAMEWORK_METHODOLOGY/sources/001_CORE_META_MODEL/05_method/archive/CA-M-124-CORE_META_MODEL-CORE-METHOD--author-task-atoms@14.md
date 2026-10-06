---
atom_id: CA-M-124
cce_version: cce_1
cce_form: method
subjects:
  governs:
    occurrent:
      - Task Atom Authoring
  depends_on:
    continuant:
      - "Autonomous Confidence Threshold"
      - "Confidence Threshold/source"
      - CCE
      - Atom/Claim
      - "Atom/Content Role: Plan/Type: Task/Scope"
      - "Atom/Content Role: Plan/Type: Task/Definition of Done"
version: 14
updated_at: "2026-09-09 02:24:28 +0400"
relations: {}
---
# Author Task Atoms

**to** author one Task Atom, the Author **must** perform **all** of:

1. resolve **`=1`** effective Author from the declared Author **or** its default.
2. resolve **`=1`** effective Assignee from the declared Assignee **or** its default.
3. state **`=1`** Claim that assigns its required action **and** intended result to the Assignee.
4. derive the Task Summary from the complete Claim **and** Claim Scope.
5. state **`=1`** atomic **or** composite Task Scope.
6. state **`=1`** Definition of Done according to CA-M-123.
7. resolve **`=1`** effective Autonomous Confidence Threshold according **to** CA-M-271; declare a Task override **only** **when** the Author explicitly selects that Task value, **and** **otherwise** inherit **without** copying it into the Task.
8. include Task Details **only** **when** the information remains within the Task Scope **and** Claim **and** establishes no additional Definition of Done.
