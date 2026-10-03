---
content_role: Requirement
type: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Draft
cce_version: cce_1
cce_form: permission
subjects:
  governs: "Realization Graph"
  depends_on:
    - "Atom/Claim"
    - "Evaluation"
    - "Evidence"
    - "Relation Derivation Class"
version: 5
updated_at: "2026-09-23 20:47:56 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-M-312", "CA-R-1494", "CAPRMEDIO-META-REQU-097"]}
---
# Summary

Allow pre-runtime pass only with complete relation coverage

## Claim

an Evaluation using a Realization Graph **may** return `pass` **before** runtime **only when** sufficient evidence establishes the checked Claim for the declared input boundary.

- **if** the Claim requires complete coverage of particular Relation mechanisms, verify that coverage; a completeness declaration alone is insufficient.
- check the actual acceptance condition. complete provenance **or** graph coverage does **not** itself establish that condition.
- a possible inferred Relation is **not** an observed occurrence. **when** required runtime evidence is unavailable **or** a material condition remains unresolved, do **not** substitute a pre-runtime `pass`.

this Claim constrains permission **to** report a result; the applicable E Atoms supply the checks. it does **not** require complete graph coverage for a Claim that needs **only** bounded evidence.
