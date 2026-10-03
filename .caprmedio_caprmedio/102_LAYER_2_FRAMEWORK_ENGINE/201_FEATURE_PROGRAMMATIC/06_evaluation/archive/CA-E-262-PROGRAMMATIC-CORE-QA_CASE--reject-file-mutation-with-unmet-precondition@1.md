---
atom_id: CA-E-262
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - file-mutation
    occurrent:
      - evaluation
version: 1
updated_at: 2026-08-23 17:12:00 +0400
relations:
  evaluation_for:
    - CA-M-161
  derived_from:
    - CA-A-053
---
# Reject file mutation with unmet precondition

## Claim checked

One PROGRAMMATIC file mutation stops before writing, replacing, or removing a
file when its declared target or precondition is invalid.

## Applicable conditions

Apply when a component writes, replaces, or removes a file.

## Test case

Request one file mutation with a declared precondition that does not hold.

## Acceptance criteria

Pass only when the operation returns the precondition failure and leaves the
target bytes unchanged.

## Failure disposition

Reject the mutation and preserve the existing target for diagnosis.
