---
subjects:
  declared:
    continuant:
      - scope-topology
  prerequisite:
    continuant:
      - cce-language
cce_version: cce_1
cce_form: method
version: 2
updated_at: 2026-08-25 01:20:06
relations: {}
---
# Evaluate Scope Expressions

**to** evaluate one Scope Expression, the Resolver **must** perform **all** of:

1. resolve each exact Atom ID **or** other atomic identity to **exactly one** governed entity.
2. interpret **all** `<ENTITY_KIND>` as **every** governed entity of that kind within Current Scope.
3. interpret **or** as set union.
4. interpret **and** as set intersection.
5. interpret **without** as left-side set exclusion.
6. interpret **where** as retention of only members whose property predicate evaluates to true according to CA-M-122.
7. evaluate the innermost parenthesized set function before its containing set function.
8. use another Scope function only when an active CCE Method gives that function **exactly one** set meaning.
