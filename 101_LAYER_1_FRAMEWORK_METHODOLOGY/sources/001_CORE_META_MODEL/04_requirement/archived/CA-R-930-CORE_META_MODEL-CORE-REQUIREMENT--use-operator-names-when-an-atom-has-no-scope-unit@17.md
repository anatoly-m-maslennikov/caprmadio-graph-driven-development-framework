---
subjects:
  governs: "Atom/Scope"
  depends_on:
    - "Operator"
    - "Scope Unit"
version: 17
updated_at: "2026-09-29 22:40:00 +0400"
relations:
  child_of:
    - CA-R-927
atom_id: "CA-R-930"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Archived"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 9
---
# Use Operator Names When an Atom Has No Scope Unit

an Atom with no Scope Unit owner **must** have **`=1`** identified human Operator as its owner, referenced by that Operator's registered name.

- multiple Operators **may** participate **without** becoming multiple owners of that Atom.
- ownership is distinct from the Revision's Author **and** a Plan's Assignee.
