---
atom_id: CA-O-098
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Corrective Method Acceptance Step"
  depends_on:
    - "Step"
    - "Action"
    - "Step/Agentic Execution Context"
    - "AI Agent"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Workflow Run"
    - "Step Run"
version: 4
updated_at: "2026-10-04 15:14:54 +0000"
relations:
  relates_to:
    - CA-O-090
    - CA-R-1527
    - CA-R-1525
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/IMPLEMENTATION_WORKFLOW/CA-O-098-CORE_META_MODEL-STEP--verify-and-activate-corrective-method-drafts.md
  source_atom_id: CA-O-098
  source_atom_revision: 4
  source_sha256: 84e6ff7d80bba36a66916c778ba008a93e2ac125059127629a36076860e5ceb0
  original_relations_sha256: 6c05b0491f90ce42dacccbc1fe094328e13701a15a3952f2aa74e7b0c7afb7cd
---
# Summary

Verify and activate corrective Method Drafts

## Operation

Corrective Method Acceptance Step **means** the Workflow node invoking **=1** Action, CA-O-090, **in** Integrated context under CA-R-1527.

- bind inputs from CA-O-101 **in** the separately admitted Method-learning Run: Draft references, retained passing implementation/regression checks, diagnosis **and** actual fix evidence, current baseline **and** Author bindings, selected learning Plan, existing Method authority, **and** current confidence **and** permission gates. this Step is **not** a node of CA-O-016.
- use the host's native session/subagent, file, **and** command capabilities; this binding has no MCP prerequisite. missing required context **or** capability returns a blocked invocation, **not** silent execution **in** another context.
- retain exact Action/Step Revisions, source bindings, actual effects, **and** returned results. pass the Action's result **to** the Workflow **without** independently copying its behavior.

## Details
