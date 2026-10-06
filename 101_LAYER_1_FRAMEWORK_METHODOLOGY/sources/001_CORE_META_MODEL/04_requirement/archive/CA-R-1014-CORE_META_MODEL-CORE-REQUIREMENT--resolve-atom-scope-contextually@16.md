---
subjects:
  governs: "Atom/Scope"
  depends_on:
    - "Scope Unit/Scope"
    - "Operator"
    - "Atom/Governed Subject"
    - "Atom/Claim"
version: 16
updated_at: "2026-09-22 17:59:17 +0000"
relations:
  child_of:
    - CA-R-1596
atom_id: "CA-R-1014"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Resolve Atom Scope Contextually

an Atom Scope **must** include its current Scope Unit Scope **or** named Operator fallback, its **`=1`** Atom Governed Subject, **and** **any** explicit Scope constraints **in** its Claim.
