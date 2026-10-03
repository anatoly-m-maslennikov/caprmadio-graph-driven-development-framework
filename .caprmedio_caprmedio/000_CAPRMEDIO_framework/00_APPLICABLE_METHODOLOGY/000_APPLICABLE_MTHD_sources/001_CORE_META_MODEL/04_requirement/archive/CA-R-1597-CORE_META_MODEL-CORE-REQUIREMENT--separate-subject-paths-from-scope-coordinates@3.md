---
subjects:
  governs: "Atom/Subjects"
  depends_on:
    - "Subject"
    - "Subject Path"
    - "Entity"
    - "Scope Unit"
    - "Atom/Claim/Target Scope Unit"
version: 3
updated_at: "2026-09-22 20:07:50 +0000"
relations:
  relates_to:
    - CA-R-1275
    - CA-R-1201
    - CA-R-1202
    - CA-R-1595
    - CA-M-273
atom_id: "CA-R-1597"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Separate Subject Paths from Scope Coordinates

an Atom's Subject Paths **must** identify the Entity targets of its Subject Relations **without** substituting those paths for its owning Scope Unit **or** its Claim Target Scope Unit.
