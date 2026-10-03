---
atom_id: CA-R-1625
content_role: Requirement
current_scope_unit: SKILLS
claim_target_scope_unit: SKILLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "CAPRMEDIO Main Skill"
  depends_on:
    - "AI Agent"
    - "Action"
    - "Operator"
    - "Skill"
    - "Step Run"
    - "Workflow"
version: 9
updated_at: "2026-10-01 21:44:50 +0400"
relations: {"child_of": ["CAPRMEDIO-METHODOLOGY-REQU-508"], "relates_to": ["CA-R-1522", "CA-R-1626"]}
---
# Summary

Provide CA as the universal entry skill

## Scope

requests submitted by Operators and AI Agents through the CAPRMEDIO Main Skill `ca` for methodology-defined Workflow execution and MCP Step instructions and results.

## Claim

FRAMEWORK_ENGINE **must** provide `ca` as the primary Skill entry point through which Operators **and** AI Agents submit requests **to** methodology-defined Workflow execution **and** exchange current Step instructions **and** results through MCP.

the Skill remains within the thin-wrapper boundary of CA-R-1626-SKILLS-REQUIREMENT--keep-ca-and-specialist-skills-thin; WORKFLOW_ORCHESTRATOR retains coordination under CA-R-1522-WORKFLOW_ORCHESTRATOR-REQUIREMENT--provide-workflow-orchestration-from-methodology rather than transferring route selection **or** Step sequencing into the Skill.

## Details
