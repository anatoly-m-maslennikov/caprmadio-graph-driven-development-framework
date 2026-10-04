---
atom_id: CA-O-093
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Requirement Implementation Step"
  depends_on:
    - "Step"
    - "Action"
    - "Step/Agentic Execution Context"
    - "AI Agent"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Workflow Run"
    - "Step Run"
version: 3
updated_at: "2026-09-24 01:39:33 +0000"
relations:
  relates_to:
    - CA-O-019
    - CA-R-1527
    - CA-R-1525
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/IMPLEMENTATION_WORKFLOW/CA-O-093-CORE_META_MODEL-STEP--implement-requirements-in-the-assigned-subagent.md
---
# Summary

Implement requirements in the assigned subagent

## Claim

Requirement Implementation Step **means** the Workflow node invoking **=1** Action, CA-O-019, **in** Isolated context under CA-R-1527.

- bind inputs from the selected P/Plan item **and** admitted work from CA-O-091, the same assigned subagent context, governing Method Projection **and** R/E/D, prepared tests from CA-O-092, baseline evidence from CA-O-094 **and** CA-O-095 **when** available, **and** the current owned work boundary.
- use the host's native session/subagent, file, **and** command capabilities; this binding has no MCP prerequisite. missing required context **or** capability returns a blocked invocation, **not** silent execution **in** another context.
- retain exact Action/Step Revisions, source bindings, actual effects, **and** returned results. pass the Action's result **to** the Workflow **without** independently copying its behavior.

reuse the assigned subagent for the selected P work across its test, implementation, diagnosis, **and** repair invocations **when** available. replacement requires the complete retained input/evidence handoff **and** fresh admission; do **not** rely on unrecorded conversational memory.
