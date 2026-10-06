---
atom_id: CA-R-1613
content_role: Requirement
type: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Realization Graph"
  depends_on:
    - "Evidence"
    - "Projection"
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

Classify each Realization Graph relation by derivation

## Claim

**every** represented Realization Graph Relation **must** carry **`>=1`** supported Relation Derivation Classes, with the supporting source **or** execution evidence identified separately for **every** assigned class.

- **when** the same Relation is source-declared, resolved, **or** observed, multiple classifications **may** coexist; they describe evidence origins, **not** mutually exclusive truth values.
- a class identifies how the Relation was obtained. it does **not** prove that the Relation is required, correct, exhaustive, **or** currently applicable.
- missing **or** conflicting derivation evidence remains an explicit unresolved diagnostic; an unsupported class **or** Relation **must not** be presented as established.
