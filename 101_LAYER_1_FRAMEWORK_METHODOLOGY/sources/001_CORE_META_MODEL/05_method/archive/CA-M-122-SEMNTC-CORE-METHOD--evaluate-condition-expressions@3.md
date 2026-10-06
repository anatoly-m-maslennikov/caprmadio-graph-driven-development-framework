---
subjects:
  declared:
    continuant:
      - cce-language
    occurrent:
      - evaluation
cce_version: cce_1
cce_form: method
version: 3
updated_at: 2026-08-23 15:00:38
relations:
  child_of:
    - CA-M-113
---
# Evaluate condition expressions

TO evaluate one CCE condition expression, the Resolver MUST PERFORM ALL OF:

1. Evaluate the innermost parenthesized function before its containing function.
2. Evaluate `=` and `!=` as exact equality and inequality between one governed property and one canonical value.
3. Evaluate `<`, `<=`, `>`, and `>=` only for properties with one governed comparison order.
4. Evaluate `IN` and `NOT IN` as scalar membership and non-membership in one explicitly parenthesized value list, or according to CA-M-127 when the governed property is set-valued.
5. Evaluate `IS EMPTY` and `IS NOT EMPTY` as absence and presence of a governed property value.
6. Evaluate `CONTAINS`, `STARTS WITH`, and `ENDS WITH` only for governed textual property values.
7. Evaluate `AND` as true only when every argument is true.
8. Evaluate `OR` as true when at least one argument is true.
9. Evaluate `NOT` as the inverse truth value of its argument.
10. Evaluate `IF ... THEN` as false only when its antecedent is true and its consequent is false.
11. Evaluate `EVERY` as true only when its predicate is true for every member of its population.
12. Evaluate `ANY` as true when its predicate is true for at least one member of its population.
13. Evaluate `NONE` as true only when its predicate is false for every member of its population.
14. Evaluate `WHERE` as restriction of one population to members whose predicate is true.
15. Use another logical function only when an active CCE Method gives that function exactly one logical meaning.
