---
subjects:
  governs: "Atom/Scope"
  depends_on:
    - "Operator"
    - "Scope Unit"
version: 15
updated_at: "2026-09-24 14:16:19 +0000"
relations:
  child_of:
    - CA-R-927
---
# Use Operator Names When an Atom Has No Scope Unit

an Atom with no Scope Unit owner **must** have **`=1`** identified human Operator as its owner, referenced by that Operator's registered name.

- multiple Operators **may** participate **without** becoming multiple owners of that Atom.
- ownership is distinct from the Revision's Author **and** a Plan's Assignee.
