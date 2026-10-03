---
tier: core
atom_id: CA-E-207
version: 5
updated_at: "2026-09-05 23:00:00 +0400"
relations:
  child_of:
    - CA-R-815
  evaluation_for:
    - CA-R-860
subjects:
  governs:
    occurrent:
      - "Project/priority model application"
  depends_on:
    continuant:
      - "Operator"
      - "Scope"
      - "Project"
      - "CAPRMEDIO Framework Instance"
cce_version: cce_1
cce_form: evaluation
---
# Evaluate priority-governed alternative selection

## Claim checked

the selected alternative satisfies active constraints **and** the priority model established by the Operator.

## Applicable conditions

apply **when** CAPRMEDIO selects among acceptable alternatives for an affected Scope **and** Project stage.

## Check

resolve the current Operator-selected priority model **and** its parameters under CA-R-860. check the selection against that model **and** **every** active constraint. for a lexicographic selection, check the applicable criterion order under CA-M-131; for another selected model, check that model **without** substituting lexicographic ordering. an unresolved model **or** comparison **must** be returned **to** the Operator.

## Acceptance

pass **only** **when** the selected alternative satisfies **every** active constraint **and** follows the current Operator-selected priority model for that Scope **and** stage. a tie **or** incomparable result **must not** be converted into an automatic winner **without** authority from that model.

## Failure

reject the selection **and** report **every** breached constraint, priority-model mismatch, unauthorized algorithm substitution, **or** automatic selection made while the model **or** its application remains unresolved **to** the Operator.
