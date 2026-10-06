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
version: 4
updated_at: 2026-08-23 15:24:07
relations:
  child_of:
    - CA-M-113
    - CA-M-122
    - CA-R-999
    - CA-R-1006
---
# Evaluate Scope Expressions

TO evaluate one Scope Expression, the Resolver MUST PERFORM ALL OF:

1. Resolve each exact Atom ID or other atomic identity to exactly one governed entity.
2. Interpret `ALL <ENTITY_KIND>` as every governed entity of that kind within Current Scope.
3. Interpret `OR` as set union.
4. Interpret `AND` as set intersection.
5. Interpret `WITHOUT` as left-side set exclusion.
6. Interpret `WHERE` as retention of only members whose property predicate evaluates to true according to CA-M-122.
7. Evaluate the innermost parenthesized set function before its containing set function.
8. Use another Scope function only when an active CCE Method gives that function exactly one set meaning.
