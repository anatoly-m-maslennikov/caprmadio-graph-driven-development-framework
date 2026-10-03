---
atom_id: CA-E-265
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - subprocess-timeout
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
# Surface one subprocess timeout

## Claim checked

One PROGRAMMATIC subprocess boundary observes and returns timeout completion
instead of waiting indefinitely or reporting a successful result.

## Applicable conditions

Apply only when a component invokes a subprocess with a declared timeout.
Components without a subprocess boundary are not applicable.

## Test case

Invoke one declared subprocess that exceeds its declared timeout.

## Acceptance criteria

Pass only when the boundary returns a typed timeout outcome with the declared
input context and no false success.

## Failure disposition

Stop the affected operation and return timeout recovery to its owner.
