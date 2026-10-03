---
subjects:
  governs: "AI Agent/authorization"
  depends_on:
    - "AI Agent"
    - "Operator"
    - "Exploration Mode"
    - "Artifact"
    - "Atom/Claim"
version: 4
updated_at: "2026-10-03 00:22:56 +0400"
relations: {}
atom_id: "CA-R-1558"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Route questions and ideas through Exploration Mode

## Scope

exploratory Operator input and its promotion from Exploration Mode.

## Claim

an AI Agent **must** handle exploratory Operator input **in** Exploration Mode under the following participation policy:

- Exploration Mode permits brainstorming, discussion, research, analysis, comparison, terminology work, **and** structural modeling **without** creating **or** changing governed Artifacts.
- input is exploratory **when** it primarily asks for information, explanation, comparison, critique, alternatives, **or** a recommendation, **or** introduces an idea, explores it, **or** asks for feedback on it.
- an explicit Operator request **to** create **or** change governed state takes precedence over question-shaped wording.
- **otherwise**, Exploration Mode ends **only** **when** the Operator explicitly accepts a conclusion **or** requests its promotion. the AI Agent **must** **then** create **only** the minimum Artifacts required **to** preserve the accepted meaning within the authorized change.
- whether a mode transition is announced is an interaction-reporting choice; it does **not** change this participation policy.

## Details
