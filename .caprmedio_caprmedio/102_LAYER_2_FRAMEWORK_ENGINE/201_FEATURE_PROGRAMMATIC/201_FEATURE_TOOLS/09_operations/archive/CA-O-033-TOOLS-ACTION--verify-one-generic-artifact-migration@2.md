---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Verify Artifact Migration"
  depends_on:
    - "Action"
    - "Artifact"
    - "Artifact/Revision"
    - "Relation"
    - "Projection"
    - "Journal/Record"
version: 2
updated_at: "2026-09-17 03:14:49 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Verify one generic Artifact migration

Verify Artifact Migration **means** the reusable Action that produces a complete read-**only** postcondition report for one applied Artifact migration under CA-R-1140. its modeled boundary is the complete requested result; partial comparison, incomplete attribution, **or** an unreported unresolved input is **not** an independently successful outcome.

## Applicable when

use this Action **when** an applied generic Artifact migration plan requires a read-**only** postcondition replay.

## Action

1. resolve the applied migration plan, its declared postconditions, **and** the recorded applied transaction identity.
2. inspect the current carriers, typed references, affected Projections, **and** Work Journal evidence named by the plan **without** mutating them.
3. compare **every** observed result with the declared postconditions **and** classify each residual old state, unexpected mutation, **and** unmapped identity.
4. attribute **every** finding **to** the relevant plan condition, observed carrier **or** evidence, **and** current digest **or** revision.
5. return a complete verification result **without** repairing discrepancies **or** deciding semantic adoption.

## Outcome

one read-**only** migration-verification result reports whether **every** declared postcondition holds **and** identifies **every** residual, unexpected, **or** unmapped state.

## Failure or stop

do **not** mutate carriers, references, Projections, **or** Journals; report an explicit blocked result **when** the applied plan **or** required evidence cannot be resolved.
