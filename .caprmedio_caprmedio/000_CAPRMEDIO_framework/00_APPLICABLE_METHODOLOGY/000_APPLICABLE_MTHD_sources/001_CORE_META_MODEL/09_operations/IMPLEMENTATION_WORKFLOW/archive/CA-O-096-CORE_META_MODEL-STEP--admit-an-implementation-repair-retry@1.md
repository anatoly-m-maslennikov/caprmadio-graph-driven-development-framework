---
atom_id: CA-O-096
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Implementation Retry Control Step"
  depends_on:
    - "Step"
    - "Action"
    - "Step/Agentic Execution Context"
    - "AI Agent"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Workflow Run"
    - "Step Run"
version: 1
updated_at: "2026-09-24 01:39:33 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to:
    - CA-O-024
    - CA-R-1527
    - CA-R-1525
---
# Summary

Admit an implementation repair retry

## Claim

Implementation Retry Control Step **means** the Workflow node invoking **=1** Action, CA-O-024, **in** Integrated context under CA-R-1527.

- bind inputs from the diagnosed failures from CA-O-095, effective retry sources, retained consumed count, selected P/Plan, current governing permissions, **and** effective confidence threshold.
- use the host's native session/subagent, file, **and** command capabilities; this binding has no MCP prerequisite. missing required context **or** capability returns a blocked invocation, **not** silent execution **in** another context.
- retain exact Action/Step Revisions, source bindings, actual effects, **and** returned results. pass the Action's result **to** the Workflow **without** independently copying its behavior.

map the Action's admitted-retry decision **to** `retry_permitted` **and** **every** exhausted, prohibited, unresolved, **or** approval-blocked decision **to** `retry_blocked`. preserve CA-O-024 accounting **without** another retry counter.
