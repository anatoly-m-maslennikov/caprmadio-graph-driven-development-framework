---
atom_id: CA-E-264
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - subprocess-effect
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
# Surface one nonzero subprocess result

## Claim checked

One PROGRAMMATIC subprocess boundary observes and returns a non-zero exit
status with the context required for diagnosis or recovery.

## Applicable conditions

Apply only when a component invokes a subprocess. Components without a
subprocess boundary are not applicable.

## Test case

Invoke one declared subprocess that returns a non-zero exit status.

## Acceptance criteria

Pass only when the boundary reports the explicit status and declared input
context without treating the invocation as successful.

## Failure disposition

Stop the affected operation and return the failure to its caller or recovery
owner.
