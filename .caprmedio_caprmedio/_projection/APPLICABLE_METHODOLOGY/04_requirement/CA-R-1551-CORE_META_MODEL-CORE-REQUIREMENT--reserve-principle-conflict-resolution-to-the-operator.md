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
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1551-CORE_META_MODEL-CORE-REQUIREMENT--reserve-principle-conflict-resolution-to-the-operator.md
  source_atom_id: CA-R-1551
  source_atom_revision: 4
  source_sha256: 791f505d8bfa5af63b43e5f08d6543a67cd8a34b3558b6c215a767a208d1f025
  original_relations_sha256: aa9d7d21c52e869f2a5593baf11368dd2fc11f56d7c6be53eda3c1cd0436618c
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
