---
subjects:
  governs: "CCE/Role Profile: Evaluation"
  depends_on:
    - "Atom/Content Role: Evaluation"
    - "CCE Operator"
    - "Condition Expression"
version: 4
updated_at: "2026-10-02 20:35:16 +0400"
relations:
  child_of:
    - CA-M-307
  relates_to:
    - CA-R-1341
    - CA-M-122
    - CA-M-264
atom_id: "CA-M-312"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Write Evaluation Claims with the Evaluation CCE Profile

## Scope

Evaluation Claims with the Evaluation CCE Role Profile.

## Claim

**to** write an Evaluation Claim with the Evaluation CCE Role Profile, the Author **must** perform **all** of:

1. state the primary contribution as one falsifiable check, acceptance criterion, **or** disposition rule against identified checked authority **and** Scope.
2. state recoverable inputs, the evaluated subject, observable evidence, **and** the condition that yields each result necessary for reproducibility under CA-M-264-CORE_META_MODEL-METHOD--write-evaluations-with-reproducible-falsification.
3. use condition, temporal, quantification, logical, restriction, predicate, **and** comparison Operators with explicit scope over the checked evidence **and** result.
4. use modality **only** to constrain correct evaluation **or** disposition. an Evaluation **must not** create the Requirement that it checks.
5. include a checking procedure **only** as subordinate Evaluation content. keep reusable authoring technique **or** general test procedure **in** Method authority.
6. report unresolved, unavailable, **or** contradictory evidence as its governed result rather than silently converting it **to** pass **or** fail.

## Details
