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
    - CA-R-1134
  derived_from:
    - CA-A-058
---
# Transition one generic Artifact lifecycle

## Applicable when

Use this Method when one generic Artifact must traverse one transition defined by its registered lifecycle state model.

## Procedure

1. Resolve one source carrier, its current lifecycle state, and the requested target state against the registered lifecycle model.
2. Reject an undefined, ambiguous, or disallowed transition before creating a destination directory or changing a carrier.
3. Derive the permitted destination, lazily create that directory only when the transition is valid, and determine required metadata and canonical-reference updates.
4. Expose the complete transition dry-run with source, destination, state change, metadata change, and reference rewrites.
5. On authorized apply, move the carrier and apply required metadata and reference updates as one rollbackable transaction, then verify the registered target state.

## Outcome

One generic Artifact completes one registered lifecycle transition with valid destination, required metadata, and canonical references.

## Failure or stop

Fail closed on an undefined or ambiguous state model, disallowed transition, collision, stale source, or failed rewrite; do not substitute this helper for a CAPRMEDIO Atom lifecycle operation.
