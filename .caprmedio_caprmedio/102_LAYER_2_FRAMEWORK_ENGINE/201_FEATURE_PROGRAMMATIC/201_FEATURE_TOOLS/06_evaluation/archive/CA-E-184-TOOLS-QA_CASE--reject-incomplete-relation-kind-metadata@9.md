---
subjects:
  governs: "Relation Kind/Registry Entry"
  depends_on: []
version: 9
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-R-806

llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject incomplete relation-kind metadata

## Claim checked

Deterministic Tools cannot use a relation kind whose canonical registry entry is incomplete.

## Test case

Compile a fixture registry containing one **otherwise** valid direct relation whose derived inverse name, declaration carrier, **or** upstream endpoint is absent, **then** gather commit context for a file using that relation.

## Acceptance criteria

Registry compilation fails with the exact missing field, context gathering returns no sealed envelope, **and** no governed **or** Git state changes.

## Failure disposition

Reject the registry compiler **and** Finder **if** either infers the missing field **or** continues with a partial relation entry.
