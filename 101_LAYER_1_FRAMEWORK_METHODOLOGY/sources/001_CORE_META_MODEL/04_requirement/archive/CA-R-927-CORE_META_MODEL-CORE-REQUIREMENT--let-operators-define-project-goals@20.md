---
subjects:
  governs: "Atom/Content Role: Requirement/Type: Goal"
  depends_on:
    - "Atom/Claim"
    - "Atom/Scope"
    - "Operator"
    - "Project"
version: 20
updated_at: "2026-09-24 14:16:19 +0000"
relations:
  child_of:
    - CA-R-925
atom_id: "CA-R-927"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Let Operators Define Project Goals

**every** Project Scope Unit **must** be the Claim Target Scope Unit of an accepted Goal Atom whose Atom Scope **contains** no Scope Unit **and** **`=1`** identified human Operator as its owner.
