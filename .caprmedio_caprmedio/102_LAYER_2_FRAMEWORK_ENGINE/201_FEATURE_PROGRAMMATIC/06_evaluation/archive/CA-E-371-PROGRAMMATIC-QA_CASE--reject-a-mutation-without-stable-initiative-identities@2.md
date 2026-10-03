---
atom_id: CA-E-371
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - programmatic-mutation-identity
  depends_on:
    continuant:
      - programmatic software
version: 2
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-191
  derived_from:
    - CA-A-058
---
# Reject a mutation without stable Initiative identities

## Claim checked

One programmatic mutation is blocked before its first effect when its sealed
Initiative or stable action identity is missing or replaced.

## Test case

Submit one mutation whose worker replaces the stable action identity with its
queue-parent identity before applying the effect.

## Acceptance criteria

Pass only when the mutation returns an explicit blocked outcome and applies no
effect.

## Failure disposition

Reject dispatch until the original Initiative and action identities are
restored.

## Sources

- [CA-M-191 — Bind one programmatic mutation to its Initiative](../05_method/CA-M-191-PROGRAMMATIC-METHOD--bind-one-programmatic-mutation-to-its-initiative.md)
