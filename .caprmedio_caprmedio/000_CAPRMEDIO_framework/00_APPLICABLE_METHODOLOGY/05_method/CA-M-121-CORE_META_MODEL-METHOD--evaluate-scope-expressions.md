---
subjects:
  governs: "Scope Expression Evaluation"
  depends_on:
    - "Scope Expression"
version: 17
updated_at: "2026-09-29 22:34:56 +0000"
relations: {}
atom_id: "CA-M-121"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-121-CORE_META_MODEL-METHOD--evaluate-scope-expressions.md
  source_atom_id: CA-M-121
  source_atom_revision: 17
  source_sha256: 6b5139e9e507051863dcac7faa4eb75fb70cd38592e68bf05914e9dc6accdb14
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary
Evaluate Scope Expressions

## Scope
evaluation of a Scope Expression.

## Claim
**to** evaluate one Scope Expression, the Resolver **must** perform **all** of:

1. resolve **every** exact Atom ID **or** other atomic identity **to** **`=1`** Governed Entity.
2. interpret **all** `<ENTITY_KIND>` as **every** Governed Entity of that kind within Atom Scope.
3. interpret **or** as set union.
4. interpret **and** as set intersection.
5. interpret **without** as left-side set exclusion.
6. interpret **where** as retention of **only** members whose field predicate evaluates **to** true according **to** `CA-M-122-CORE_META_MODEL-METHOD--evaluate-condition-expressions`.
7. evaluate the innermost parenthesized set function **before** its containing set function.
8. use another Scope function **only** **when** an active CCE Method gives that function **`=1`** set meaning.

## Details
