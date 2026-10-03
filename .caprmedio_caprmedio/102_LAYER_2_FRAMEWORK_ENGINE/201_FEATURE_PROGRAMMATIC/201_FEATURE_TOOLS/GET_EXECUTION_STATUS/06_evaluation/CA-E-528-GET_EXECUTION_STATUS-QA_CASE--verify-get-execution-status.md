---
atom_id: CA-E-528
content_role: Evaluation
type: QA Case
current_scope_unit: GET_EXECUTION_STATUS
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-03 14:55:01 +0000"
subjects:
  governs: "Tool/GET_EXECUTION_STATUS"
  depends_on:
    - "Tool"
    - "Action"
    - "Workflow"
    - "Atom"
    - "Scope Unit"
    - "Implementation"
    - "Workflow Run"
    - "Journal"
relations:
  relates_to: [CA-R-1807, CA-D-515]
---
# Summary

Verify GET_EXECUTION_STATUS

## Scope

the GET_EXECUTION_STATUS capability for Tool/GET_EXECUTION_STATUS.

## Claim

the Evaluation **must** check the GET_EXECUTION_STATUS Tool against its declared result **and** Carrier contract using an end-to-end mock Project.

## Details

- exercise running, completed, failed, interrupted, pending Actions, initial check results preserved through fixing, missing Runs, unsupported Action IDs, and recording failure.
- compare complete expected results with actual results; successful counts alone do **not** establish correctness.
- invoke the real MCP transport for the exposed schema **and** result boundary.
- retain existing RMED Atoms Base Revise behavior, including its initial evidence **and** absence of a saved-output recheck.
