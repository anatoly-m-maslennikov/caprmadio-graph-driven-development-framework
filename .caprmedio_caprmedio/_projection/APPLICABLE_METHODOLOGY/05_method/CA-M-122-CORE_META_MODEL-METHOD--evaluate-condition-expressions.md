---
subjects:
  governs: "CCE Condition Expression Evaluation"
  depends_on:
    - "CCE Condition Expression"
    - "CCE Operator"
version: 16
updated_at: "2026-10-01 21:33:03 +0400"
relations:
  child_of:
    - CA-M-113
atom_id: "CA-M-122"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-122-CORE_META_MODEL-METHOD--evaluate-condition-expressions.md
  source_atom_id: CA-M-122
  source_atom_revision: 16
  source_sha256: f9c8e95aaf79f92b2c92d3cedfdf173870102cac58f6a134fedb830cfe3c5197
  original_relations_sha256: 5eb127874e3ee8c1f6d4c667ea5a3b8f1fcf5ca1bc02536507146474a017249a
---
# Summary

Evaluate Condition Expressions

## Scope

evaluation of CCE Condition Expressions.

## Claim

**to** evaluate one CCE condition expression, the Resolver **must** perform **all** of:

1. evaluate the innermost parenthesized function **before** its containing function.
2. evaluate **`=`** **and** **`!=`** as exact equality **and** inequality between one governed property **and** one canonical value.
3. evaluate **`<`**, **`<=`**, **`>`**, **and** **`>=`** **only** for properties with one governed comparison order.
4. evaluate **in** **and** **not in** as scalar membership **and** non-membership **in** one explicitly parenthesized value list, **or** according **to** CA-M-127-CORE_META_MODEL-METHOD--evaluate-set-valued-property-membership **when** the governed property is set-valued.
5. evaluate **is empty** **and** **is not empty** as absence **and** presence of a governed property value.
6. evaluate **contains**, **starts with**, **and** **ends with** **only** for governed textual property values.
7. evaluate **and** as true **only** **when** **every** argument is true.
8. evaluate **or** as true **when** **`>=1`** argument is true.
9. evaluate **not** as the inverse truth value of its argument.
10. evaluate **if** ... **then** as false **only** **when** its antecedent is true **and** its consequent is false.
11. evaluate **every** as true **only** **when** its predicate is true for **every** member of its population.
12. evaluate **any** as true **when** its predicate is true for **`>=1`** member of its population.
13. evaluate **none** as true **only** **when** its predicate is false for **every** member of its population.
14. evaluate **where** as restriction of one population **to** members whose predicate is true.
15. use another logical function **only** **when** an active CCE Method gives that function **`=1`** logical meaning.

## Details
