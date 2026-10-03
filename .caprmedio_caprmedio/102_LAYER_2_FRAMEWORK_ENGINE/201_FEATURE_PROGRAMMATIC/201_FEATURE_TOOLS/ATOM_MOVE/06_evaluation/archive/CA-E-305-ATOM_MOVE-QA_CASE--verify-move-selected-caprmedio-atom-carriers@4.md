---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - artifact-operations
    occurrent:
      - evaluation
version: 4
updated_at: 2026-09-02 01:10:00 +0400
relations:
  evaluation_for:
    - CA-M-187
---
# Verify move selected caprmedio atom carriers

## Claim checked

CA-M-187 relocates the complete sealed Atom target set while preserving every carrier byte, filename, and stable Atom ID.

## Applicable when

Apply to any realization of CA-M-187 before it can move individual Atom carriers or recursive subtrees.

## Test case

Use one fixture with one explicitly selected Atom and a two-level subtree containing three Atom carriers and one non-Atom file. Record a shape-preserving subtree dry-run and an explicitly flattened subtree dry-run; introduce a destination collision into the shape-preserving map and attempt delegated apply, then remove the collision and apply the unchanged exact and shape-preserving requests through sealed Initiative envelopes.

## Acceptance criteria

The collision attempt moves nothing; the valid applies move the explicitly selected Atom and all three subtree Atoms to their mapped destinations, preserve the default subtree shape, leave the non-Atom untouched, remove all selected sources, and preserve every selected carrier's filename, stable ID, and digest. The explicit-flatten dry-run exposes a flat map and makes no mutation.

## Failure disposition

Reject the realization and preserve source and destination maps, flattening map, authority result, collision evidence, before-and-after digests, and any incomplete move state.
