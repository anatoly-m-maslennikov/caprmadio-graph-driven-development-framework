---
atom_id: CA-E-395
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - generated-boundary-evaluation
  depends_on:
    continuant:
      - programmatic software
version: 1
updated_at: 2026-09-01 02:10:00 +0400
relations:
  evaluation_for:
    - CA-M-233
  derived_from:
    - CA-A-053
---
# Fuzz parsers and stateful boundaries

## Claim checked

Broad input or transition spaces preserve accepted invariants under generated
valid, invalid, and ordered cases.

## Test case

Run a bounded property or state-machine campaign against one parser or
lifecycle and inject an invariant-breaking generated sequence.

## Acceptance criteria

Pass only when the minimal failing input or sequence and seed are preserved,
the defect is accepted or rejected explicitly, and an accepted defect gains a
deterministic regression case.

## Failure disposition

Reject unreplayable generated evidence and keep expensive campaigns outside
synchronous Hooks.

## Sources

- [Hypothesis stateful testing](https://hypothesis.readthedocs.io/en/latest/stateful.html)
- [CA-M-233 — Select software Evaluation techniques by failure mode](../05_method/CA-M-233-PROGRAMMATIC-CORE-METHOD--select-software-evaluation-techniques-by-failure-mode.md)
