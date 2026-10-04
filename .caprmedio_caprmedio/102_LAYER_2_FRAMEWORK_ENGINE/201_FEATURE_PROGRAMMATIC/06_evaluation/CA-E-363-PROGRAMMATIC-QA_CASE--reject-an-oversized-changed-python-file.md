---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "source-file-size"
  depends_on:
    - "programmatic software"
version: 8
updated_at: "2026-10-04 04:23:28 +0400"
relations:
  evaluation_for:
    - CA-M-162
    - CA-E-539
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-363
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
---
# Reject an oversized changed Python file

## Claim checked

one new **or** materially changed hand-authored PROGRAMMATIC Python file remains at
**or** below 200 physical lines **or** has a specific bounded exception.

## Test case

evaluate one changed 201-line hand-authored Python file with no file-size
exception.

## Acceptance criteria

pass **only** **when** conformance is rejected **until** the file is reduced, split by
responsibility, **or** supplied with one accepted bounded exception.

## Failure disposition

block the changed file from claiming source-boundary conformance.

## Sources

- [CA-M-162 — Ratchet hand-authored Python source boundaries](../05_method/CA-M-162-PROGRAMMATIC-CORE-METHOD--ratchet-hand-authored-python-source-boundaries.md)
