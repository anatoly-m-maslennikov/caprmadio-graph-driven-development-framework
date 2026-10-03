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
      - Task/Scope
      - Task/Definition of Done
version: 9
updated_at: 2026-08-28 22:31:24 +0400
relations: {}
---
# Author Task Atoms

**to** author one Task Atom, the Author **must** perform **all** of:

1. resolve exactly one effective Author from the declared Author or its default.
2. resolve exactly one effective Assignee from the declared Assignee or its default.
3. state exactly one Claim that assigns its required action and intended result to the Assignee.
4. derive the Task Summary from the complete Claim and Claim Scope.
5. state exactly one atomic or composite Task Scope.
6. state exactly one Definition of Done according to CA-M-123.
7. state exactly one Autonomous Confidence Threshold.
8. include Task Details only when the information remains within the Task Scope and Claim and establishes no additional Definition of Done.
