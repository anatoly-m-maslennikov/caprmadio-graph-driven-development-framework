---
content_role: Requirement
type: Requirement
current_scope_unit: APPS
claim_target_scope_unit: APPS
local_tier: Standard
author: Anatoly Maslennikov
status: Draft
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "App/service lifecycle"
  depends_on:
    - "Action"
    - "App"
    - "Operator"
    - "Project"
    - "Workflow Run"
version: 1
updated_at: "2026-09-23 19:20:45 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-E-352", "CA-M-222", "CA-R-1100", "CA-R-1523", "CA-R-1524"]}
---
# Summary

Keep local application lifecycle bounded and observable

## Claim

an admitted local App service **must** expose supervised, bounded, **and** observable startup, shutdown, restart, cancellation, timeout, **and** recovery outcomes for its owned background work.

- the Operator **or** admitted client can distinguish starting, running, stopping, completed, failed, **and** unresolved recovery outcomes **without** inferring success from a disconnected session **or** stopped process.
- interrupted work remains subject **to** that application's declared recovery boundary; restarting the service **must not** silently lose work, duplicate effects, **or** promote transient state **to** Project authority.
- unsupported lifecycle capabilities remain explicit rather than being reported as performed. WORKFLOW_ORCHESTRATOR retains its narrower accepted-work **and** handoff rules under CA-R-1523 **and** CA-R-1524.

this Requirement selects no supervisor implementation, uniform retry policy, permanent server, **or** Workflow for building the application.
