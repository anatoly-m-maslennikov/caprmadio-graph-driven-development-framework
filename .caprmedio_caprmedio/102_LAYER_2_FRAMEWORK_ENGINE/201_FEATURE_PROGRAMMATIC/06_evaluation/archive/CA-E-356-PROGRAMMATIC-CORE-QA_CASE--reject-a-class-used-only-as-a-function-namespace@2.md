---
atom_id: CA-E-356
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - function-allocation
  depends_on:
    continuant:
      - programmatic software
version: 2
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-157
  derived_from:
    - CA-A-053
---
# Reject a class used only as a function namespace

## Claim checked

One deterministic responsibility that needs no identity or owned state is
implemented as specifically named functions in a module rather than as a class
used only for grouping.

## Test case

Evaluate one changed class whose methods are all static deterministic
transformations and whose instances own no state, invariant, resource,
lifecycle, or adapter.

## Acceptance criteria

Pass only when the class is rejected and the transformations are allocated to
specifically named functions in one cohesive module.

## Failure disposition

Reject the changed allocation until the namespace-only class is removed.

## Sources

- [CA-M-157 — Allocate deterministic transformations to functions](../05_method/CA-M-157-PROGRAMMATIC-CORE-METHOD--allocate-deterministic-transformations-to-functions.md)
