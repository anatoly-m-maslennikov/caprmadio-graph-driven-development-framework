---
subjects:
  governs: "AI Agent/authorization"
  depends_on:
    - "AI Agent"
    - "Operator"
    - "AI Agent Delegation"
version: 4
updated_at: "2026-10-03 00:22:56 +0400"
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
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1552-CORE_META_MODEL-CORE-REQUIREMENT--require-active-delegation-for-ai-agent-actions.md
  source_atom_id: CA-R-1552
  source_atom_revision: 4
  source_sha256: 9c8bf376935993dd5ad8f8d42f38d5a63de1b4b47a0681b5d856ac6e77036961
  original_relations_sha256: b47bf49353063d138eaaafb2507e53893b8f65ed84f88d6c603da43b611c30d9
---
# Summary

Require active delegation for AI Agent actions

## Scope

AI Agent actions under active Operator-issued delegation.

## Claim

an AI Agent **may** perform **or** authorize a governed action **without** per-action Operator approval **only** **when** an active Operator-issued delegation authorizes that identified Agent, action, target scope, **and** applicable constraints.

## Details
