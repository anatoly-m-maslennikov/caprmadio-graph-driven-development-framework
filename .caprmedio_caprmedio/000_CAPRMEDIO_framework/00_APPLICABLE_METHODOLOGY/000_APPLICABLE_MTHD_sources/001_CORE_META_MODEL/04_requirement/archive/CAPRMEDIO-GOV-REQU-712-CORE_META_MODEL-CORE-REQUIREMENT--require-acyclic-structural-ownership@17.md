---
subjects:
  governs: "relation-model"
  depends_on:
    - "atom-boundary"
version: 17
updated_at: "2026-09-10 04:16:18 +0400"
relations: {}
atom_id: "CAPRMEDIO-GOV-REQU-712"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 9
---
# Require acyclic structural ownership

the directed graph formed by active `structural_parent` relations **must** be acyclic.
