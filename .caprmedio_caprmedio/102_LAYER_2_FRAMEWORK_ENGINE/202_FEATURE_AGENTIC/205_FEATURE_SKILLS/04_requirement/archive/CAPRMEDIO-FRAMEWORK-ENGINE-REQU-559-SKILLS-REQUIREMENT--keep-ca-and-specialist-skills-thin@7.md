---
atom_id: CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559
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
  governs: "Skill/instruction boundary"
  depends_on:
    - "AI Agent Delegation"
    - "Action"
    - "Action/Execution Kind"
    - "CAPRMEDIO Main Skill"
    - "Methodology"
    - "Operator"
    - "Project"
    - "Skill"
    - "Step"
    - "Step Run"
    - "Step/Agentic Execution Context"
    - "Tool"
    - "Workflow"
version: 7
updated_at: "2026-09-23 19:41:33 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"child_of": ["CA-R-1124", "CA-R-643"], "relates_to": ["CA-R-1111", "CA-R-1522", "CA-R-1527", "CA-R-1529", "CA-R-1552", "CA-R-1601", "CA-R-852", "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-564"]}
---
# Summary

Keep CA and specialist skills thin

## Claim

the CAPRMEDIO Main Skill `ca` **and** specialist entry Skills **must** remain very thin bootstrap **and** response handlers rather than contain task-specific procedures.

- retain **only** the standing instructions needed **to** establish the owning Project's framework connection, use the admitted MCP interface, handle Step responses, return actual results, **and** report unavailable inputs, failures, **or** escalation needs. a specialist entry **may** identify its registered route **without** copying that route's procedure.
- obtain task-specific instructions **and** necessary context through MCP responses for the current admitted Agentic Step under CA-R-1522 **and** CA-R-1529. the response supplies the Action instructions, bound inputs **or** accessible references, required output, **and** execution boundaries. do **not** preload the whole Methodology, unrelated resources, **or** future-Step instructions merely **to** remember what comes next.
- keep Workflow transitions **and** execution state with the executor. the Skill **must not** independently select the next Step, replay an uncertain effect, **or** infer completion from receiving a prompt. additional context required by the current Step remains admissible; thinness **must not** omit governing authority **or** necessary inputs.
- retain methodology Action **and** Workflow definitions as behavioral authority. ACTION_PROMPTS implements the Action instructions under CA-R-1601; the MCP response delivers the bound invocation, **not** another independently authored procedure. reference canonical Tools **and** the shared runtime rather than embedding **or** copying executable helpers into Skills.
- keep MCP-delivered instructions within current Operator authorization **and** the admitted Step context. a response does **not** expand delegation, replace higher authority, **or** authorize a guessed fallback procedure **when** the framework connection is unavailable. Integrated **and** Isolated participation retain CA-R-1527's existing boundary.
