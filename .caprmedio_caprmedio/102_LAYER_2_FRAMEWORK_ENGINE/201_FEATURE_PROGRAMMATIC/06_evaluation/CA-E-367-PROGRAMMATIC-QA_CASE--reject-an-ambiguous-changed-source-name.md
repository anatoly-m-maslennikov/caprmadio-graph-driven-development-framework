---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "source-name"
  depends_on:
    - "programmatic software"
version: 9
updated_at: "2026-10-04 04:23:28 +0400"
relations:
  evaluation_for:
    - CA-M-158
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-367
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
---
# Reject an ambiguous changed source name

## Claim checked

one new **or** materially changed source unit has a specific,
intention-revealing name that states one responsibility.

## Test case

evaluate one changed class named `Manager` **without** a qualifying project term **or**
owned responsibility.

## Acceptance criteria

pass **only** **when** the class is rejected **until** its name identifies the exact
responsibility it owns.

## Failure disposition

block the changed unit from claiming naming conformance.

## Sources

- [CA-M-158 — Allocate owned state and lifecycle to objects](../05_method/CA-M-158-PROGRAMMATIC-CORE-METHOD--allocate-owned-state-and-lifecycle-to-objects.md)
