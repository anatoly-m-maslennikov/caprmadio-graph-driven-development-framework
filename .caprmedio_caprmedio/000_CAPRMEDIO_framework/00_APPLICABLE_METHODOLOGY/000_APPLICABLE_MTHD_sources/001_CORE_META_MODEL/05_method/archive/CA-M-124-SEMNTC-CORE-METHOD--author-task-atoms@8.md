---
atom_id: CA-M-124
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - Task
  depends_on:
    continuant:
      - CCE
      - Task/Job
      - Task/Scope
      - Task/Definition of Done
version: 8
updated_at: 2026-08-27 00:50:08 +0400
relations:
  child_of:
    - CA-M-113
    - CA-M-123
    - CA-R-989
    - CA-R-1211
    - CA-R-1212
    - CA-R-1214
    - CA-R-1215
    - CA-R-1043
    - CA-R-1044
    - CA-R-1045
    - CA-R-1078
    - CA-R-1079
    - CA-R-1080
    - CA-R-1081
    - CA-R-1082
    - CA-R-1083
---
# Author Task Atoms

to author one Task Atom, the Author **must** perform all of:

1. resolve exactly one effective Author from the declared Author or its default.
2. resolve exactly one effective Assignee from the declared Assignee or its default.
3. state exactly one Task Job as a Claim that assigns its required action to the Assignee.
4. make the Task Summary express exactly the Task Job.
5. state exactly one atomic or composite Task Scope.
6. state exactly one Definition of Done according to CA-M-123.
7. state exactly one Autonomous Confidence Threshold.
8. include Task Details only when the information remains within the Task Scope and Task Job and establishes no additional Definition of Done.
