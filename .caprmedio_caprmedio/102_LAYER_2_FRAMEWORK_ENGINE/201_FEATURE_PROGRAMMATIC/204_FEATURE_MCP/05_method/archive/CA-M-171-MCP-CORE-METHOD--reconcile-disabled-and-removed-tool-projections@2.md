---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - framework-engine-mcp
version: 2
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1109
  derived_from:
    - CA-A-057
---
# Reconcile disabled and removed Tool projections

## Applicable when

Apply when the current Tool source set or its enablement decisions change.

## Procedure

1. Resolve the complete current source set before changing the registry.
2. Add newly eligible Tools, exclude explicitly disabled Tools, and remove projections without current sources.
3. Publish only the resulting complete set rather than retaining a separate allowlist.

## Outcome

The registry has no stale, disabled, or independently configured Tool projection.

## Failure or stop

Stop when source discovery is incomplete or any resulting projection cannot be classified.
