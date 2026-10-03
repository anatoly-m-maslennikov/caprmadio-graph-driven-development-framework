---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "WORKFLOW_ORCHESTRATOR/Goal"
  depends_on:
    - "APPS"
    - "Workflow Run"
version: 1
updated_at: "2026-09-23 04:20:00 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Coordinate Workflow Runs

WORKFLOW_ORCHESTRATOR **must** own synchronous **and** asynchronous Workflow Run coordination, including interactive Step suspension, result submission, continuation, recovery, **and** next-Step selection from applicable methodology.
