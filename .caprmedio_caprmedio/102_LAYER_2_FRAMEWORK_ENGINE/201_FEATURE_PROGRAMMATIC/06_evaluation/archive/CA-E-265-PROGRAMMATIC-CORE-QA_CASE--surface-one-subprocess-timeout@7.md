---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "subprocess-timeout"
  depends_on:
    - "programmatic software"
version: 7
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-161
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Surface one subprocess timeout

## Claim checked

One PROGRAMMATIC subprocess boundary observes and returns timeout completion
instead of waiting indefinitely or reporting a successful result.

## Applicable conditions

Apply only when a component invokes a subprocess with a declared timeout.
Components without a subprocess boundary are not applicable.

## Test case

Invoke one declared subprocess that exceeds its declared timeout.

## Acceptance criteria

Pass only when the boundary returns a typed timeout outcome with the declared
input context and no false success.

## Failure disposition

Stop the affected operation and return timeout recovery to its owner.

## Sources

- [CA-M-161 — Bound file and subprocess effects](../05_method/CA-M-161-PROGRAMMATIC-CORE-METHOD--bound-file-and-subprocess-effects.md)
