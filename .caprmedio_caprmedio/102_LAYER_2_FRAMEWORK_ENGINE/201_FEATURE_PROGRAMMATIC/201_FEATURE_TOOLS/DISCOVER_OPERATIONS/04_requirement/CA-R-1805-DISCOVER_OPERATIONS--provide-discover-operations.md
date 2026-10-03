---
atom_id: CA-R-1805
content_role: Requirement
current_scope_unit: DISCOVER_OPERATIONS
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-03 14:55:01 +0000"
subjects:
  governs: "Tool/DISCOVER_OPERATIONS"
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
  relates_to: [CA-O-113, CA-R-1810]
---
# Summary

Find Workflows and Actions by outcome

## Scope

the DISCOVER_OPERATIONS capability for Tool/DISCOVER_OPERATIONS.

## Claim

the DISCOVER_OPERATIONS Tool **must** return a ranked, bounded selection of active Workflow and Action definitions matching the requested outcome and filters.

## Details

- implement the methodology Action CA-O-113-PROJECT_CONFIGURATION-ACTION--discover-operations.
- accept a query, Workflow or Action kind, Scope Unit and execution-kind filters, offset, and result limit; return summaries, definition bindings, and implementation availability.
- preserve the Operator's choice of what **to** execute; discovery, context retrieval, **and** observation provide capabilities.
- bounded **or** unavailable evidence **must** remain explicit **rather than** establish a successful assessment.
