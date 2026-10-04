---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "python-workflow-exception"
  depends_on:
    - "programmatic software"
version: 8
updated_at: "2026-10-04 04:23:28 +0400"
relations:
  evaluation_for:
    - CA-M-221
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-377
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
---
# Reject an unaccepted overlapping Python workflow manager

## Claim checked

one Python workflow does **not** mix uv with another overlapping environment **or**
dependency manager **unless** an accepted Method owns a bounded exception.

## Test case

evaluate one governed path that runs both uv **and** Poetry **without** an accepted
exception.

## Acceptance criteria

pass **only** **when** the path is rejected **before** environment mutation.

## Failure disposition

block the alternative manager **until** a required capability, bounded carriers,
commands, cost, recovery procedure, **and** Operator acceptance are governed.

## Sources

- [CA-M-221 — Use uv as the default Python workflow frontend](../05_method/CA-M-221-PROGRAMMATIC-CORE-METHOD--use-uv-as-the-default-python-workflow-frontend.md)
