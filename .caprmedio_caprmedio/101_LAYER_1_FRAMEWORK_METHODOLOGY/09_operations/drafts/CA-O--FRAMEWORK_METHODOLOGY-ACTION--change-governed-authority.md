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
  governs: "Change Governed Authority"
  depends_on:
    - "Action"
    - "Workflow"
    - "Workflow Run"
    - "Operator"
    - "AI Agent"
    - "AI Agent Delegation"
    - "Atom"
    - "Atom/Revision"
    - "Scope Unit"
    - "Atom/Local Tier: Principle"
    - "Autonomous Confidence Threshold"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Concern"
    - "Atom/Status"
    - "Journal"
version: 4
updated_at: "2026-09-23 17:20:35 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1530", "CA-R-1565", "CA-M-314", "CA-R-1552", "CA-R-1558", "CA-R-852", "CA-R-1551", "CA-R-1557", "CA-O-028", "CA-O-008", "CA-M-271", "CAPRMEDIO-META-REQU-144"]}
---
# Summary

Change governed authority

## Claim

Change Governed Authority **means** the Action that carries an authorized session change request through the applicable existing mutation behavior **and** reports the actual result, **without** establishing another approval policy **or** reimplementing lifecycle operations.

### Inputs and preconditions

- the actual Operator request, exact proposed changes, affected source Atoms **and** Revisions, target Scope Units, **and** expected result.
- applicable active authority, Project Principles, effective confidence settings, existing mutation behavior, **and** current authorization evidence.
- **any** unresolved conflict, required Evaluation, preservation condition, **or** stricter approval gate relevant **to** this change.

### Behavior

1. classify the input under CA-R-1558. exploratory discussion remains read-only; an explicit instruction **to** change governed state is assessed as that instruction, **not** forced through another discussion-only round.
2. inspect the applicable active authority **and** Principles for the exact proposed change. use CA-O-028 **when** RMEDO conflicts need resolution; do **not** duplicate its correction algorithm **or** automatically create a Concern contrary **to** CA-R-1557.
3. check whether the current Operator instruction **or** an active delegation covers the identified Agent, actions, targets, **and** constraints under CA-R-852 **and** CA-R-1552. honor stricter approval gates **and** CA-R-1551. ask for a decision **only** **when** required authority, permission, **or** confidence remains unresolved; do **not** demand a second approval solely because the change is about authority.
4. prepare the exact authorized mutation using the existing source-change **and** lifecycle behavior. use CA-O-008 for approved source corrections **where** applicable. Draft creation is governed by the actual authorized request **and** current authoring authority, **not** by a separate requirement that the Operator say the word Draft.
5. recheck current sources **and** authorization **before** dispatch. reuse the admitted target Action **or** Workflow rather than writing another create, update, replace, promote, **or** archive procedure. **if** the selected behavior requires a separate Workflow Run, return a handoff **to** the caller; do **not** start a nested run **or** equate handoff with completion.
6. **when** the selected behavior returns execution results, preserve its actual effects, required checks, failures, **and** evidence references. do **not** widen scope, infer approval, report an unchecked result as complete, **or** create another authoritative history instead of referencing the existing Journal evidence.

### Results and effects

- changed: the exact completed authorized changes, resulting source references, **and** required check evidence returned by the existing mutation behavior.
- handed off: the selected existing Workflow **and** complete input/authorization context for the caller; no mutation completion is claimed.
- blocked: the unresolved authority, conflict, permission, confidence, **or** source-state condition, **and** **any** specific Operator decision still required.
- failed: actual partial effects, remaining work, **and** recovery evidence; retries **or** rollback require their own applicable authority **and** bounds.

effects are limited **to** the exact authorized change performed through the selected existing behavior. routing, an accepted proposal, session restoration, **or** a high confidence score does **not** independently authorize persistence.
