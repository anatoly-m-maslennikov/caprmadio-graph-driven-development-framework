---
atom_id: CA-O-094
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Implementation Evaluation Step"
  depends_on:
    - "Step"
    - "Action"
    - "Step/Agentic Execution Context"
    - "AI Agent"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Workflow Run"
    - "Step Run"
version: 4
updated_at: "2026-09-24 17:18:07 +0000"
relations:
  relates_to:
    - CA-O-020
    - CA-R-1527
    - CA-R-1525
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/IMPLEMENTATION_WORKFLOW/CA-O-094-CORE_META_MODEL-STEP--run-the-selected-implementation-checks.md
---
# Summary

Run the selected implementation checks

## Claim

Implementation Evaluation Step **means** the Workflow node invoking **=1** Action, CA-O-020, **in** Integrated context under CA-R-1527.

- bind inputs from the selected P/Plan, exact current candidate **and** phase, prepared tests **and** commands, governing Method Projection **and** R/E/D, relevant complete test inputs, **and** retained issue **and** regression evidence from prior Step results.
- use the host's native session/subagent, file, **and** command capabilities; this binding has no MCP prerequisite. missing required context **or** capability returns a blocked invocation, **not** silent execution **in** another context.
- retain exact Action/Step Revisions, source bindings, actual effects, **and** returned results. pass the Action's result **to** the Workflow **without** independently copying its behavior.
