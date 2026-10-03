---
atom_id: CA-E-401
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - tool-effect-result
    occurrent:
      - evaluation
  depends_on:
    continuant:
      - TOOLS
version: 1
updated_at: 2026-09-01 02:25:00 +0400
relations:
  evaluation_for:
    - CA-M-223
  derived_from:
    - CA-A-057
---
# Bind one Tool effect result to its operation

## Claim checked

One admitted Tool effect and its receipt remain bound to the canonical
operation through failure and retry.

## Test case

Apply one admitted file effect, force a partial failure, retry it with the same
operation identity, and attempt to attach the receipt to another operation.

## Acceptance criteria

Pass only when the original identity remains on every request, failure, retry,
and receipt, and the mismatched attachment is rejected.

## Failure disposition

Stop the effect path until operation identity, sealed target, arguments, and
receipt agree.

## Sources

- [CA-M-223 — Bind Tool effect results to the canonical operation](../05_method/CA-M-223-TOOLS-CORE-METHOD--bind-tool-effect-results-to-the-canonical-operation.md)
- [Python documentation: `tempfile`](https://docs.python.org/3.14/library/tempfile.html)
