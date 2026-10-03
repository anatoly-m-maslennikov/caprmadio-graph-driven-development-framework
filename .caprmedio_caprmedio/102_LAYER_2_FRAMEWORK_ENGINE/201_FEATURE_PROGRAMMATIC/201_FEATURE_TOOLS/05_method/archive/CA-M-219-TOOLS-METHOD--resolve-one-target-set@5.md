---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - feature-boundary
version: 5
updated_at: 2026-09-02 00:40:00 +0400
relations:
  method_for:
    - CA-R-1153
  derived_from:
    - CA-A-058
---
# Resolve one target set

## Applicable when

Use this Method when `TARGET_SET` must resolve identities or governed selectors before another Tool checks or changes the targets.

## Procedure

1. Confirm that `TARGET_SET` is registered as one `unordered_unit` Finder owned immediately by `TOOLS` at Structural level `4`, with prefix `TARGET_SET`, address `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/TARGET_SET`, and realization path `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/TARGET_SET/`.
2. Resolve the supplied explicit identities and composable governed selectors against the current project frontier.
3. Deduplicate the resolved members and order them by the registered stable ordering rule.
4. Seal membership, source frontier, and content digest together as one target-set identity.
5. Return the sealed set read-only to a named downstream Tool without evaluating or changing any target; reject an invalid unit boundary, unresolved selector, ambiguous identity, missing member, or changed frontier.

## Outcome

One `TARGET_SET` result contains exactly its stable ordered membership, source frontier, and content digest for downstream checking or change.

## Failure or stop

Do not mutate targets, execute Evaluations, create change plans, or rebuild Projections; return an explicit unresolved or stale result instead.
