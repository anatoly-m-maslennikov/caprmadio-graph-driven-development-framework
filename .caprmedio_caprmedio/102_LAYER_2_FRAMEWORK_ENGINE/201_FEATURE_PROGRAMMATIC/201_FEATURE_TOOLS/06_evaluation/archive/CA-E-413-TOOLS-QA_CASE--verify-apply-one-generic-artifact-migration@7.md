---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Apply Generic Artifact Migration"
  depends_on:
    - "Action"
    - "Artifact"
    - "Artifact/Carrier"
    - "Artifact/Revision"
    - "Relation"
    - "Journal/Record"
version: 7
updated_at: "2026-09-17 03:35:21 +0000"
relations: {"evaluation_for":["CA-R-1139","CA-O-043"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify apply one generic Artifact migration

## Claim checked

CA-O-043 applies **only** an approved unchanged generic migration plan as one rollbackable transaction with attributable Work Journal evidence.

## Applicable when

Apply whenever generic migration precondition checking, transaction construction, rollback, **or** Work Journal append mechanics change.

## Test case

Prepare one approved two-carrier migration plan with one reference rewrite. Change one recorded precondition **before** an apply attempt, **then** restore it **and** apply the unchanged approved plan.

## Acceptance criteria

the stale attempt changes no carrier **or** reference **and** appends no migration event. The valid attempt applies **every** planned effect once, appends one attributable migration event, **and** exposes one transaction identity.

## Failure disposition

Reject the realization **and** preserve plan digest, precondition comparison, carrier **and** reference diffs, Work Journal evidence, transaction identity, **and** rollback evidence.

## Post-effect failure coverage

from an independent exact before-state, inject a failure **after** **>=1** planned Carrier **or** reference change **and** **before** the migration completes. also exercise a Journal append failure **after** the planned mutations succeed, under CA-O-043's declared recovery boundary.

- verify restoration of **every** planned mutable Carrier **and** reference **to** the before-state, with unrelated targets unchanged.
- distinguish rejected preflight, failed apply, failed Journal append, successful recovery, **and** incomplete recovery. **none** is an applied-migration success merely because the plan was valid.
- accepted Journal Records remain immutable under CA-R-1491. preserve actual mutation **and** recovery evidence; rollback of mutable Carriers **must not** erase an accepted event **or** recast it as current state.
- prove the injected fault follows a real selected effect. preflight rejection alone does **not** satisfy recovery coverage; incomplete **or** unverified restoration fails the claimed rollback guarantee.
