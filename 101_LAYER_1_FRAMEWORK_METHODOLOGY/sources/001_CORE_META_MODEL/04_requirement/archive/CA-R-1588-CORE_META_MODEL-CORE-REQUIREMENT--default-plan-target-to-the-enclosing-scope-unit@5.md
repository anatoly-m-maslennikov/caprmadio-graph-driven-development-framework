---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Claim/Target Scope Unit"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Claim/Target Scope Unit"
    - "Scope Unit"
    - "Hub Atom"
    - "Atom/Content Role: Plan/Type: Plan/Label"
version: 5
updated_at: "2026-09-22 23:02:20 +0000"
relations: {"relates_to": ["CA-R-1574", "CA-D-482"]}
atom_id: "CA-R-1588"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Summary

Default Plan target to the enclosing Scope Unit

## Claim

during authoring, a Plan with no separately selected Claim Target Scope Unit **must** select its owning Scope Unit as the target, independently of decomposition **or** Label; a Hub does **not** become that default target. carry the resolved target under CA-D-482.
