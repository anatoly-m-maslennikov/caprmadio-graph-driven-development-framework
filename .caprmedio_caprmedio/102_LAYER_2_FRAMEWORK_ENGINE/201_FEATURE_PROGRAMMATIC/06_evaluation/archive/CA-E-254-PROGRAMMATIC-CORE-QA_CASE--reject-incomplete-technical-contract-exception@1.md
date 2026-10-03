---
atom_id: CA-E-254
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - technical-contract-exception
    occurrent:
      - evaluation
version: 1
updated_at: 2026-08-23 17:12:00 +0400
relations:
  evaluation_for:
    - CA-M-110
  derived_from:
    - CA-A-053
---
# Reject incomplete technical-contract exception

## Claim checked

One proposed PROGRAMMATIC dependency or non-Python exception has every record
required by the technical contract before it can be accepted.

## Applicable conditions

Apply when one changed component requires a dependency or non-Python exception
to the default technical boundary.

## Test case

Evaluate one proposed exception whose record omits one required capability,
bounded-carrier, interface, boundary-cost, evidence, or Operator-acceptance
field.

## Acceptance criteria

Pass only when the incomplete exception is rejected without admitting the
affected component.

## Failure disposition

Block the exception and the affected component until one complete bounded
record is available.
