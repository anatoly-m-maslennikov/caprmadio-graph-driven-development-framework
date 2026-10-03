---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "tool-effect-result"
  depends_on:
    - "TOOLS"
version: 7
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-M-223
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Bind one Tool effect result to its operation

## Claim checked

one admitted Tool effect **and** its receipt remain bound **to** the canonical
operation through failure **and** retry.

## Test case

apply one admitted file effect, force a partial failure, retry it with the same
operation identity, **and** attempt **to** attach the receipt **to** another operation.

## Acceptance criteria

pass **only** **when** the original identity remains on **every** request, failure, retry,
**and** receipt, **and** the mismatched attachment is rejected.

## Failure disposition

stop the effect path **until** operation identity, sealed target, arguments, **and**
receipt agree.

## Sources

- [CA-M-223 — Bind Tool effect results to the canonical operation](../05_method/CA-M-223-TOOLS-CORE-METHOD--bind-tool-effect-results-to-the-canonical-operation.md)
- [Python documentation: `tempfile`](https://docs.python.org/3.14/library/tempfile.html)
