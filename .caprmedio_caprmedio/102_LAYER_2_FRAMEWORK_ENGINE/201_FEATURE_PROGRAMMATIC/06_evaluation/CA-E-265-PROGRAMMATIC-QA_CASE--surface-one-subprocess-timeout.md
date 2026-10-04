---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "subprocess-timeout"
  depends_on:
    - "programmatic software"
version: 10
updated_at: "2026-10-04 04:23:28 +0400"
relations:
  evaluation_for:
    - CA-M-161
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-265
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
---
# Surface one subprocess timeout

## Claim checked

one PROGRAMMATIC subprocess boundary observes **and** returns timeout completion
instead of waiting indefinitely **or** reporting a successful result.

## Applicable conditions

apply **only** **when** a component invokes a subprocess with a declared timeout.
components **without** a subprocess boundary are **not** applicable.

## Test case

invoke one declared subprocess that exceeds its declared timeout.

## Acceptance criteria

pass **only** **when** the boundary returns a typed timeout outcome with the declared
input context **and** no false success.

## Failure disposition

stop the affected operation **and** return timeout recovery **to** its owner.

## Sources

- [CA-M-161 — Bound file and subprocess effects](../05_method/CA-M-161-PROGRAMMATIC-CORE-METHOD--bound-file-and-subprocess-effects.md)
