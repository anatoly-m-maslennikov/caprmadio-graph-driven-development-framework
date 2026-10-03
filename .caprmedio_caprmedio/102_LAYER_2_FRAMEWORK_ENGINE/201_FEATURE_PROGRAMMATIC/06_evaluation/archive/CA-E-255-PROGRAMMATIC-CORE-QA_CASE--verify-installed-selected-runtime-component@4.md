---
atom_id: CA-E-255
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - installed-runtime
  depends_on:
    continuant:
      - programmatic software
version: 4
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-110
  derived_from:
    - CA-A-053
---
# Verify installed selected-runtime component

## Claim checked

One delivered installable PROGRAMMATIC component runs under the runtime and
dependency selections owned by accepted Methods from the carrier placed and
encoded by its Delivery.

## Applicable conditions

Apply only when a lower-Scope Delivery declares the component installable.
This case does not establish a platform-support claim.

## Test case

Install one delivered component from its Delivery-owned carrier, invoke its
declared entry boundary, and compare the observed runtime and dependencies with
their Method-owned selections and materializations.

## Acceptance criteria

Pass only when the installed carrier reaches its declared entry boundary
without requiring an undeclared runtime or dependency and without the carrier
claiming selection authority.

## Failure disposition

Reject the installation claim and return the component to its Delivery owner.

## Sources

- [CA-M-110 — Implement PROGRAMMATIC components in Python](../05_method/CA-M-110-PROGRAMMATIC-CORE-IMPL_METHOD--implement-programmatic-components-in-python.md)
