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
      - "Atom/Claim/Structural Entity"
      - "Scope Unit"
      - "Atom Collection/Type: Epic"
      - "Scope Expression"
      - "Atom/Content Role: Plan/Type: Task/Definition of Done"
version: 17
updated_at: "2026-09-12 03:06:55 +0400"
relations: {}
---
# Author Task Atoms

**to** author one Task Atom, the Author **must** perform **all** of:

1. resolve **`=1`** effective Author from the declared Author **or** its default.
2. resolve **`=1`** effective Assignee from the declared Assignee **or** its default.
3. state **`=1`** Claim that assigns its required action **and** intended result to the Assignee.
4. derive the Task Summary from the complete Claim **and** Claim Structural Entity.
5. resolve **`=1`** Claim Structural Entity; default an omitted override **to** the nearest containing Scope Unit under CA-R-1445, independently of Epic containment. resolve an explicit target **without** replacing it with the containing Epic **or** Scope Unit, retain narrower **or** composite selections as restrictions **in** the Claim, **and** reject an ancestor Scope Unit as a target.
6. state **`=1`** Definition of Done according to CA-M-123.
7. resolve **`=1`** effective Autonomous Confidence Threshold according **to** CA-M-271; declare a Task override **only** **when** the Author explicitly selects that Task value, **and** **otherwise** inherit **without** copying it into the Task.
8. include Task Details **only** **when** the information remains within the Claim's restrictions **and** identified Claim Structural Entity **and** establishes no additional Definition of Done.
