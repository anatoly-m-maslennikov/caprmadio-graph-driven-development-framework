---
atom_id: CA-O-091
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
  governs: "Implementation Preparation Step"
  depends_on:
    - "Step"
    - "Action"
    - "Step/Agentic Execution Context"
    - "AI Agent"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Workflow Run"
    - "Step Run"
version: 2
updated_at: "2026-09-24 18:16:00 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to:
    - CA-O-017
    - CA-R-1527
    - CA-R-1525
---
# Summary

Prepare delegated implementation work

## Claim

Implementation Preparation Step **means** the Workflow node invoking **=1** Action, CA-O-017, **in** Integrated context under CA-R-1527.

- bind inputs from the Workflow inputs, bounded request **and** current P/Plan **when** supplied, admitted authority sources **and** declared input universe, any supplied compiled Method file, selected R/D implementation targets, separate Evaluation authority, permissions, selected mode, complete runtime inputs, retained work/evidence, assigned subagent references, remaining retry state, **and** latest returned results.
- use the host's native session/subagent, file, **and** command capabilities; this binding has no MCP prerequisite. missing required context **or** capability returns a blocked invocation, **not** silent execution **in** another context.
- retain exact Action/Step Revisions, source bindings, actual effects, **and** returned results. pass the Action's result **to** the Workflow **without** independently copying its behavior.
