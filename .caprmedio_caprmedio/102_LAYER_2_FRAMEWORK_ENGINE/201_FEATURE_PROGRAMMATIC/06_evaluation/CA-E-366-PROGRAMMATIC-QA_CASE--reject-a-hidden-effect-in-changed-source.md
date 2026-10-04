---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "source-effect-boundary"
  depends_on:
    - "programmatic software"
version: 9
updated_at: "2026-10-04 04:23:28 +0400"
relations:
  evaluation_for:
    - CA-M-160
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-366
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
---
# Reject a hidden effect in changed source

## Claim checked

one changed effect function declares its complete effect boundary **or** allocates
persistent ownership **to** an object.

## Test case

evaluate one changed function that reads the process environment implicitly
**before** writing its declared target.

## Acceptance criteria

pass **only** **when** the function is rejected **until** the environment observation is
an explicit input **or** an owned adapter boundary.

## Failure disposition

block the changed unit **until** the hidden observation is removed.

## Sources

- [CA-M-160 — Separate deterministic transformations from effects and lifecycle](../05_method/CA-M-160-PROGRAMMATIC-CORE-METHOD--separate-deterministic-transformations-from-effects-and-lifecycle.md)
