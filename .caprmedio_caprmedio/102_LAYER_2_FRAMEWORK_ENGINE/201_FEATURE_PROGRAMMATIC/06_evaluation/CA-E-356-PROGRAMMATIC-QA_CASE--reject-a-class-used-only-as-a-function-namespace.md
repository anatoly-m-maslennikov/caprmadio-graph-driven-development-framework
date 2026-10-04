---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "function-allocation"
  depends_on:
    - "programmatic software"
version: 8
updated_at: "2026-10-04 04:23:28 +0400"
relations:
  evaluation_for:
    - CA-M-157
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-356
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
---
# Reject a class used only as a function namespace

## Claim checked

one deterministic responsibility that needs no identity **or** owned state is
implemented as specifically named functions **in** a module rather than as a class
used **only** for grouping.

## Test case

evaluate one changed class whose methods are **all** static deterministic
transformations **and** whose instances own no state, invariant, resource,
lifecycle, **or** adapter.

## Acceptance criteria

pass **only** **when** the class is rejected **and** the transformations are allocated **to**
specifically named functions **in** one cohesive module.

## Failure disposition

reject the changed allocation **until** the namespace-only class is removed.

## Sources

- [CA-M-157 — Allocate deterministic transformations to functions](../05_method/CA-M-157-PROGRAMMATIC-CORE-METHOD--allocate-deterministic-transformations-to-functions.md)
