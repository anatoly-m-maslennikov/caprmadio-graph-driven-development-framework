---
atom_id: CA-E-255
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - installed-runtime
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
# Verify installed selected-runtime component

## Claim checked

One delivered installable PROGRAMMATIC component realizes under the selected
technical runtime boundary from its installed carrier.

## Applicable conditions

Apply only when a lower-Scope Delivery declares the component installable.
This case does not establish a platform-support claim.

## Test case

Install one delivered component into the selected runtime boundary and invoke
its declared entry boundary from the installed carrier.

## Acceptance criteria

Pass only when the installed carrier reaches its declared entry boundary
without requiring an undeclared runtime or dependency.

## Failure disposition

Reject the installation claim and return the component to its Delivery owner.
