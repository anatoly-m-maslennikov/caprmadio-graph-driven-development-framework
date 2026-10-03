---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Patch Generic Artifact Relations"
  depends_on:
    - "Action"
    - "Artifact"
    - "Artifact/Carrier"
    - "Artifact/Revision"
    - "Relation"
    - "Scope Unit"
version: 4
updated_at: "2026-09-17 03:32:31 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Patch generic Artifact relations

Patch Generic Artifact Relations **means** the reusable Action that produces one complete authorized relation-only change **to** one generic Artifact, **or** no accepted partial change under CA-R-1131. its modeled boundary is the complete selected mutable-state transition; a partial application is **not** an independently accepted result.

## Applicable when

use this Action **when** a governed Tool needs generic mechanics **to** add, replace, **or** remove explicitly selected typed relation targets on one Artifact.

## Action

1. resolve one source Artifact, seal its path, revision, digest, existing relation targets, **and** `relational_endpoints` descriptors.
2. normalize **every** requested target **to** a canonical project-graph node reference; resolve a relative Scope Unit reference from the source Artifact owner using its exact full name.
3. validate the requested relation kind, source **and** target classes, direction, lifecycle, cardinality, Content-role applicability, **and** endpoint identity.
4. produce the complete relation-only dry-run; reject an invalid target **or** descriptor **without** changing **any** relation **or** body byte.
5. on authorized apply, recheck the sealed preconditions, atomically write **only** the validated relation **and** endpoint changes, advance revision metadata once, **and** preserve the body digest.

## Outcome

one generic Artifact receives exactly the validated direct relation-target **and** endpoint-descriptor changes while its body **and** unrelated metadata remain unchanged.

## Failure or stop

stop **or** roll back on an unresolved reference, invalid relation policy, stale source, failed precondition, **or** **any** requested body **or** unrelated-field change.
