---
atom_id: CA-E-360
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - one-shot-effect
  depends_on:
    continuant:
      - programmatic software
version: 2
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-160
  derived_from:
    - CA-A-053
---
# Admit a bounded one-shot effect function

## Claim checked

One bounded one-shot effect may be a function when every dependency and
boundary is explicit and no identity or ownership persists across calls.

## Test case

Evaluate one specifically named function that applies one file effect from an
explicit target and dependency and returns a typed outcome without retained
state.

## Acceptance criteria

Pass only when the function's target, dependency, input, outcome, and failure
boundary are explicit and it owns no state, invariant, resource, lifecycle, or
adapter across calls.

## Failure disposition

Reject the function or allocate an object when any persistent ownership is
required.

## Sources

- [CA-M-160 — Separate deterministic transformations from effects and lifecycle](../05_method/CA-M-160-PROGRAMMATIC-CORE-METHOD--separate-deterministic-transformations-from-effects-and-lifecycle.md)
