---
atom_id: CA-R-1806
content_role: Requirement
current_scope_unit: GET_EXECUTION_CONTEXT
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-03 14:55:01 +0000"
subjects:
  governs: "Tool/GET_EXECUTION_CONTEXT"
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
  relates_to: [CA-O-114, CA-R-1810]
---
# Summary

Load the selected execution context

## Scope

the GET_EXECUTION_CONTEXT capability for Tool/GET_EXECUTION_CONTEXT.

## Claim

the GET_EXECUTION_CONTEXT Tool **must** return the selected capability's exact current definition, implementation binding, input schema when supported, and relevant authority and operational context.

## Details

- implement the methodology Action CA-O-114-PROJECT_CONFIGURATION-ACTION--get-execution-context.
- accept a Tool name or Operations Atom ID and a context budget; return source-bound content, related Workflow Steps and Actions, applicable RMED, implementation and prompt references, and explicit context gaps.
- preserve the Operator's choice of what **to** execute; discovery, context retrieval, **and** observation provide capabilities.
- bounded **or** unavailable evidence **must** remain explicit **rather than** establish a successful assessment.
