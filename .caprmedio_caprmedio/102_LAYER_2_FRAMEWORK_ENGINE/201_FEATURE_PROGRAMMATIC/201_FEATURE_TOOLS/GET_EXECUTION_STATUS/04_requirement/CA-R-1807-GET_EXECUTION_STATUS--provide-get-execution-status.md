---
atom_id: CA-R-1807
content_role: Requirement
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
  relates_to: [CA-O-115, CA-R-1810]
---
# Summary

Read execution status and saved results

## Scope

the GET_EXECUTION_STATUS capability for Tool/GET_EXECUTION_STATUS.

## Claim

the GET_EXECUTION_STATUS Tool **must** return the saved Workflow Run status and requested Action results with evidence references, distinguishing work outcomes from evidence-recording failures.

## Details

- implement the methodology Action CA-O-115-PROJECT_CONFIGURATION-ACTION--get-execution-status.
- accept a supported Run ID, optional Action ID and selection ordinal, and whether full saved results are requested; return status, output, results, progress, recording blockers, and report references.
- preserve the Operator's choice of what **to** execute; discovery, context retrieval, **and** observation provide capabilities.
- bounded **or** unavailable evidence **must** remain explicit **rather than** establish a successful assessment.
