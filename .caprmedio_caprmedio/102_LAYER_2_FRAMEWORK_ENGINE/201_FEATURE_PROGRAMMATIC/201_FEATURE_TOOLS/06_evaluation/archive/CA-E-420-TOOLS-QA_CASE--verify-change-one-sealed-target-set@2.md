---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - feature-boundary
    occurrent:
      - evaluation
version: 2
updated_at: 2026-09-02 00:40:00 +0400
relations:
  evaluation_for:
    - CA-M-254
---
# Verify change one sealed target set

## Claim checked

CA-M-254 applies only an explicitly approved unchanged complete `BULK_CHANGE` plan as one validated rollbackable transaction.

## Applicable when

Apply whenever registered bulk operations, plan sealing, approval gating, transaction validation, or rollback handling changes.

## Test case

Inspect the registered `BULK_CHANGE` unit, then use one sealed target set and registered structured-patch and rename effects to derive a complete plan. Change one target after plan approval, then restore it and apply the unchanged approved plan.

## Acceptance criteria

`BULK_CHANGE` has prefix `BULK_CHANGE`, immediate `TOOLS` owner, `unordered_unit` kind, Structural level `4`, address `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/BULK_CHANGE`, and realization path `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/BULK_CHANGE/`. The stale plan changes nothing. The unchanged plan applies every declared effect exactly once, exposes one transaction identity and final target frontier, and leaves no unplanned mutation.

## Failure disposition

Reject the realization and preserve target set, approved plan, precondition comparison, declared effects, final frontier, transaction identity, and rollback evidence.
