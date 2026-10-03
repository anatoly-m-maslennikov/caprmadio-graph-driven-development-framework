---
atom_id: CAPRMEDIO-FRAMEWORK-ENGINE-REQU-558
content_role: Requirement
type: Requirement
current_scope_unit: SKILLS
claim_target_scope_unit: SKILLS
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "CAPRMEDIO Main Skill"
  depends_on:
    - "AI Agent"
    - "Action"
    - "Operator"
    - "Skill"
    - "Step Run"
    - "Workflow"
version: 8
updated_at: "2026-09-23 19:41:33 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"child_of": ["CAPRMEDIO-METHODOLOGY-REQU-508"], "relates_to": ["CA-R-1522", "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559"]}
---
# Summary

Provide CA as the universal entry skill

## Claim

FRAMEWORK_ENGINE **must** provide `ca` as the primary Skill entry point through which Operators **and** AI Agents submit requests **to** methodology-defined Workflow execution **and** exchange current Step instructions **and** results through MCP.

the Skill remains within the thin-wrapper boundary of CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559; WORKFLOW_ORCHESTRATOR retains coordination under CA-R-1522 rather than transferring route selection **or** Step sequencing into the Skill.
