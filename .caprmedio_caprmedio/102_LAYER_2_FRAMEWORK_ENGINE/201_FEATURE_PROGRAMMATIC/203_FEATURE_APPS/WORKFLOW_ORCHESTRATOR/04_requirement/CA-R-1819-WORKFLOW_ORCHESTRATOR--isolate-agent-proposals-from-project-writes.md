---
atom_id: CA-R-1819
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 04:10:07 +0400"
subjects:
  governs: "Action/execution/isolation"
  depends_on: [AI Agent, Atom, Operator, Implementation, Workflow Run, Tool, Carrier]
relations:
  relates_to: [CA-R-1814, CA-R-846]
---
# Summary

isolate Agent proposals from Project writes

## Scope

Agentic Action execution **in** the Docker runtime.

## Claim

an AI Agent **must** receive **only** its supplied execution context **and** required authentication, **without** access **to** writable Project Carriers, the host home directory **or** the Docker daemon.

## Details

- the AI Agent returns a structured proposal; the trusted worker alone admits **and** applies authorized changes.
- the execution context carries the selected Atom, checking rules, Action prompt **and** relevant saved phase report.
- container isolation replaces the inner CLI sandbox **only** **in** the dedicated Agent service, which has no Project mounts.
- credentials remain runtime data, excluded from the image, source control, public status **and** reports.
