---
subjects:
  governs: "AI Agent/authorization"
  depends_on:
    - "AI Agent"
    - "Autonomous Confidence Threshold"
    - "Operator"
    - "AI Agent Delegation"
version: 4
updated_at: "2026-09-21 00:39:50 +0000"
relations: {"child_of":["CAPRMEDIO-META-REQU-144"]}
atom_id: "CA-R-1555"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 10
---
# Govern CA execution gates

an identified AI Agent **may** omit clarification **only** **when** confidence **in** **every** following item meets its applicable configured requirement:

- intent;
- scope;
- route;
- entry criteria.

confidence **must not** create delegated authority **or** bypass per-action Operator approval **when** active authority requires it.
