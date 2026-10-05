---
atom_id: CA-O-096
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
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
version: 3
updated_at: "2026-10-04 16:53:23 +0000"
relations:
  relates_to:
    - CA-O-024
    - CA-R-1527
    - CA-R-1525
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/IMPLEMENTATION_WORKFLOW/CA-O-096-CORE_META_MODEL-STEP--admit-an-implementation-repair-retry.md
  source_atom_id: CA-O-096
  source_atom_revision: 3
  source_sha256: 0c7bcf5a9385792bd2576bdbc0e7a9d8445854ee29eac6879c70c35114c9e35e
  original_relations_sha256: de2ef28b17f0e68d88249e9195dc3743b7a006804a21d505b52acfb938123324
---
# Summary

Admit an implementation repair retry

## Operation

Implementation Retry Control Step **means** the Workflow node invoking **=1** Action, CA-O-024, **in** Integrated context under CA-R-1527.

- bind inputs from the diagnosed failures from CA-O-095, effective retry sources, retained consumed count, selected P/Plan, current governing permissions, **and** effective confidence threshold.
- use the host's native session/subagent, file, **and** command capabilities; this binding has no MCP prerequisite. missing required context **or** capability returns a blocked invocation, **not** silent execution **in** another context.
- retain exact Action/Step Revisions, source bindings, actual effects, **and** returned results. pass the Action's result **to** the Workflow **without** independently copying its behavior.

map the Action's admitted-retry decision **to** `retry_permitted` **and** **every** exhausted, prohibited, unresolved, **or** approval-blocked decision **to** `retry_blocked`. preserve CA-O-024 accounting **without** another retry counter.

## Details
