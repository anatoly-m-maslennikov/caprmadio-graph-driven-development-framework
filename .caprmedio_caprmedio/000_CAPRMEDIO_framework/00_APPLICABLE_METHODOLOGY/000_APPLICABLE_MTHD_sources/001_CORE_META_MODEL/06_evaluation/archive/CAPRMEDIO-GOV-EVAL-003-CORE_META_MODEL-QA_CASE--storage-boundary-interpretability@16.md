---
subjects:
  governs: "Carrier"
  depends_on:
    - "Atom"
    - "Artifact"
    - "Journal"
    - "Journal/Record"
    - "Work Journal/Event"
    - "Projection"
    - "Workflow"
    - "Scope Unit"
    - "Atom/Content Role"
    - "Operator"
    - "Runtime State"
version: 16
updated_at: "2026-09-18 14:16:20 +0000"
relations:
  evaluation_for:
    - CAPRMEDIO-META-REQU-656
    - CA-R-1463
    - CA-D-308
    - CA-R-1467
    - CA-R-1468
    - CA-D-341
    - CAPRMEDIO-META-REQU-158
---
# Storage-boundary interpretability

## Claim checked

an Operator can place an Atom, Journal Record, resumable checkpoint, generated cache, **and** disposable workspace **in** the governed storage boundary **and** explain its retention behavior.

## Applicable conditions

the available boundaries are the applicable Project authority root, Framework control root, Runtime State, **and** the host temporary root. workflow **and** Implementation events use the shared Project Work Journal through its D-defined Project-wide Carrier; Scope Units **and** Content Roles do **not** receive separate authoritative Journals.

## Acceptance criteria

**`>=90`**% of classifications are correct **and** no classification treats runtime **or** scratch as canonical truth.

the Evaluation **must** fail **if** placement creates a separate authoritative Journal for a workflow, Scope Unit, **or** Content Role; this check is required regardless of the aggregate classification score. multiple storage segments **in** the selected Journal Carrier **must** be classified as Carriers of the same Journal, **not** additional Journals. the Artifact Change Log **and** Process Log **must** be classified as non-authoritative Projections of that Journal, **not** separate historical sources.

## Journal-view fixtures

use one admitted Artifact-change event associated with an execution **and** one admitted read-only execution event. derive an artifact-change view **and** a Workflow-execution view from the same Journal selection. the first event **may** appear **in** both views with the same canonical Event identity; the read-only execution **must not** require a fabricated Artifact-change event.

reject a fixture that independently writes history into either view, creates a second authoritative record merely **to** serve the other view, changes a represented fact **without** its source record, invents an execution association **or** successful outcome, treats a record as proof that its claimed outcome occurred, **or** reports known incomplete **or** stale coverage as complete current history. rebuilding either view from the same declared Journal selection **must** preserve its source event references **and** represented historical facts. this mandatory Journal-view check is independent of the aggregate storage-classification score.


## Failure disposition

record a Concern for **every** ambiguous boundary **and** stop storage-boundary readiness **until** the governing rule **or** its presentation is corrected.
