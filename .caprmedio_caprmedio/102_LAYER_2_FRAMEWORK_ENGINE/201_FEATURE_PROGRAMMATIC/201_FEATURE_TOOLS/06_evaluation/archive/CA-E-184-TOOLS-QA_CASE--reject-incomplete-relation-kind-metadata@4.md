---
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 4
updated_at: 2026-08-23 18:08:00 +0400
relations:
  evaluation_for:
    - CA-R-806

---
# Reject incomplete relation-kind metadata

## Claim checked

Deterministic Tools cannot use a relation kind whose canonical registry entry is incomplete.

## Test case

Compile a fixture registry containing one otherwise valid direct relation whose derived inverse name, declaration carrier, or upstream endpoint is absent, then gather commit context for a file using that relation.

## Acceptance criteria

Registry compilation fails with the exact missing field, context gathering returns no sealed envelope, and no governed or Git state changes.

## Failure disposition

Reject the registry compiler and Finder if either infers the missing field or continues with a partial relation entry.
