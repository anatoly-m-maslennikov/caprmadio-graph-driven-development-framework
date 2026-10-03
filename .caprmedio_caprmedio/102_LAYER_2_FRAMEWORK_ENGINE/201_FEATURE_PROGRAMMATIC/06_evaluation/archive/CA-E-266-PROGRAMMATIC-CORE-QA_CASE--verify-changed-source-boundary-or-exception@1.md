---
atom_id: CA-E-266
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - source-boundary
    occurrent:
      - evaluation
version: 1
updated_at: 2026-08-23 17:12:00 +0400
relations:
  evaluation_for:
    - CA-M-162
  derived_from:
    - CA-A-053
---
# Verify changed source boundary or exception

## Claim checked

One changed hand-authored PROGRAMMATIC Python source carrier satisfies the
source-size ratchet or records its required bounded exception.

## Applicable conditions

Apply to a new or materially changed hand-authored Python file. Generated
Runtime and Delivery outputs are not applicable.

## Test case

Evaluate one changed executable unit exceeding 40 logical lines without a
documented exception.

## Acceptance criteria

Pass only when the carrier is rejected until it is split, reduced, or supplied
with one specific documented exception that retains its single responsibility.

## Failure disposition

Block the changed source from claiming source-boundary conformance.
