---
subjects:
  governs: "Actor"
  depends_on:
    - "Operator"
    - "AI Agent"
    - "Project"
    - "Atom/Local Tier: Principle"
    - "AI Agent Delegation"
    - "Autonomous Confidence Threshold"
version: 3
updated_at: "2026-09-21 00:39:50 +0000"
relations:
  child_of:
    - CA-R-1058
atom_id: "CA-R-1551"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Reserve Principle-conflict resolution to the Operator

- **only** an Operator **may** resolve a conflict between active Project Principles, **and** that decision is non-delegable.
- an AI Agent **may** detect, analyze, **and** propose resolutions for that conflict but **must not** choose one.
- an AI Agent **may** resolve a conflict that does **not** involve two active Project Principles **only** **when** its active Operator delegation permits **every** required action **and** the configured confidence requirements are satisfied.
