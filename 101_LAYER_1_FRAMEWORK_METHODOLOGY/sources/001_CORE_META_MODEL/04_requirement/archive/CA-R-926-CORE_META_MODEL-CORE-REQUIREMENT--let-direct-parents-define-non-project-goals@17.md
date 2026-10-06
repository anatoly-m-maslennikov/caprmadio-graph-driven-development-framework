---
subjects:
  governs: "Atom/Content Role: Requirement/Type: Goal"
  depends_on:
    - "Scope Unit"
    - "Project Structure"
    - "Atom/Claim"
    - "Structural Parent Relation"
version: 17
updated_at: "2026-09-22 17:59:17 +0000"
relations:
  child_of:
    - CA-R-925
atom_id: "CA-R-926"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Let Direct Parents Define Non-Project Goals

**every** non-Project Scope Unit **must** have **`>=1`** accepted Goal Atom owned by its declared direct parent Scope Unit. this is a Goal-coverage obligation, **not** the source of the child's structural identity; a missing accepted Goal is a reported gap **and** **must not** remove **or** conceal the declared Scope Unit.
