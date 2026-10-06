---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Atom/Claim/Target Scope Unit"
  depends_on:
    - "Atom/Scope"
    - "Atom/Claim"
    - "Atom/Subjects"
    - "Current-scope Atom"
    - "Relational Atom"
    - "Scope Unit"
    - "Operator"
    - "Hub Atom"
version: 2
updated_at: "2026-09-22 17:59:17 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"evaluation_for": ["CA-R-1595", "CA-R-1596", "CA-R-922", "CA-R-923", "CA-R-1271", "CA-R-1588", "CA-D-476", "CA-D-477"]}
---
# Validate Target Scope Unit and textual Claim Scope

## Claim checked

**every** Atom resolves **`=1`** Claim Target Scope Unit; its Claim Scope remains applicability restrictions **in** the Claim text, **not** another structured target **or** metadata Property.

## Test case

create a Current-scope Atom with an omitted target **and** a Claim restricted **to** Python files; repeat with a composite restriction. create a permitted Demand with a different explicit target, a parent-owned Goal for its direct child, an Operator-owned Project Goal with an explicit Project target, **and** a Plan inside nested Hubs. **then** omit a required target, provide two targets, use a Hub as a target, leave the target unresolved, encode Claim Scope as separate metadata, **or** infer a target **or** ownership change from the textual restriction alone.

## Acceptance criteria

valid targets resolve **to** **`=1`** Scope Unit. omission uses the current Scope Unit **where** one exists; external Project Goals retain their explicit target. narrower **or** composite applicability alone leaves a Current-scope Atom Current-scope. a different permitted target yields a Relational Atom **without** transferring ownership **or** changing Scope Unit ancestry. Hub nesting does **not** create another target. **every** invalid fixture fails with the exact missing, unresolved, duplicate, misclassified, **or** independently duplicated fact identified.

## Failure disposition

report the affected Atom **and** target, ownership, **or** Claim-text distinction; preserve the source **until** an authorized correction is selected.
