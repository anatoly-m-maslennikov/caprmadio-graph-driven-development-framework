---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "deterministic-transformation"
  depends_on:
    - "programmatic software"
version: 10
updated_at: "2026-10-04 04:23:28 +0400"
relations:
  evaluation_for:
    - CA-M-157
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-256
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
---
# Verify deterministic transformation from declared inputs

## Claim checked

one declared deterministic PROGRAMMATIC transformation produces its result **and**
failure values from explicit declared inputs **without** an implicit host
observation **or** external effect.

## Applicable conditions

apply **when** a component parses, classifies, validates, plans, projects,
formats, **or** **otherwise** transforms explicit input into a result.

## Test case

evaluate one transformation twice with the same declared input while varying
an **otherwise** irrelevant host observation.

## Acceptance criteria

pass **only** **when** both results **and** failure values are equivalent **and** the
transformation reports no filesystem, process, clock, environment, network,
persistence, **or** logging-export effect.

## Failure disposition

stop treating the unit as deterministic **and** assign its missing observation **or**
effect boundary **to** the appropriate owner.

## Sources

- [CA-M-157 — Allocate deterministic transformations to functions](../05_method/CA-M-157-PROGRAMMATIC-CORE-METHOD--allocate-deterministic-transformations-to-functions.md)
