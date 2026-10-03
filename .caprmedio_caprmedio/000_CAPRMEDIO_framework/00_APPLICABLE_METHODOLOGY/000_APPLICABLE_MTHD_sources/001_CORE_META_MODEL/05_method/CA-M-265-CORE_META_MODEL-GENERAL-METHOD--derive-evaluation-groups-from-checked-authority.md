---
subjects:
  governs: "Atom/Content Role: Evaluation/grouping"
  depends_on:
    - "Atom/Content Role"
    - "Evaluation For Relation"
version: 9
updated_at: "2026-10-01 21:38:15 +0400"
relations: {}
atom_id: "CA-M-265"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Derive evaluation groups from checked authority

## Scope

derivation of Er, Em, and Ed groups from checked authority.

## Claim

**to** derive Er, Em, **and** Ed groups, resolve the Content Role of **every** `evaluation_for` target **and** include the Evaluation **in** the corresponding Requirement, Method, **or** Delivery group; **if** targets span multiple roles, **then** include it **in** **every** applicable group **without** assigning a new Content Role **or** persisting a duplicate target-role field. absence of individual targets on a Core **or** General Evaluation policy admitted by CA-R-1018-CORE_META_MODEL-CORE-REQUIREMENT--register-evaluation-targets **must not** require an invented classification.

## Details
