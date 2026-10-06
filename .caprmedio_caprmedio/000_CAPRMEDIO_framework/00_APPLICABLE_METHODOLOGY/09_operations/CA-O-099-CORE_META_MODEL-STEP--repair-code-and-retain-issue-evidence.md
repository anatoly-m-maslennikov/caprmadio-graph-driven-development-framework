---
atom_id: CA-O-099
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
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
version: 2
updated_at: "2026-10-04 16:53:23 +0000"
relations:
  relates_to:
    - CA-O-021
    - CA-R-1527
    - CA-R-1525
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/IMPLEMENTATION_WORKFLOW/CA-O-099-CORE_META_MODEL-STEP--repair-code-and-retain-issue-evidence.md
  source_atom_id: CA-O-099
  source_atom_revision: 2
  source_sha256: cb41a0ac54a473f106cfd02efcdfc6b75f5d592eecdc7f5c3c3906aceb925617
  original_relations_sha256: 1ea5c7fc0c690b75607075f32f2d9552decfced01b385e0f28a6205f30651f72
---
# Summary

Repair code and retain issue evidence

## Operation

Implementation Repair Step **means** the Workflow node invoking **=1** Action, CA-O-021, **in** Isolated context under CA-R-1527.

- bind inputs from the same assigned implementation subagent context, diagnosis from CA-O-095, admitted retry from CA-O-096, selected P/Plan **and** owned boundary, current candidate, Method Projection **and** R/E/D, regression commands, **and** retained issue **and** regression evidence.
- use the host's native session/subagent, file, **and** command capabilities; this binding has no MCP prerequisite. missing required context **or** capability returns a blocked invocation, **not** silent execution **in** another context.
- retain exact Action/Step Revisions, source bindings, actual effects, **and** returned results. pass the Action's result **to** the Workflow **without** independently copying its behavior.

reuse the assigned subagent for the selected P work across its test, implementation, diagnosis, **and** repair invocations **when** available. replacement requires the complete retained input/evidence handoff **and** fresh admission; do **not** rely on unrecorded conversational memory.

## Details
