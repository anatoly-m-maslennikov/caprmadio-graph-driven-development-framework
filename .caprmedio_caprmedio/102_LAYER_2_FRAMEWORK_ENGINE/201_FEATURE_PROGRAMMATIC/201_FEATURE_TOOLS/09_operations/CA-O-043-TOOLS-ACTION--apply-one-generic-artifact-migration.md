---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Apply Generic Artifact Migration"
  depends_on:
    - "Action"
    - "Artifact"
    - "Artifact/Carrier"
    - "Artifact/Revision"
    - "Relation"
    - "Journal/Record"
version: 3
updated_at: "2026-09-17 03:35:21 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Apply one generic Artifact migration

Apply Generic Artifact Migration **means** the reusable Action that produces one complete approved generic Carrier-and-reference migration with its required attributable Journal evidence, **or** restoration of the complete prior mutable Carrier-and-reference state under CA-R-1139. its modeled boundary is the complete selected mutable-state transition; a partial application is **not** an independently accepted result.

## Applicable when

use this Action **when** one approved generic Artifact migration plan **must** be applied against its unchanged recorded preconditions.

## Action

1. resolve the approved migration plan **and** seal its plan digest, source preconditions, carrier mappings, **and** required reference mutations.
2. recheck **every** recorded precondition against the current source frontier **and** reject **any** changed, missing, **or** additional required source fact.
3. construct one transaction containing exactly the approved carrier **and** reference mutations; exclude unplanned effects.
4. apply the transaction rollbackably, appending the governed migration event through the Work Journal Tool **only** **after** **all** mutation effects succeed.
5. return the applied transaction identity **and** exact resulting frontier **without** interpreting it as a CAPRMEDIO Atom migration.

## Outcome

one approved unchanged generic Artifact migration is applied as one rollbackable carrier-**and**-reference transaction with attributable Work Journal evidence.

## Failure or stop

do **not** apply an unapproved **or** stale plan; roll back **every** carrier **and** reference mutation on **any** failed effect **or** Journal append failure.
