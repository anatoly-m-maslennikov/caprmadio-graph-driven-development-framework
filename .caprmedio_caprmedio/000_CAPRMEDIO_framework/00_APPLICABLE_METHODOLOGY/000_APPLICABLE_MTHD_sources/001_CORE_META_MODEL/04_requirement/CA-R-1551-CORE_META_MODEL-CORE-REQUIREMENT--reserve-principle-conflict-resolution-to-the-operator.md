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
version: 4
updated_at: "2026-10-03 00:06:54 +0400"
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
global_tier: 9
---
# Summary

Reserve Principle-conflict resolution to the Operator

## Scope

conflicts between active Project Principles **and** an AI Agent's delegated conflict resolution.

## Claim

- **only** an Operator **may** resolve a conflict between active Project Principles, **and** an Operator's decision to resolve that conflict is non-delegable.
- an AI Agent **may** detect, analyze, **and** propose resolutions for a conflict between active Project Principles but **must not** choose a resolution for a conflict between active Project Principles.
- an AI Agent **may** resolve a conflict that does **not** involve two active Project Principles **only** **when** the AI Agent's active Operator delegation permits **every** required action **and** the configured confidence requirements are satisfied.

## Details
