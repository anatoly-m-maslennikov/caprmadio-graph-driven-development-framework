---
atom_id: CA-C-489
content_role: Concern
type: Problem
current_scope_unit: PROMPTS
local_tier: Standard
global_tier: 11
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 03:53:17 +0000"
subjects:
  governs: "Repair review prompt authority drift"
  depends_on: [Tool, Implementation, Evaluation, Workflow Run, Journal]
relations:
  concern_about: [CA-P-1762]
---
# Summary

Repair review prompt authority drift

## Concern

Base Revise prompt tests use stale source pins, root resolution and word-budget/layout assumptions; the current compact prompt contract is not fully validated.

## Evidences

`102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/RMED_ATOM_REVIEW/tests/test_prompt_specification.py`, `tests/test_contracts.py` and `source_bindings.json` establish the stale root/pin/budget cases; the active CA-D-446 is version 7 rather than the previous manifest's version 6.

Source/mock results do not establish actual release completion.

## Blast radius

The affected selected Workflow, full release gate and CA-P-1655 final acceptance.

## Disposition

Refresh exact live pins and compact prompts without weakening accepted checks or raising the budget; fix confirmed stale fixtures and retain real defects.

CA-P-1762 owns the bounded repair. Keep this Problem active until its regression and independent acceptance establish the repair.
