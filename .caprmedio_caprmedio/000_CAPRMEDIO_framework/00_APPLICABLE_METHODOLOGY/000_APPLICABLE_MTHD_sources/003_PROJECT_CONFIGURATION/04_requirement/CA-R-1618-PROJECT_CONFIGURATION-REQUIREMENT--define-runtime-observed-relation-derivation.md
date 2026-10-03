---
atom_id: CA-R-1618
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Runtime-observed Relation Derivation"
  depends_on:
    - "Evidence"
    - "Journal"
    - "Realization Graph"
    - "Relation"
    - "Relation Derivation Class"
version: 4
updated_at: "2026-10-03 01:07:45 +0400"
relations:
  relates_to:
    - CA-R-1616
    - CA-R-1617
    - CA-R-1687
    - CA-R-1746
global_tier: 11
---
# Summary

Define Runtime-observed Relation Derivation

## Scope

runtime-observed derivation of represented Realization Graph Relations.

## Claim

Runtime-observed Relation Derivation **means** that a represented Realization Graph Relation is supported by recoverable evidence of its occurrence during an identified execution.

## Details

the result **must** identify the execution, relevant inputs **and** state, observation boundary, **and** supporting record. observation **in** that execution does **not** prove occurrence **in** unobserved executions, the absence of unobserved Relations, **or** compliance with a Requirement.
