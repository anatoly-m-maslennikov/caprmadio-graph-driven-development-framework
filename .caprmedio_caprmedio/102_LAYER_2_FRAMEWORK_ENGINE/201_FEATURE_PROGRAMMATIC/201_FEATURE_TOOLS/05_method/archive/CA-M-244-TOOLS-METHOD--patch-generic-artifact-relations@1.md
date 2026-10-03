---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - artifact-operations
version: 1
updated_at: 2026-09-02 00:25:00 +0400
relations:
  method_for:
    - CA-R-1131
  derived_from:
    - CA-A-058
---
# Patch generic Artifact relations

## Applicable when

Use this Method when a governed Tool needs generic mechanics to add, replace, or remove explicitly selected typed relation targets on one Artifact.

## Procedure

1. Resolve one source Artifact, seal its path, revision, digest, existing relation targets, and `relational_endpoints` descriptors.
2. Normalize each requested target to a canonical project-graph node reference; resolve a relative Scope Unit reference from the source Artifact owner using its exact full name.
3. Validate the requested relation kind, source and target classes, direction, lifecycle, cardinality, Content-role applicability, and endpoint identity.
4. Produce the complete relation-only dry-run; reject an invalid target or descriptor without changing any relation or body byte.
5. On authorized apply, recheck the sealed preconditions, atomically write only the validated relation and endpoint changes, advance revision metadata once, and preserve the body digest.

## Outcome

One generic Artifact receives exactly the validated direct relation-target and endpoint-descriptor changes while its body and unrelated metadata remain unchanged.

## Failure or stop

Stop or roll back on an unresolved reference, invalid relation policy, stale source, failed precondition, or any requested body or unrelated-field change.
