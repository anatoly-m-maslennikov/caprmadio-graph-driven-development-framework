---
atom_id: CA-O-095
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Implementation Failure Diagnosis Step"
  depends_on:
    - "Step"
    - "Action"
    - "Step/Agentic Execution Context"
    - "AI Agent"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Workflow Run"
    - "Step Run"
version: 3
updated_at: "2026-10-04 16:53:23 +0000"
relations:
  relates_to:
    - CA-O-089
    - CA-R-1527
    - CA-R-1525
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/IMPLEMENTATION_WORKFLOW/CA-O-095-CORE_META_MODEL-STEP--diagnose-failures-in-the-assigned-subagent.md
  source_atom_id: CA-O-095
  source_atom_revision: 3
  source_sha256: 49d06e90f7939527a66d51ffe06084f157bdab9de138255d4dea7edc114d3fa8
  original_relations_sha256: f44c9db520af7268fea8076f22c861ee76b9cf12ee645e58fa3317547c9eaf52
---
# Summary

Diagnose failures in the assigned subagent

## Operation

Implementation Failure Diagnosis Step **means** the Workflow node invoking **=1** Action, CA-O-089, **in** Isolated context under CA-R-1527.

- bind inputs from the same assigned implementation subagent context, selected P/Plan, current candidate **and** phase, failure evidence from CA-O-094, test definitions, current Method Projection **and** R/E/D, **and** applicable confidence **and** permission gates.
- use the host's native session/subagent, file, **and** command capabilities; this binding has no MCP prerequisite. missing required context **or** capability returns a blocked invocation, **not** silent execution **in** another context.
- retain exact Action/Step Revisions, source bindings, actual effects, **and** returned results. pass the Action's result **to** the Workflow **without** independently copying its behavior.

reuse the assigned subagent for the selected P work across its test, implementation, diagnosis, **and** repair invocations **when** available. replacement requires the complete retained input/evidence handoff **and** fresh admission; do **not** rely on unrecorded conversational memory.

## Details
