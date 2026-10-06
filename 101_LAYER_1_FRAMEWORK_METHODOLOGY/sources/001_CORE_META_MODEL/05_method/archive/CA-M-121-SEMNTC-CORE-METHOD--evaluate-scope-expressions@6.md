---
atom_id: CA-M-121
subjects:
  governs:
    occurrent:
      - Scope Expression Evaluation
  depends_on:
    continuant:
      - Scope Expression
cce_version: cce_1
cce_form: method
version: 6
updated_at: 2026-08-29 01:16:37 +0400
relations: {}
---
# Evaluate Scope Expressions

**to** evaluate one Scope Expression, the Resolver **must** perform **all** of:

1. resolve **every** exact Atom ID **or** other atomic identity to **`=1`** Governed Entity.
2. interpret **all** `<ENTITY_KIND>` as **every** Governed Entity of that kind within Current Scope.
3. interpret **or** as set union.
4. interpret **and** as set intersection.
5. interpret **without** as left-side set exclusion.
6. interpret **where** as retention of **only** members whose field predicate evaluates to true according to CA-M-122.
7. evaluate the innermost parenthesized set function **before** its containing set function.
8. use another Scope function **only** **when** an active CCE Method gives that function **`=1`** set meaning.
