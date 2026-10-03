---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "programmatic-mutation-identity"
  depends_on:
    - "programmatic software"
version: 6
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-191
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject a mutation without stable Initiative identities

## Claim checked

One programmatic mutation is blocked **before** its first effect **when** its sealed
Initiative **or** stable action identity is missing **or** replaced.

## Test case

Submit one mutation whose worker replaces the stable action identity with its
queue-parent identity **before** applying the effect.

## Acceptance criteria

pass **only** **when** the mutation returns an explicit blocked outcome **and** applies no
effect.

## Failure disposition

Reject dispatch **until** the original Initiative **and** action identities are
restored.

## Sources

- [CA-M-191 — Bind one programmatic mutation to its Initiative](../05_method/CA-M-191-PROGRAMMATIC-METHOD--bind-one-programmatic-mutation-to-its-initiative.md)
