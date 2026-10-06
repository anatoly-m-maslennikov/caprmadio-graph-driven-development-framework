---
subjects:
  governs: "CCE Claim and Projection Validation"
  depends_on:
    - "Atom/Claim"
    - "Atom/Summary"
    - "Translation"
    - "Confidence Threshold"
    - "Operator"
    - "Atom/Content Role: Plan/Type: Task"
    - "Epic"
    - "Framework Instance Settings"
cce_version: cce_1
cce_form: evaluation
version: 17
updated_at: "2026-09-17 14:24:34 +0000"
relations: {"evaluation_for":["CA-M-111","CA-M-115","CA-M-114","CA-M-271","CA-O-050","CA-R-940","CA-R-941","CA-R-1273"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate CCE Claims and derived Projections

## Claim checked

**every** active **or** draft Atom **contains** **`=1`** human-readable precise CCE Claim **and** a source-faithful Summary. requested Translation **and** terminology Projections preserve their source meaning; their absence **when** **not** requested is **not** an Atom defect.

## Test case

create valid active **and** draft Atom Claims for **every** admitted Content Role. include fixtures with no requested Translation **or** terminology Projection **and** fixtures with requested Projections. derive a candidate Summary during Atom creation, **then** retain it for checks of subsequent Revisions under CA-E-463. derive requested Translation **and** terminology Projections twice **without** regenerating the existing Atom's Summary. **then** introduce ambiguity, an unstated participant, two independent Claims, an added Projection meaning, an independent vocabulary entry, **and** a confidence result below the effective Confidence Threshold resolved according **to** CA-M-271.

## Acceptance criteria

**every** valid fixture has **`=1`** precise interpretation, a source-faithful Summary, **and** reproducible Projections **when** requested. no fixture fails merely because an optional Projection was **not** requested. **every** invalid fixture fails. a confidence result below the effective Confidence Threshold leaves the Atom unchanged **and** requests Operator disposition. changing the applicable Operator input, Task override, enclosing Epic override, **or** Framework Instance Settings default changes the checked threshold according **to** CA-M-271 **without** retaining a fixed percentage gate.

## Failure disposition

record a Concern naming the affected Claim **or** Projection.
