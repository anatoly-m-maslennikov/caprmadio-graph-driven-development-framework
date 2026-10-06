---
version: 1
updated_at: "2026-09-15 21:00:34 +0400"
relations:
  child_of:
    - CA-R-1487
  relates_to:
    - CA-O-022
    - CA-M-293
subjects:
  governs: "Select Priority-Governed Alternative"
  depends_on:
    - "Action"
    - "Operator"
    - "Resolve Operator Priorities"
    - "Project/priority model application"
    - "Project/lexicographic selection"
cce_version: cce_1
cce_form: definition
---
# Select an alternative under active priorities

Select Priority-Governed Alternative **means** the Action that applies resolved Operator priorities **to** candidate alternatives **and** returns a justified selection **or** an unresolved comparison.

## execution

1. obtain the effective priorities resolved under CA-O-022 for the affected context. unresolved priorities do **not** authorize selection.
2. reject **every** candidate that violates applicable authority **or** a non-negotiable constraint.
3. apply the selected model **to** the remaining alternatives using the available evidence. use CA-M-293 **only** for an Operator-selected lexicographic model; use the selected technique for another model.
4. return a selected alternative **only** **when** that model justifies the choice. retain the constraints, criterion evidence, **and** comparison result that justify it.

## unresolved comparison

**if** no admissible alternative remains **or** the model does **not** determine a selection:

- report the alternatives, constraints, evidence, **and** unresolved comparison **to** the Operator.
- identify incomplete criterion order, unresolved ties, **or** incomparable results **when** applicable.
- do **not** invent a tie-break, substitute an algorithm, **or** return an unsupported winner.

**if** the Operator changes the applicable priorities, use the newly resolved result under CA-O-022 **before** comparing again.
