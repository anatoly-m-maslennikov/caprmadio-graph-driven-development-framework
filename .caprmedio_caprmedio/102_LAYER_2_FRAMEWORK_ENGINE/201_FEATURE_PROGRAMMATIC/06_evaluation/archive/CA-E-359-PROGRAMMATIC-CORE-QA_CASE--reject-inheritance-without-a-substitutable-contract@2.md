---
atom_id: CA-E-359
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - subtype-contract
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
# Reject inheritance without a substitutable contract

## Claim checked

One PROGRAMMATIC inheritance relationship exists only for a stable
substitutable subtype contract.

## Test case

Evaluate one changed subclass that inherits behavior for code reuse but cannot
replace its base under the base contract.

## Acceptance criteria

Pass only when the inheritance is rejected and the behavior is expressed by a
function, module, or composed collaborator.

## Failure disposition

Reject the subtype boundary until substitutability is demonstrated or
inheritance is removed.

## Sources

- [CA-M-158 — Allocate owned state and lifecycle to objects](../05_method/CA-M-158-PROGRAMMATIC-CORE-METHOD--allocate-owned-state-and-lifecycle-to-objects.md)
