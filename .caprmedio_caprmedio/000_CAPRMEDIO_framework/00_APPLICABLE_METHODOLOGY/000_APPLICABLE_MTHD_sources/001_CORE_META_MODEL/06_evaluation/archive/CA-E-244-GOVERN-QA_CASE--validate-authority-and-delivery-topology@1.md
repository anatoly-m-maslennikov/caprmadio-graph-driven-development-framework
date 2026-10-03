---
atom_id: CA-E-244
cce_version: cce_1
cce_form: evaluation
version: 1
updated_at: 2026-08-22 08:09:26
relations:
  evaluation_for:
    - CA-R-770
    - CA-R-774
    - CA-R-776
    - CA-R-952
    - CA-R-953
---
# Validate authority and Delivery topology

## Claim checked

The Project topology uses the registered authority directories, root Delivery directories, and BSEED Delivery exception.

## Test case

Resolve every registered directory pair. Verify that the three BSEED units deliver inside FRAMEWORK_METHODOLOGY authority and that the six Project Layers plus FIELD deliver at the repository root. Then swap, omit, duplicate, or rename each path separately.

## Acceptance criteria

Only the exact registered topology passes, and every authority-to-Delivery pair denotes one Scope Unit.

## Failure disposition

Record a Concern naming the mismatched Scope Unit and path.
