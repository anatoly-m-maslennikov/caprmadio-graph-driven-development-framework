---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Transition Generic Artifact Lifecycle"
  depends_on:
    - "Action"
    - "Artifact"
    - "Artifact/Carrier"
    - "Artifact/Revision"
    - "Relation"
version: 2
updated_at: "2026-09-17 03:33:08 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Transition one generic Artifact lifecycle

Transition Generic Artifact Lifecycle **means** the reusable Action that produces one complete authorized transition **in** the selected registered generic Artifact lifecycle model, **or** restoration of the complete prior mutable state under CA-R-1134. its modeled boundary is the complete selected mutable-state transition; a partial application is **not** an independently accepted result.

## Applicable when

use this Action **when** one generic Artifact **must** traverse one transition defined by its registered lifecycle state model.

## Action

1. resolve one source carrier, its current lifecycle state, **and** the requested target state against the registered lifecycle model.
2. reject an undefined, ambiguous, **or** disallowed transition **before** creating a destination directory **or** changing a carrier.
3. derive the permitted destination, lazily create that directory **only** **when** the transition is valid, **and** determine required metadata **and** canonical-reference updates.
4. expose the complete transition dry-run with source, destination, state change, metadata change, **and** reference rewrites.
5. on authorized apply, move the carrier **and** apply required metadata **and** reference updates as one rollbackable transaction, **then** verify the registered target state.

## Outcome

one generic Artifact completes one registered lifecycle transition with valid destination, required metadata, **and** canonical references.

## Failure or stop

fail closed on an undefined **or** ambiguous state model, disallowed transition, collision, stale source, **or** failed rewrite; do **not** substitute this helper for a CAPRMEDIO Atom lifecycle operation.
