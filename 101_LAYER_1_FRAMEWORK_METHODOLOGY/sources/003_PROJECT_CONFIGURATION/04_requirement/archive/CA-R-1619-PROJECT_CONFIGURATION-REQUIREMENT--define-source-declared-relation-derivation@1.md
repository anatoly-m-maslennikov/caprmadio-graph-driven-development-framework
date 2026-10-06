---
atom_id: CA-R-1619
content_role: Requirement
type: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Source-declared Relation Derivation"
  depends_on:
    - "Evidence"
    - "Realization Graph"
    - "Relation"
    - "Relation Derivation Class"
version: 1
updated_at: "2026-09-23 21:40:21 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to:
    - CA-R-1616
    - CA-R-1617
    - CAPRMEDIO-META-REQU-097
    - CAPRMEDIO-META-REQU-657
---
# Summary

Define Source-declared Relation Derivation

## Claim

Source-declared Relation Derivation **means** that a represented Realization Graph Relation is explicitly encoded **in** an identified selected native source, manifest, **or** configuration.

the result **must** identify the exact source occurrence **and** the interpretation used **to** read that declaration. declaring a Relation does **not** establish that it executes, resolves successfully, **or** satisfies a Requirement.
