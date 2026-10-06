---
atom_id: CA-E-511
content_role: Evaluation
type: QA Case
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Atom/Claim/Target Scope Unit"
  depends_on:
    - "Atom/Claim"
    - "Atom/Scope"
    - "Atom/Subjects"
    - "Current-scope Atom"
    - "Hub Atom"
    - "Operator"
    - "Relational Atom"
    - "Scope Unit"
version: 1
updated_at: "2026-09-23 21:40:21 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-D-477
    - CA-D-482
    - CA-R-1271
    - CA-R-1588
    - CA-R-1595
    - CA-R-1596
    - CA-R-922
    - CA-R-923
---
# Summary

Validate Target Scope Unit and textual Claim Scope

## Claim

### Claim checked

**every** Atom resolves **`=1`** Claim Target Scope Unit; its Claim Scope remains applicability restrictions **in** the Claim text, **not** another structured target **or** metadata Property.

### Test case

create a Current-scope Atom with its own Scope Unit explicitly carried as target **and** a Claim restricted **to** Python files; repeat with a composite restriction. create a permitted Demand with a different explicit target, a parent-owned Goal for its direct child, an Operator-owned Project Goal with an explicit Project target, **and** a Plan inside nested Hubs. **then** omit the internally required target even **when** filename **or** placement identifies its owner, provide two targets, use a Hub as a target, leave the target unresolved, encode Claim Scope as separate metadata, **or** infer a target **or** ownership change from the textual restriction alone.

### Acceptance criteria

valid targets resolve **to** **`=1`** Scope Unit. authoring defaults select **and** carry the current Scope Unit **where** one exists; reading does **not** repair an omitted target from placement; external Project Goals retain their explicit target. narrower **or** composite applicability alone leaves a Current-scope Atom Current-scope. a different permitted target yields a Relational Atom **without** transferring ownership **or** changing Scope Unit ancestry. Hub nesting does **not** create another target. **every** invalid fixture fails with the exact missing, unresolved, duplicate, misclassified, **or** independently duplicated fact identified.

### Failure disposition

report the affected Atom **and** target, ownership, **or** Claim-text distinction; preserve the source **until** an authorized correction is selected.
