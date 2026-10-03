---
content_role: Evaluation
type: QA Case
current_scope_unit: SKILLS
claim_target_scope_unit: SKILLS
local_tier: Standard
author: Anatoly Maslennikov
status: Draft
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Skill/context loading"
  depends_on:
    - "AI Agent"
    - "Action"
    - "Methodology"
    - "Skill"
    - "Step"
    - "Step Run"
    - "Tool"
    - "Workflow"
version: 1
updated_at: "2026-09-23 19:41:33 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"evaluation_for": ["CA-R-1529", "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559"], "relates_to": ["CA-R-1522", "CA-R-1601", "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-564"]}
---
# Summary

Check context loading for MCP-delivered Workflow Steps

## Claim

the context-loading Evaluation **must** distinguish necessary current-Step context from unrelated **or** prematurely loaded instructions under CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559 **and** CA-R-1529.

### Inputs and evidence

- identify the supported host, Skill package Revision, interface boundary, current Workflow **and** Step bindings, required standing authority, **and** an admitted Agentic Step fixture.
- provide **`=1`** necessary referenced resource, an unrelated resource, **and** a future-Step prompt as distinguishable fixture items. define which current inputs **and** authority are mandatory **before** observing the run.
- retain observable discovery, body-load, MCP-response, resource-fetch, **and** context-insertion evidence. distinguish what the Skill requests from **any** independently supplied host context; do **not** claim visibility into an opaque host.

### Checks and results

- discovery exposes the bounded entry metadata; activation loads the thin bootstrap **and** response handler. neither phase inserts the fixture's task-specific procedure into the standing Skill body.
- the admitted MCP response supplies sufficient current-Step instructions **and** bindings. the receiving context can use the necessary resource **without** loading the unrelated resource, future-Step prompt, **or** complete Methodology.
- **after** the executor admits a subsequent Step, its necessary context becomes eligible. current governing authority **and** required prerequisites are never excluded merely **to** reduce context size.
- a fixture that omits required current-Step context, preloads unrelated instructions through the Skill, **or** requires remembering a previous conversation **must** fail with the observed boundary identified.
- incomplete host evidence yields an unresolved result, **not** a pass; an unsupported host remains outside the claimed compatibility boundary. pass requires recoverable evidence for **all** applicable checks.
