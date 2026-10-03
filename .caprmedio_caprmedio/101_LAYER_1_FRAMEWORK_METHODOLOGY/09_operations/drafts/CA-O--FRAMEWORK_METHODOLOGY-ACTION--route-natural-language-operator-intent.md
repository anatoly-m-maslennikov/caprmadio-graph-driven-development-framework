---
content_role: Operations
type: Action
current_scope_unit: FRAMEWORK_METHODOLOGY
claim_target_scope_unit: FRAMEWORK_METHODOLOGY
local_tier: Standard
author: Anatoly Maslennikov
status: Draft
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Route Operator Intent"
  depends_on:
    - "Action"
    - "Workflow"
    - "Operator"
    - "Project"
    - "Scope Unit"
    - "CAPRMEDIO Main Skill"
    - "CAPRMEDIO Routing Tree"
    - "Framework Instance Settings"
    - "Autonomous Confidence Threshold"
    - "AI Agent Delegation"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Methodology"
version: 4
updated_at: "2026-09-23 17:20:35 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1530", "CA-R-1565", "CA-M-314", "CA-R-1552", "CA-R-1558", "CA-R-852", "CAPRMEDIO-GOV-REQU-333", "CAPRMEDIO-GOV-REQU-336", "CA-R-1355", "CAPRMEDIO-METHODOLOGY-REQU-508", "CA-M-271", "CAPRMEDIO-META-REQU-144", "CA-O-079"]}
---
# Summary

Route natural-language operator intent

## Claim

Route Operator Intent **means** the Action that resolves a current natural-language Operator request through the canonical CAPRMEDIO Routing Tree **and** returns its selected route, required inputs, **and** execution conditions **without** treating route selection as authorization.

### Inputs and preconditions

- the actual Operator input, relevant conversational context, current Project **and** Scope Unit, **and** initialized session context.
- the current registered CAPRMEDIO Routing Tree, applicable route precedence, effective settings, **and** available authorization.
- references **to** the active authority needed for the selected request; load additional authority on demand rather than loading the whole Methodology.

### Behavior

1. interpret the request using the registered intent concepts, synonyms, entry criteria, outputs, **and** authority effects under CAPRMEDIO-GOV-REQU-333. do **not** maintain another routing dictionary **in** this Action **or** the Skill.
2. select a valid route using CAPRMEDIO-GOV-REQU-336 **and** CA-R-1355. equivalent natural-language **and** explicit Skill requests retain the behavior required by CAPRMEDIO-METHODOLOGY-REQU-508; unresolved competing routes remain ambiguous.
3. resolve applicable confidence settings under CA-M-271 **and** preserve the distinction between confidence **and** permission under CAPRMEDIO-META-REQU-144. insufficient confidence, missing required inputs, **or** unresolved meaning returns a clarification need rather than a guessed executable route.
4. apply CA-R-1558 **to** distinguish exploration from an explicit change request. for an executable request, return the existing target Action **or** Workflow, its inputs, required authorization checks, **and** applicable approval conditions. do **not** require another approval **when** valid existing authorization already covers the operation **and** no stricter gate applies.
5. return a bounded in-session execution proposal **when** useful. it is **not** a persisted Plan Atom **and** does **not** create one automatically. **any** requested Plan persistence follows current Plan authority; unfinished work follows CA-O-079 rather than a duplicate routing-specific preservation rule.

### Results and effects

- routed: the selected route, routing-source reference, request classification, target Action **or** Workflow reference, bound inputs, **and** outstanding execution conditions.
- clarification needed: the unresolved interpretation, relevant alternatives, missing evidence, **and** the precise question that current authority cannot settle.
- blocked **or** failed: the invalid routing input **or** failed operation, with recoverable context **and** no claimed execution.

this Action returns routing information **to** the calling session; it does **not** execute the selected mutation, widen a delegation, create an approval, **or** report the requested work complete. the session uses the selected existing operational behavior under its own execution boundary.
