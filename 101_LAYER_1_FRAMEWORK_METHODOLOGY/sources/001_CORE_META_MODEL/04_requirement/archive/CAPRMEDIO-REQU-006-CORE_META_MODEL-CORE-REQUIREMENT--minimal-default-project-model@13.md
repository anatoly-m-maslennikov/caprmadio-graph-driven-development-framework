---
version: 13
updated_at: "2026-09-14 23:34:13 +0000"
relations:
  child_of:
    - CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary
subjects:
  governs: "Project/minimum model"
  depends_on:
    - "Project"
    - "Atom/Content Role: Requirement"
    - "Atom/Content Role: Implementation"
    - "Atom"
    - "Structural Level"
    - "CAPRMEDIO Framework Instance"

atom_id: "CAPRMEDIO-REQU-006"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 9
---
# Minimal default project model

CAPRMEDIO **must** use Project-scope Requirement authority plus its real Implementation as the minimum Project model, **must not** require an Implementation Atom, **and** **may** enable other Atom roles, applicability tiers, Structural Levels, descendant scopes, **or** automation **only** **when** necessary.
