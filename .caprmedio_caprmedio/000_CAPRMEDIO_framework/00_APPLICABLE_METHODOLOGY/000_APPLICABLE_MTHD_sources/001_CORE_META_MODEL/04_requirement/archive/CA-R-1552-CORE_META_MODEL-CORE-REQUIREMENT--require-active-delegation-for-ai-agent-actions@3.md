---
subjects:
  governs: "AI Agent/authorization"
  depends_on:
    - "AI Agent"
    - "Operator"
    - "AI Agent Delegation"
version: 3
updated_at: "2026-09-21 00:39:50 +0000"
relations:
  child_of:
    - CA-P-034
atom_id: "CA-R-1552"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Require active delegation for AI Agent actions

an AI Agent **may** perform **or** authorize a governed action **without** per-action Operator approval **only** while an active Operator-issued delegation authorizes that identified Agent, action, target scope, **and** applicable constraints.
