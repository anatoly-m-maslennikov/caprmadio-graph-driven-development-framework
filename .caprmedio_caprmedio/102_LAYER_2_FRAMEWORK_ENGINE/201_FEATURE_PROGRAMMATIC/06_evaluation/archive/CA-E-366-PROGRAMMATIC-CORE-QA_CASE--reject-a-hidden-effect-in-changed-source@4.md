---
atom_id: CA-E-366
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "source-effect-boundary"
  depends_on:
    - "programmatic software"
version: 4
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-M-160
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject a hidden effect in changed source

## Claim checked

One changed effect function declares its complete effect boundary or allocates
persistent ownership to an object.

## Test case

Evaluate one changed function that reads the process environment implicitly
before writing its declared target.

## Acceptance criteria

Pass only when the function is rejected until the environment observation is
an explicit input or an owned adapter boundary.

## Failure disposition

Block the changed unit until the hidden observation is removed.

## Sources

- [CA-M-160 — Separate deterministic transformations from effects and lifecycle](../05_method/CA-M-160-PROGRAMMATIC-CORE-METHOD--separate-deterministic-transformations-from-effects-and-lifecycle.md)
