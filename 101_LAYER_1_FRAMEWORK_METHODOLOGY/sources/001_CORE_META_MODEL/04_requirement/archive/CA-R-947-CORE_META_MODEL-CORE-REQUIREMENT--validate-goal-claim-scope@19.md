---
subjects:
  governs: "Atom/Claim/Target Scope Unit"
  depends_on:
    - "Atom/Content Role: Requirement/Type: Goal"
    - "Atom/Scope"
    - "Scope Unit"
    - "Project Structure"
    - "Project"
version: 19
updated_at: "2026-09-22 17:59:17 +0000"
relations:
  child_of:
    - CA-R-925
    - CA-R-926
    - CA-R-927
atom_id: "CA-R-947"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Validate Goal Claim Scope

a Goal Atom **must** identify **`=1`** Claim Target Scope Unit that is a direct child of its Atom Scope Unit according **to** authoritative Project Structure, **or** the Project Scope Unit **if** its Atom Scope **contains** no Scope Unit. a Goal reference assigns a purpose **and** **must not** independently declare **or** change the target's Name, parent, order, **or** Carrier binding.
