---
subjects:
  declared:
    continuant:
      - cce-language
    occurrent:
      - evaluation
cce_version: cce_1
cce_form: method
version: 4
updated_at: 2026-08-29 01:16:37 +0400
relations:
  child_of:
    - CA-M-113
---
# Evaluate condition expressions

**to** evaluate one CCE condition expression, the Resolver **must** PERFORM **all** OF:

1. Evaluate the innermost parenthesized function **before** its containing function.
2. Evaluate **`=`** **and** **`!=`** as exact equality **and** inequality between one governed property **and** one canonical value.
3. Evaluate **`<`**, **`<=`**, **`>`**, **and** **`>=`** **only** for properties with one governed comparison order.
4. Evaluate **in** **and** **not in** as scalar membership **and** non-membership **in** one explicitly parenthesized value list, **or** according to CA-M-127 **when** the governed property is set-valued.
5. Evaluate **is empty** **and** **is not empty** as absence **and** presence of a governed property value.
6. Evaluate **contains**, **starts with**, **and** **ends with** **only** for governed textual property values.
7. Evaluate **and** as true **only** **when** **every** argument is true.
8. Evaluate **or** as true **when** **`>=1`** argument is true.
9. Evaluate **not** as the inverse truth value of its argument.
10. Evaluate **if** ... **then** as false **only** **when** its antecedent is true **and** its consequent is false.
11. Evaluate **every** as true **only** **when** its predicate is true for **every** member of its population.
12. Evaluate **any** as true **when** its predicate is true for **`>=1`** member of its population.
13. Evaluate **none** as true **only** **when** its predicate is false for **every** member of its population.
14. Evaluate **where** as restriction of one population to members whose predicate is true.
15. Use another logical function **only** **when** an active CCE Method gives that function **`=1`** logical meaning.
