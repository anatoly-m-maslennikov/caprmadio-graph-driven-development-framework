---
atom_id: CA-E-270
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - engineering-ratchet
    occurrent:
      - evaluation
version: 1
updated_at: 2026-08-23 17:12:00 +0400
relations:
  evaluation_for:
    - CA-M-164
  derived_from:
    - CA-A-053
---
# Verify changed-code adoption ratchet

## Claim checked

One changed or new PROGRAMMATIC target within an admitted automation or typing
capability does not regress below its current passing boundary.

## Applicable conditions

Apply when a component changes source within an admitted typing, formatting,
linting, or behavioral-check capability. Unadmitted capability selection is
not applicable.

## Test case

Evaluate one changed target against its current admitted passing boundary.

## Acceptance criteria

Pass only when the target meets the current boundary or has one bounded
exception owned by the canonical configuration, Delivery, or Implementation
carrier.

## Failure disposition

Reject the ratchet claim and return the target to its change owner.
