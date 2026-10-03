---
version: 5
updated_at: "2026-09-15 19:54:51 +0400"
relations:
  child_of:
    - CA-R-815
  method_for:
    - CA-R-860
subjects:
  governs: "Project/lexicographic selection"
  depends_on:
    - "Operator"
    - "Scope"
    - "Project"
    - "Atom/Content Role: Method"
cce_version: cce_1
cce_form: method
atom_id: CA-M-131
---
# Apply lexicographic selection when selected

## applicability

use this comparison **only** **when** the Operator has selected a lexicographic priority model for the affected Scope **and** Project stage. it **must not** replace a different Operator-selected priority model.

## selection

1. resolve the selected model **and** its effective criterion order under CA-R-860.
2. reject **every** alternative that violates a non-negotiable constraint.
3. compare the remaining alternatives using **every** active, applicable Operator-priority criterion **in** the resolved order. the current criterion set includes CA-M-093 through CA-M-100 **and** remains extensible.
4. choose the alternative that is strictly preferred at the first criterion **where** admissible alternatives differ.

## unresolved comparison

report the alternatives, constraints, evidence, **and** unresolved comparison **to** the Operator **if** **any** of the following applies:

- the criterion order is incomplete.
- alternatives remain tied **after** **all** applicable criteria.
- criteria are incomparable.

do **not** break a tie **or** infer a preference automatically.
