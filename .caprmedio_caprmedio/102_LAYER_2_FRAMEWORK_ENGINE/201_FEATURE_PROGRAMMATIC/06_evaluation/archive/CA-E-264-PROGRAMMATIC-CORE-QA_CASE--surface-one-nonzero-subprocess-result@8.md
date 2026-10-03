---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "subprocess-effect"
  depends_on:
    - "programmatic software"
version: 8
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-161
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Surface one nonzero subprocess result

## Claim checked

One PROGRAMMATIC subprocess boundary observes **and** returns a non-zero exit
status with the context required for diagnosis **or** recovery.

## Applicable conditions

Apply **only** **when** a component invokes a subprocess. Components **without** a
subprocess boundary are **not** applicable.

## Test case

Invoke one declared subprocess that returns a non-zero exit status.

## Acceptance criteria

pass **only** **when** the boundary reports the explicit status **and** declared input
context **without** treating the invocation as successful.

## Failure disposition

Stop the affected operation **and** return the failure **to** its caller **or** recovery
owner.

## Sources

- [CA-M-161 — Bound file and subprocess effects](../05_method/CA-M-161-PROGRAMMATIC-CORE-METHOD--bound-file-and-subprocess-effects.md)
