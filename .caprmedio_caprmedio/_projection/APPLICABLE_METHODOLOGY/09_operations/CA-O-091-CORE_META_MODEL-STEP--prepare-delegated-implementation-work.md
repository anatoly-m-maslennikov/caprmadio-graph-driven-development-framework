---
atom_id: CA-O-091
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
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
version: 4
updated_at: "2026-10-04 16:53:23 +0000"
relations:
  relates_to:
    - CA-O-017
    - CA-R-1527
    - CA-R-1525
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/IMPLEMENTATION_WORKFLOW/CA-O-091-CORE_META_MODEL-STEP--prepare-delegated-implementation-work.md
  source_atom_id: CA-O-091
  source_atom_revision: 4
  source_sha256: 8581f4a6fa4c805eaa08b845b46bd4ceda4880f611c8cc6538d0c382e3999b8b
  original_relations_sha256: 8cbf084aa689e9d8440dbe92835bfd968046bbcaca8ef0b90054af291cae77df
---
# Summary

Prepare delegated implementation work

## Operation

Implementation Preparation Step **means** the Workflow node invoking **=1** Action, CA-O-017, **in** Integrated context under CA-R-1527.

- bind inputs from the Workflow inputs, bounded request **and** current P/Plan **when** supplied, admitted authority sources **and** declared input universe, any supplied compiled Method file, selected R/D implementation targets, separate Evaluation authority, permissions, selected mode, complete runtime inputs, retained work/evidence, assigned subagent references, remaining retry state, **and** latest returned results.
- use the host's native session/subagent, file, **and** command capabilities; this binding has no MCP prerequisite. missing required context **or** capability returns a blocked invocation, **not** silent execution **in** another context.
- retain exact Action/Step Revisions, source bindings, actual effects, **and** returned results. pass the Action's result **to** the Workflow **without** independently copying its behavior.

## Details
