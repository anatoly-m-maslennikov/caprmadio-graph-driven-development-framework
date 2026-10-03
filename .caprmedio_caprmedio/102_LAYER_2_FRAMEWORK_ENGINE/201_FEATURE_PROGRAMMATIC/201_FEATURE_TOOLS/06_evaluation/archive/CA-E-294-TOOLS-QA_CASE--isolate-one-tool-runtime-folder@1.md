---
atom_id: CA-E-294
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - runtime
    occurrent:
      - evaluation
version: 1
updated_at: 2026-08-23 17:40:00 +0400
relations:
  evaluation_for:
    - CA-M-143
  derived_from:
    - CA-A-057
---
# Isolate one Tool runtime folder

## Claim checked

Each Tool that persists runtime files uses its dedicated owned runtime directory.

## Test case

Run two Tools that persist runtime files concurrently.

## Acceptance criteria

Each Tool writes only below its own runtime directory or declared run-specific descendant, and neither relies on the other's files.

## Failure disposition

Stop the affected Tool execution and report the unowned shared-state boundary.
