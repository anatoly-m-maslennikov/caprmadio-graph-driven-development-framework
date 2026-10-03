---
content_role: Delivery
type: Delivery
current_scope_unit: WORKFLOW_ORCHESTRATOR
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
author: Anatoly Maslennikov
status: Draft
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "WORKFLOW_ORCHESTRATOR/state Carriers"
  depends_on:
    - "Action"
    - "Carrier"
    - "Event"
    - "Journal"
    - "Project Temporary State"
    - "Workflow"
    - "Workflow Run"
version: 1
updated_at: "2026-09-23 19:20:45 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"delivery_for": ["CA-R-1524"], "relates_to": ["CA-D-437", "CA-D-490", "CA-M-302", "CA-R-1100", "CA-R-1522", "CA-R-1523", "CAPRMEDIO-META-REQU-158"]}
---
# Summary

Place Workflow coordination and recovery state

## Claim

WORKFLOW_ORCHESTRATOR **must** place retained coordination **and** recovery-state Carriers **in** its declared project-local runtime location, separate from disposable worker state.

- retain the request, Run, dispatch, definition, **and** recovery bindings required by CA-R-1524; canonical execution facts remain **in** the Project Journal under CAPRMEDIO-META-REQU-158.
- runtime queues, scheduling indexes, **and** displayed state carry references **to** their canonical events rather than independently authored historical copies.
- disposable worker scratch, caches, **and** staging use Project Temporary State under CA-D-437; resumable state **must not** depend **only** on those disposable Carriers.

the application Implementation retains its Delivery binding under CA-D-490. this placement specification does **not** select a database, transport, server library, retry policy, **or** Workflow definition.
