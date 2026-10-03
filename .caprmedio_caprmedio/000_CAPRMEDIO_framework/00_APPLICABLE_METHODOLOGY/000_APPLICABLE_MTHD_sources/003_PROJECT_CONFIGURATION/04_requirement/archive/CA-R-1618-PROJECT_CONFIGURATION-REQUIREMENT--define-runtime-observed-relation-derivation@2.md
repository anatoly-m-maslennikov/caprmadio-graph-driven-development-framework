---
atom_id: CA-R-1618
content_role: Requirement
type: Requirement
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
version: 2
updated_at: "2026-09-23 21:40:21 +0000"
relations:
  relates_to:
    - CA-R-1616
    - CA-R-1617
    - CAPRMEDIO-META-REQU-097
    - CAPRMEDIO-META-REQU-657
---
# Summary

Define Runtime-observed Relation Derivation

## Claim

Runtime-observed Relation Derivation **means** that a represented Realization Graph Relation is supported by recoverable evidence of its occurrence during an identified execution.

the result **must** identify the execution, relevant inputs **and** state, observation boundary, **and** supporting record. observation **in** that execution does **not** prove occurrence **in** unobserved executions, the absence of unobserved Relations, **or** compliance with a Requirement.
