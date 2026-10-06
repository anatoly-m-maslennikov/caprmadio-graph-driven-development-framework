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
      - CCE
      - Atom/Claim
      - "Atom/Content Role: Plan/Plan Type: Task/Scope"
      - "Atom/Content Role: Plan/Plan Type: Task/Definition of Done"
version: 11
updated_at: 2026-08-29 02:40:41 +0400
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
7. state **`=1`** Autonomous Confidence Threshold.
8. include Task Details **only** **when** the information remains within the Task Scope **and** Claim **and** establishes no additional Definition of Done.
