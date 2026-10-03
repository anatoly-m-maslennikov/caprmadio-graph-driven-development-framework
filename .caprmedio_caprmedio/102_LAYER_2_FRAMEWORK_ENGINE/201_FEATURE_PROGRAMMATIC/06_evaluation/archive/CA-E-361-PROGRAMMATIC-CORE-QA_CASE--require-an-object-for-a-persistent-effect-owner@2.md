---
atom_id: CA-E-361
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - persistent-effect-owner
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
# Require an object for a persistent effect owner

## Claim checked

One effect that owns identity, state, an invariant, a resource, a lifecycle, or
a replaceable adapter across calls is applied through a specifically named
object method.

## Test case

Evaluate one standalone function that acquires a resource and retains its
lifecycle state for a later call.

## Acceptance criteria

Pass only when the function is rejected and the persistent responsibility is
allocated to one object with explicit acquisition, use, and release boundaries.

## Failure disposition

Reject the effect boundary until its persistent owner is explicit.

## Sources

- [CA-M-160 — Separate deterministic transformations from effects and lifecycle](../05_method/CA-M-160-PROGRAMMATIC-CORE-METHOD--separate-deterministic-transformations-from-effects-and-lifecycle.md)
