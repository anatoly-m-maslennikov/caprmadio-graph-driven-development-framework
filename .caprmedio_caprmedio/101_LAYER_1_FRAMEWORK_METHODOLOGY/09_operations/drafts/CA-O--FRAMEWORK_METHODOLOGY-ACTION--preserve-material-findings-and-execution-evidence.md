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
  governs: "Preserve Material Findings and Execution Evidence"
  depends_on:
    - "Action"
    - "Operator"
    - "AI Agent Delegation"
    - "Project"
    - "Scope Unit"
    - "Artifact"
    - "Atom"
    - "Atom/Content Role: Analysis"
    - "Atom/Content Role: Operations"
    - "Atom/Content Role: Evaluation"
    - "Journal"
    - "Journal/Record"
    - "Event"
    - "Evidence"
    - "Provenance"
    - "Projection"
    - "Atom/Content Role: Plan/Type: Plan"
version: 1
updated_at: "2026-09-23 17:57:20 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1490", "CA-M-002", "CA-R-1337", "CA-R-1530", "CA-R-1552", "CA-R-1558", "CA-R-852", "CAPRMEDIO-META-REQU-158", "CA-R-1463", "CAPRMEDIO-META-REQU-097", "CA-R-1491", "CA-M-314", "CA-R-1565", "CA-R-1464", "CA-D-434", "CA-D-479"]}
---
# Summary

Preserve material findings and execution evidence

## Claim

Preserve Material Findings and Execution Evidence **means** the Action that preserves valuable findings **and** actual execution evidence through their appropriate existing records, within applicable authorization **and** recording obligations.

### Inputs

- the information **to** preserve, its source context, existing evidence references, **and** the reason it matters.
- the owning Project **and** Scope Unit, relevant existing records, applicable authority, **and** the current Operator request **or** active delegation.
- actual observed events, completed effects, failures, **and** uncertainties; an intended effect is **not** evidence that it happened.

### Behavior

1. assess value under CA-R-1490. reuse is **not** a prerequisite: a one-time decision, failure, **or** origin record can matter. information with no preservation need can remain ephemeral; lack of reuse alone does **not** establish that absence.
2. check authorization under CA-R-1558, CA-R-1552, **and** CA-R-852. exploratory discussion does **not** automatically authorize persistence. carry out an explicit authorized request **or** admitted delegated recording obligation **without** a blanket second approval; unresolved permission **or** stricter applicable gates remain blockers.
3. distinguish findings, explanations, comparisons, **and** rationale under CA-R-1337 from actual governed events under CAPRMEDIO-META-REQU-158. the former belong **in** Analysis; actual Artifact changes **and** execution history belong **in** the existing Project Journal. a historical observation is **not** an Operations definition; reusable behavior proposals follow their own authorized authoring request under CA-R-1530.
4. find existing records **before** creating another. reuse canonical records **and** references under CA-M-002. keep origin history separate from evidence of correctness under CAPRMEDIO-META-REQU-097; do **not** convert an Analysis finding into accepted authority **or** an observed effect into a successful Evaluation.
5. use existing authorized Artifact-change behavior **to** preserve missing Analysis content **and** existing Journal behavior **to** record actual governed events. retain evidence boundaries **and** known uncertainty; do **not** fabricate unknown Actors, times, causes, **or** outcomes. reuse canonical Event identities rather than independently maintaining another history. log views remain Projections under CA-R-1463.
6. check that the requested information is recoverable from the returned records **and** that references resolve. an already preserved item returns its existing reference **without** creating a duplicate. report separate conformance findings **without** making them a Journal admission gate under CA-R-1491.

### Results

- preserved: the information disposition, canonical record references, actual changes **or** no-change result, **and** known evidence limits.
- blocked: the preserved input context, unresolved permission **or** destination, **and** the specific decision required from the Operator.
- failed: actual partial effects, remaining information **to** preserve, **and** available recovery evidence; do **not** report incomplete preservation as complete.

effects are limited **to** the authorized preservation work. this Action does **not** execute unfinished Plans, promote governing Drafts, invent reusable behavior from historical facts, **or** create a second authoritative Journal.
