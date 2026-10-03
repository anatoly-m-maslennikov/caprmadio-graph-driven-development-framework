---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - runtime
    occurrent:
      - evaluation
version: 3
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-M-142
  derived_from:
    - CA-A-057
---
# Keep one Tool runtime state outside installation

## Claim checked

One Tool's mutable runtime state is isolated from its selected installed executable release.

## Test case

Run one Tool that records mutable execution state, then inspect its installation and runtime roots.

## Acceptance criteria

Mutable state exists only beneath `.caprmedio_runtime`; the installation contains no mutable execution state and deleting runtime does not delete governed authority.

## Failure disposition

Reject the release or runtime layout until the boundary is restored.
