---
content_role: Method
type: Method
current_scope_unit: SKILLS
claim_target_scope_unit: SKILLS
local_tier: Standard
author: Anatoly Maslennikov
status: Draft
cce_version: cce_1
cce_form: method
subjects:
  governs: "Skill/authoring"
  depends_on:
    - "AI Agent Delegation"
    - "Action"
    - "CAPRMEDIO Main Skill"
    - "Methodology"
    - "Operator"
    - "Skill"
    - "Step"
    - "Tool"
    - "Workflow"
version: 1
updated_at: "2026-09-23 19:41:33 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"method_for": ["CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559"], "relates_to": ["CA-R-1111", "CA-R-1522", "CA-R-1527", "CA-R-1529", "CA-R-1552", "CA-R-1601", "CA-R-852", "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-558", "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-564"]}
---
# Summary

Write very thin Skills for MCP-delivered Step instructions

## Claim

**to** author a very thin Skill under CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559, separate stable bootstrap **and** response-handling instructions from the task-specific instructions supplied by the framework.

- use a short discovery description that identifies the entry purpose **and** its registered route **when** applicable; do **not** put a Workflow procedure **in** the description.
- keep the standing body limited **to** framework connection, the admitted request/result interface, **and** generic response, failure, missing-input, **and** escalation handling. explain how **to** consume the current invocation **without** embedding the decisions performed by its Action.
- reference the shared runtime under CAPRMEDIO-FRAMEWORK-ENGINE-REQU-564. represent executable capabilities by references **to** canonical Tools, **not** scripts maintained inside the Skill.
- let the current MCP response supply the Action prompt **and** its Step bindings under CA-R-1522 **and** CA-R-1529. retain accessible references for additional current-Step context rather than preloading the Methodology **or** a library of unrelated prompts.
- refer **to** the existing delegation **and** Step-context rules. do **not** author another approval policy, routing tree, continuation table, **or** delegation procedure inside the Skill.

the result is a bounded Skill wrapper that remains valid **when** the admitted task-specific Action instructions change **without** changing the wrapper interface. **if** authoring reveals a missing interface, source, **or** authority binding, report that gap rather than hide it inside a larger Skill body. this Method governs authoring; it does **not** define a new session Workflow **or** promote another Draft.
