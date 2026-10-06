---
version: 10
updated_at: "2026-09-17 17:40:18 +0000"
relations:
  child_of:
    - CA-R-815
  evaluation_for:
    - CA-R-1487
    - CA-M-297
    - CA-O-022
    - CA-O-023
subjects:
  governs: "Project/priority model application"
  depends_on:
    - "Operator"
    - "Scope"
    - "Project"
    - "CAPRMEDIO Framework Instance"
    - "Resolve Operator Priorities"
    - "Select Priority-Governed Alternative"
    - "Project/lexicographic selection"
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Evaluate priority-governed alternative selection

## applicability

this Evaluation checks priority resolution **and** alternative selection for an affected Scope **and** Project stage under CA-R-1487, CA-M-297, CA-O-022, **and** CA-O-023.

## acceptance

the evaluated behavior passes **if** **all** applicable conditions hold **and** are supported by the evaluated evidence:

- the effective model **and** parameters correspond **to** applicable Operator input; unresolved input is reported **without** activating an invented model **or** preference.
- **every** selected alternative satisfies active authority **and** non-negotiable constraints.
- selection follows the Operator-selected model **without** substituting another algorithm.
- for comparison by priority order, the first deciding criterion governs relative preference; later criteria do **not** reverse it **or** bypass an unresolved earlier comparison.
- a tie **or** incomparable result is **not** converted into an automatic winner **without** authority from the selected model.
- unresolved input **or** comparison is returned **to** the Operator with its known inputs, alternatives **when** available, constraints, evidence, **and** exact unresolved point.

## falsification

the evaluated behavior fails **if** **any** applicable acceptance condition is false. missing evidence for an applicable condition leaves that condition unevaluated, **not** passed.
