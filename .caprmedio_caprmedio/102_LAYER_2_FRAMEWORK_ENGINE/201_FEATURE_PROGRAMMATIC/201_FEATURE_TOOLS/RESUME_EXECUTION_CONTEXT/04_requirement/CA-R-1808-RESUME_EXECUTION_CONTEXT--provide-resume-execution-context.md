---
atom_id: CA-R-1808
content_role: Requirement
current_scope_unit: RESUME_EXECUTION_CONTEXT
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-03 14:55:01 +0000"
subjects:
  governs: "Tool/RESUME_EXECUTION_CONTEXT"
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
  relates_to: [CA-O-116, CA-R-1810]
---
# Summary

Load the remaining execution work

## Scope

the RESUME_EXECUTION_CONTEXT capability for Tool/RESUME_EXECUTION_CONTEXT.

## Claim

the RESUME_EXECUTION_CONTEXT Tool **must** return sufficient saved context to continue unfinished work under the same Run ID without replaying completed effects.

## Details

- implement the methodology Action CA-O-116-PROJECT_CONFIGURATION-ACTION--resume-execution-context.
- accept a supported Run ID; return original request, frozen selection and criteria bindings, pending check or fix work, saved handoffs, current-source observations, and recording blockers.
- preserve the Operator's choice of what **to** execute; discovery, context retrieval, **and** observation provide capabilities.
- bounded **or** unavailable evidence **must** remain explicit **rather than** establish a successful assessment.
