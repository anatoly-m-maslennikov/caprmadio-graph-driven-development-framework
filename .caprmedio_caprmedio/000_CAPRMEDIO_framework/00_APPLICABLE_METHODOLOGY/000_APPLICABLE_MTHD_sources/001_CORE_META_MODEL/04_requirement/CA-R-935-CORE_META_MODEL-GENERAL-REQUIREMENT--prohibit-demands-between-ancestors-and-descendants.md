---
subjects:
  governs: "relation-model"
  depends_on:
    - "scope-topology"
    - "Atom/Scope"
    - "Atom/Claim/Target Scope Unit"
version: 18
updated_at: "2026-10-02 21:01:00 +0400"
relations:
  child_of:
    - CA-R-932
atom_id: "CA-R-935"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary
Prohibit Demands between ancestors and descendants

## Scope

Demand Atoms.

## Claim

a Demand Atom's Claim Target Scope Unit **must not** be an ancestor **or** descendant of its Consumer Scope Unit.

## Details
