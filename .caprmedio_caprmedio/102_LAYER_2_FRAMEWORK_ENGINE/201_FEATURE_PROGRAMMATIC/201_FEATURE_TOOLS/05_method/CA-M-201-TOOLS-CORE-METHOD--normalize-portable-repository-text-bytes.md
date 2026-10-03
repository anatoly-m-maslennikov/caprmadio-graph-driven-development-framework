---
cce_version: cce_1
cce_form: method
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 7
updated_at: 2026-09-01 23:47:24 +0400
relations:
  method_for:
    - CA-R-1122
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Normalize portable repository text bytes

## Applicable when

use this Method **when** governed repository text **must** have stable bytes across supported operating systems **and** tools.

## Procedure

1. read the repository-owned normalization policy **and** resolve the selected tracked text files **without** using host defaults as authority.
2. detect encoding, byte-order marks, line endings, final-newline state, **and** disallowed control bytes.
3. produce an exact dry-run of byte changes using the canonical encoding **and** newline rules.
4. on authorized apply, rewrite **only** files whose bytes differ **and** preserve **all** semantic text.
5. re-read **every** changed file **and** prove that a second normalization pass is byte-idempotent.

## Outcome

selected repository text has one policy-derived portable byte representation **and** remains unchanged on repeated normalization.

## Failure or stop

stop on undecodable input, an unsupported file class, missing policy, **or** a transformation that would change semantic text.
