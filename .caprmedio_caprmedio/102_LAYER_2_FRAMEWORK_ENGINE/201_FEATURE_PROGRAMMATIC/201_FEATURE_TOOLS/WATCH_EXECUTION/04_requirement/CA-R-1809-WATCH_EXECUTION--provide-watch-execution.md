---
atom_id: CA-R-1809
content_role: Requirement
current_scope_unit: WATCH_EXECUTION
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-03 14:55:01 +0000"
subjects:
  governs: "Tool/WATCH_EXECUTION"
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
  relates_to: [CA-O-117, CA-R-1810]
---
# Summary

Wait for execution updates

## Scope

the WATCH_EXECUTION capability for Tool/WATCH_EXECUTION.

## Claim

the WATCH_EXECUTION Tool **must** return correlated execution updates after a caller's cursor, including completion, failure, interruption, handoff, progress, and evidence-recording changes.

## Details

- implement the methodology Action CA-O-117-PROJECT_CONFIGURATION-ACTION--watch-execution.
- accept a supported Run ID, opaque cursor and bounded wait timeout; return a new cursor, updates, current status, timeout state, and full report reference.
- preserve the Operator's choice of what **to** execute; discovery, context retrieval, **and** observation provide capabilities.
- bounded **or** unavailable evidence **must** remain explicit **rather than** establish a successful assessment.
