---
subjects:
  governs: "Work Sequence Number"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Plan/Type: Plan/Work Sequence Number"
    - "Atom/Content Role: Plan/Type: Plan/Subtype"
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
    - "Atom/Content Role: Plan/Type: Plan/Blocking"
    - "Atom/Scope"
    - "Atom/Claim/Target Scope Unit"
version: 16
updated_at: "2026-09-22 17:59:17 +0000"
relations:
  child_of:
    - CA-R-991
atom_id: "CA-R-992"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Separate Work Sequence from Atom identity

a Work Sequence Number **must not** establish **or** change Atom identity, Atom Scope, Claim Target Scope Unit, Type, authoring Subtype, decomposition, **or** blocking.
