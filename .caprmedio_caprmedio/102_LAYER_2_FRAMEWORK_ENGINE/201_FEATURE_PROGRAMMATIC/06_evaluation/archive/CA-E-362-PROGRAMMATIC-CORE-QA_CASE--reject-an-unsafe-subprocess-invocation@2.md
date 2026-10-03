---
atom_id: CA-E-362
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - subprocess-invocation
  depends_on:
    continuant:
      - programmatic software
version: 2
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-161
  derived_from:
    - CA-A-053
---
# Reject an unsafe subprocess invocation

## Claim checked

One PROGRAMMATIC subprocess uses an argument array, explicit timeout, checked
exit status, controlled environment input, and shell execution disabled.

## Test case

Evaluate one invocation expressed as a shell command string with shell
execution enabled.

## Acceptance criteria

Pass only when the invocation is rejected before process creation and reports
the unsafe argument and shell boundary.

## Failure disposition

Reject the subprocess path until it uses the complete bounded invocation
contract.

## Sources

- [CA-M-161 — Bound file and subprocess effects](../05_method/CA-M-161-PROGRAMMATIC-CORE-METHOD--bound-file-and-subprocess-effects.md)
