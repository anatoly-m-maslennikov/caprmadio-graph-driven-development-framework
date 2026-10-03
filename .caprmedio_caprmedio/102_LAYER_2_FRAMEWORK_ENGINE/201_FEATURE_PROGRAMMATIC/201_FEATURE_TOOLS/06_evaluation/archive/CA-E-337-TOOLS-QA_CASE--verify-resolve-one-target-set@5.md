---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - feature-boundary
    occurrent:
      - evaluation
version: 5
updated_at: 2026-09-02 00:40:00 +0400
relations:
  evaluation_for:
    - CA-M-219
---
# Verify resolve one target set

## Claim checked

CA-M-219 resolves one stable sealed target set from explicit identities and governed selectors without performing a check or mutation.

## Applicable when

Apply whenever `TARGET_SET` identity resolution, ordering, sealing, or source-frontier handling changes.

## Test case

Inspect the registered `TARGET_SET` unit and supply duplicate explicit identities and one governed selector that resolve to a known member set. Resolve and seal it, then change one source before a second sealing attempt.

## Acceptance criteria

`TARGET_SET` has prefix `TARGET_SET`, immediate `TOOLS` owner, `unordered_unit` kind, Structural level `4`, address `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/TARGET_SET`, and realization path `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/TARGET_SET/`. The valid set contains each matching member once in stable order with its recorded source frontier and content digest; no target changes. The changed-frontier attempt returns no sealed accepted set.

## Failure disposition

Reject the realization and preserve identities, selector, expected membership and order, sealed frontier and digest, stale-frontier result, and no-mutation evidence.
