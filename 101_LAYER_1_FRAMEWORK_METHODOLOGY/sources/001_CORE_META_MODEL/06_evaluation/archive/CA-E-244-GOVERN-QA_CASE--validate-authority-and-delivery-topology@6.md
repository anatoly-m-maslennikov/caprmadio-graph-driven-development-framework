---
subjects:
  declared:
    continuant:
      - layout
      - authority
    occurrent:
      - evaluation
atom_id: CA-E-244
cce_version: cce_1
cce_form: evaluation
version: 6
updated_at: 2026-08-23 15:00:38
relations:
  evaluation_for:
    - CA-R-770
    - CA-R-952
    - CA-R-973
    - CA-R-974
    - CA-R-985
    - CA-R-986
    - CA-R-987
---
# Validate authority and Delivery topology

## Claim checked

Authority directories encode Structural Level, effective Navigational Order Number, effective Unit Type Name, applicable Local Order, and Unit Name, while root Delivery directories omit Unit Type Name and Local Order.

## Test case

Resolve one Feature with default navigation labels and one Layer with Operator overrides. Then introduce Structural Level `10`, rerender every Structural Level segment to two digits, and alter one effective label or Local Order independently.

## Acceptance criteria

Only directories with the current project-wide Structural Level width and the correct effective per-unit labels pass.

## Failure disposition

Record a Concern naming the mismatched Scope Unit and path.
