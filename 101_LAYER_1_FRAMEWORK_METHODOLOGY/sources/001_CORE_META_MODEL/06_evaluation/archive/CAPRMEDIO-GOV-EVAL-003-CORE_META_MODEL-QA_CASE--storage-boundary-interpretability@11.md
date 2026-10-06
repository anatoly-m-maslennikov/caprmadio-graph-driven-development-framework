---
atom_id: CAPRMEDIO-GOV-EVAL-003
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - evaluation
version: 11
updated_at: "2026-09-10 22:35:50 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-D-339
    - CA-D-341
    - CAPRMEDIO-META-REQU-158
---
# Storage-boundary interpretability

## Claim checked

an Operator can place an Atom, Journal Record, resumable checkpoint, generated cache, **and** disposable workspace **in** the governed storage boundary **and** explain its retention behavior.

## Applicable conditions

the available boundaries are the applicable Project authority root, Framework control root, Runtime State, **and** the host temporary root. workflow **and** Implementation events use the shared Project Work Journal **in** its D-defined Project-wide directory; Scope Units **and** Content Roles do **not** receive separate authoritative Journals.

## Acceptance criteria

**`>=90`**% of classifications are correct **and** no classification treats runtime **or** scratch as canonical truth.

the Evaluation **must** fail **if** placement creates a separate authoritative Journal for a workflow, Scope Unit, **or** Content Role; this check is required regardless of the aggregate classification score. multiple NDJSON segments **in** the registered directory **must** be classified as Carriers of the same Journal, **not** additional Journals.

## Failure disposition

record a Concern for **every** ambiguous boundary **and** stop storage-boundary readiness **until** the governing rule **or** its presentation is corrected.
