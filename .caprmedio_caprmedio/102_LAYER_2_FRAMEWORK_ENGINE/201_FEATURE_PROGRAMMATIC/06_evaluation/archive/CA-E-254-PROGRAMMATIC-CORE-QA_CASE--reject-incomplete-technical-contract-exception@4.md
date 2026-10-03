---
atom_id: CA-E-254
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - technical-contract-exception
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
# Reject incomplete technical-contract exception

## Claim checked

One proposed PROGRAMMATIC dependency or non-Python exception has an accepted
Method that selects it and complete configuration, Implementation, Delivery,
and evidence materializations before the affected component can be admitted.

## Applicable conditions

Apply when one changed component requires a dependency or non-Python exception
to the default technical boundary.

## Test case

Evaluate one proposed exception that omits either its accepted selecting
Method or one required capability, bounded-carrier, interface, boundary-cost,
evidence, or Operator-acceptance field.

## Acceptance criteria

Pass only when the incomplete exception is rejected without treating a
configuration, Implementation, or Delivery carrier as selection authority and
without admitting the affected component.

## Failure disposition

Block admission of the affected component until the exception has an accepted
Method and one complete bounded materialization record.

## Sources

- [CA-M-110 — Implement PROGRAMMATIC components in Python](../05_method/CA-M-110-PROGRAMMATIC-CORE-IMPL_METHOD--implement-programmatic-components-in-python.md)
