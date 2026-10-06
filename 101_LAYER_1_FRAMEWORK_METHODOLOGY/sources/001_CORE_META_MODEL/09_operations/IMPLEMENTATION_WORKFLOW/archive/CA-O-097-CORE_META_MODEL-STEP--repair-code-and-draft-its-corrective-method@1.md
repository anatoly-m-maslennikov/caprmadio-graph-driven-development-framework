---
atom_id: CA-O-097
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
  governs: "Implementation Repair Step"
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
    - CA-O-021
    - CA-R-1527
    - CA-R-1525
---
# Summary

Repair code and draft its corrective Method

## Claim

Implementation Repair Step **means** the Workflow node invoking **=1** Action, CA-O-021, **in** Isolated context under CA-R-1527.

- bind inputs from the same assigned implementation subagent context, diagnosis from CA-O-095, admitted retry from CA-O-096, selected P/Plan **and** owned boundary, current candidate, Method Projection **and** R/E/D, regression commands, **and** retained Method Drafts.
- use the host's native session/subagent, file, **and** command capabilities; this binding has no MCP prerequisite. missing required context **or** capability returns a blocked invocation, **not** silent execution **in** another context.
- retain exact Action/Step Revisions, source bindings, actual effects, **and** returned results. pass the Action's result **to** the Workflow **without** independently copying its behavior.

reuse the assigned subagent for the selected P work across its test, implementation, diagnosis, **and** repair invocations **when** available. replacement requires the complete retained input/evidence handoff **and** fresh admission; do **not** rely on unrecorded conversational memory.
