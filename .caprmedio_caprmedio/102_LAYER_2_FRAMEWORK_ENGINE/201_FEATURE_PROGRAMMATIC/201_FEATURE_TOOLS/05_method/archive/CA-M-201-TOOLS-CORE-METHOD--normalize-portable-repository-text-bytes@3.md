---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - artifact-operations
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  method_for:
    - CA-R-1122
  derived_from:
    - CA-A-058
---
# Normalize portable repository text bytes

## Applicable when

Use this Method when governed repository text must have stable bytes across supported operating systems and tools.

## Procedure

1. Read the repository-owned normalization policy and resolve the selected tracked text files without using host defaults as authority.
2. Detect encoding, byte-order marks, line endings, final-newline state, and disallowed control bytes.
3. Produce an exact dry-run of byte changes using the canonical encoding and newline rules.
4. On authorized apply, rewrite only files whose bytes differ and preserve all semantic text.
5. Re-read every changed file and prove that a second normalization pass is byte-idempotent.

## Outcome

Selected repository text has one policy-derived portable byte representation and remains unchanged on repeated normalization.

## Failure or stop

Stop on undecodable input, an unsupported file class, missing policy, or a transformation that would change semantic text.
