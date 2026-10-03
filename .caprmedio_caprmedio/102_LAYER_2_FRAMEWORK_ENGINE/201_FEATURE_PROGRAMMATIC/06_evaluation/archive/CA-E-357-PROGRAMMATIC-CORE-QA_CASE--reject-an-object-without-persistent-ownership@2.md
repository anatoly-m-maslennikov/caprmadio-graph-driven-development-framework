---
atom_id: CA-E-357
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - object-ownership
  depends_on:
    continuant:
      - programmatic software
version: 2
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-158
  derived_from:
    - CA-A-053
---
# Reject an object without persistent ownership

## Claim checked

One PROGRAMMATIC object is admitted only when it requires identity across calls
and owns state, an invariant, a resource, a lifecycle, or a replaceable
adapter.

## Test case

Evaluate one changed object that only wraps a bounded one-shot effect and owns
no responsibility across calls.

## Acceptance criteria

Pass only when the object is rejected and the effect is allocated to a
specifically named bounded function.

## Failure disposition

Reject the object until persistent ownership is demonstrated or the wrapper is
replaced by a function.

## Sources

- [CA-M-158 — Allocate owned state and lifecycle to objects](../05_method/CA-M-158-PROGRAMMATIC-CORE-METHOD--allocate-owned-state-and-lifecycle-to-objects.md)
