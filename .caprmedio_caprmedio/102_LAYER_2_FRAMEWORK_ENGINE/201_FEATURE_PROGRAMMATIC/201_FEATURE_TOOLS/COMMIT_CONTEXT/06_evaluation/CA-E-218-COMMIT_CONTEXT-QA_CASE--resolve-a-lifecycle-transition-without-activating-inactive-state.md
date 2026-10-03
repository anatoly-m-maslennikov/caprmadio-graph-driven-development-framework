---
subjects:
  governs: "Artifact/Revision/Status"
  depends_on: []
version: 12
updated_at: "2026-09-17 03:16:58 +0000"
relations: {"evaluation_for":["CA-R-803","CA-R-804","CAPRMEDIO-GOV-REQU-767","CA-R-1491"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
cce_version: cce_1
cce_form: evaluation
---
# Resolve a lifecycle transition without activating inactive state

## Claim checked

context gathering preserves **`=1`** observable lifecycle transition **without** promoting an inactive Atom **to** current authority. historical lookup **and** typed Relation resolution are distinct from active-authority selection.

## Test cases

1. prepare a fixture with **`=1`** committed active Plan Atom, another already-done Plan Atom, **and** **`=1`** solved Concern. move the active Plan Carrier byte-for-byte **to** its registered `done/` location **and** observe the exact before/after paths **and** digests.
2. gather context for that transition. separately inspect the available historical Carriers **and** **any** references **to** them, retaining the governing Relation Kind **and** source/target Content Roles rather than using a global inactive-directory exclusion.
3. supply an Active RMED-to-RMED relation targeting an inactive RMED Atom **and** an **otherwise** equivalent relation targeting an Active RMED Atom. apply CAPRMEDIO-GOV-REQU-767 **to** that qualified relation domain.

## Acceptance criteria

- the adapter retains **`=1`** unclassified trigger with both observed paths. COMMIT_CONTEXT resolves **`=1`** Plan identity **and** **`=1`** `MOVE`, using the fixture's committed active Carrier as prior evidence **and** its exact done Carrier as resulting evidence.
- done **and** solved Carriers do **not** enter active authority. their exclusion from active authority does **not** erase their historical evidence **or** make **every** reference **to** them invalid.
- resolve a reference under its admitted graph-qualified Relation Kind, endpoint classes, **and** lifecycle constraints. a historically admitted reference remains historical; it does **not** activate its endpoint. missing Relation authority yields an explicit unresolved result, **not** invented admission.
- the inactive RMED target fails the active RMED-to-RMED constraint. that constraint is **not** extended automatically **to** **all** Plan, Concern, Journal, **or** historical references.
- exact observed lifecycle evidence remains recordable under CA-R-1491 despite an unresolved **or** nonconforming Project reference. context gathering does **not** repair the reference **or** mutate either Carrier.

## Failure disposition

reject a realization **if** it suppresses the event because of a lifecycle directory, splits one observed identity into two, classifies from a hard-coded directory list, admits inactive current authority, deletes historical evidence, **or** applies an unqualified active-only filter **to** **all** reference resolution. retain the registration, paths, digests, reference kinds, endpoint classifications, **and** distinct lookup/conformance results.
