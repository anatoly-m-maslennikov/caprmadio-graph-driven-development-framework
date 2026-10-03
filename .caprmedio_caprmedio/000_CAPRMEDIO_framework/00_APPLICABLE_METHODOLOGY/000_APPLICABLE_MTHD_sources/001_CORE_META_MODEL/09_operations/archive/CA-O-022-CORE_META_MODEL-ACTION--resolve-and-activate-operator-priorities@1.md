---
version: 1
updated_at: "2026-09-15 21:00:34 +0400"
relations:
  child_of:
    - CA-R-1487
subjects:
  governs: "Resolve Operator Priorities"
  depends_on:
    - "Action"
    - "Operator"
    - "Project"
    - "Scope"
    - "CAPRMEDIO Framework Instance"
    - "Project/priority model application"
cce_version: cce_1
cce_form: definition
---
# Resolve and activate Operator priorities

Resolve Operator Priorities **means** the Action that turns applicable Operator input into the effective priority model for an identified Scope **and** Project stage.

## execution

1. identify the affected Scope **and** Project stage from the Operator input **and** its applicable context.
2. resolve the Operator-selected model, effective parameters, active criteria, applicable authority, **and** non-negotiable constraints. retain **every** applicable criterion **without** imposing a fixed catalog **or** lexicographic order on another model.
3. check whether the input determines an admissible model **and** the parameters needed **to** apply it.
4. **if** that resolution succeeds, activate the resolved priorities in the CAPRMEDIO Framework Instance for the identified context **and** return them as the Action result.

## unresolved input

**if** the selected model, required parameters, authority, **or** context remains unresolved:

- present the known input **and** the exact unresolved point **to** the Operator.
- do **not** invent a model, infer a missing preference, **or** activate an unresolved change.
- report the Action as unresolved, **not** successfully completed.
