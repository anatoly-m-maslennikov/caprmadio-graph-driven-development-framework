---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "executable-unit-size"
  depends_on:
    - "programmatic software"
version: 9
updated_at: "2026-10-04 04:23:28 +0400"
relations:
  evaluation_for:
    - CA-M-162
    - CA-E-539
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-364
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
---
# Reject a medium unit with multiple jobs

## Claim checked

one changed executable unit between 26 **and** 40 logical lines performs **=1** coherent job.

## Test case

evaluate one 30-line changed function whose accurate name **and** branches reveal
two independently reusable responsibilities.

## Acceptance criteria

pass **only** **when** the unit is rejected **until** the two responsibilities are split.

## Failure disposition

block the unit from claiming the 26-to-40-line allowance.

## Sources

- [CA-M-162 — Ratchet hand-authored Python source boundaries](../05_method/CA-M-162-PROGRAMMATIC-CORE-METHOD--ratchet-hand-authored-python-source-boundaries.md)
