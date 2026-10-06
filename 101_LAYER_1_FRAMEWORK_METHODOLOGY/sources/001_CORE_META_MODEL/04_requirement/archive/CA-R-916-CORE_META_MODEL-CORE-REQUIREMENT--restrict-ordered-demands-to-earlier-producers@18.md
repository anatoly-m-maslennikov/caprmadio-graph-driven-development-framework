---
subjects:
  governs: "relation-model"
  depends_on:
    - "Atom/Scope"
    - "Atom/Claim/Target Scope Unit"
version: 18
updated_at: "2026-09-22 17:59:17 +0000"
relations:
  child_of:
    - CA-R-932
atom_id: "CA-R-916"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Restrict ordered Demands to earlier Producers

**if** a Demand Atom's Consumer Atom Scope Unit **and** Producer Claim Target Scope Unit are ordered siblings, **then** its Producer Claim Target Scope Unit **must** precede its Consumer Atom Scope Unit.
