---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Blocking/Carrier"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Plan/Type: Plan/Blocking"
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
    - "Atom/Identifier"
    - "Atom/Subjects"
version: 3
updated_at: "2026-09-22 23:02:20 +0000"
relations: {"relates_to": ["CA-R-1580", "CA-D-481", "CA-R-1026", "CA-R-1200"]}
---
# Summary

Serialize explicit Plan blocking

## Claim

**every** explicit `A BLOCKS B` fact **must** be stored once on Plan `A` under `relations.blocks`, as a unique canonical Atom ID for Plan `B`; an omitted list encodes **=0** outgoing blocking Relations.

- do **not** store a separate inverse list.
- do **not** encode Plan scheduling with `relations.depends_on` **or** `subjects.depends_on`.
- store decomposition separately under CA-D-481; do **not** derive blocking from decomposition **or** directory order.
