---
subjects:
  governs:
    continuant:
      - cce-language
    occurrent:
      - evaluation
cce_version: cce_1
cce_form: method
version: 3
updated_at: 2026-08-29 02:40:41 +0400
relations: {}
---
# Evaluate condition expressions

**to** evaluate one CCE condition expression, the Resolver **must** perform **all** of:

1. evaluate the innermost parenthesized function before its containing function.
2. evaluate **=** **and** **!=** as exact equality **and** inequality between one governed property **and** one canonical value.
3. evaluate **<**, **<=**, **>**, **and** **>=** only for properties with one governed comparison order.
4. evaluate **in** **and** **not in** as scalar membership **and** non-membership in one explicitly parenthesized value list, **or** according to CA-M-127 when the governed property is set-valued.
5. evaluate **is empty** **and** **is not empty** as absence **and** presence of a governed property value.
6. evaluate **contains**, **starts with**, **and** **ends with** only for governed textual property values.
7. evaluate **and** as true only when **every** argument is true.
8. evaluate **or** as true when at least one argument is true.
9. evaluate **not** as the inverse truth value of its argument.
10. evaluate **if** ... **then** as false only when its antecedent is true **and** its consequent is false.
11. evaluate **every** as true only when its predicate is true for **every** member of its population.
12. evaluate **any** as true when its predicate is true for at least one member of its population.
13. evaluate **none** as true only when its predicate is false for **every** member of its population.
14. evaluate **where** as restriction of one population to members whose predicate is true.
15. use another logical function only when an active CCE Method gives that function **exactly one** logical meaning.
