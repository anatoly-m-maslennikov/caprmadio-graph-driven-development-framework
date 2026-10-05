---
atom_id: CA-O-142
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Project Structure Maintenance Authorization Step"
  depends_on: [Step, Action, Workflow, Workflow Run, Step Run, "Step/Agentic Execution Context"]
version: 2
updated_at: "2026-10-04 17:42:12 +0000"
relations:
  relates_to: [CA-O-015, CA-O-013, CA-O-141, CA-R-1509, CA-R-1510, CA-R-1511, CA-R-1527]
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-142-CORE_META_MODEL-STEP--authorize-project-structure-maintenance-change.md
  source_atom_id: CA-O-142
  source_atom_revision: 2
  source_sha256: 8e5623348eda93af6d5ef64a7f240a22cbcc8ed8f84316ad84d83338814661a4
  original_relations_sha256: b122df3c6c2091e1f02901f61b34be954310188dcd65ae3e04256594d6408707
---
# Summary

Authorize project structure maintenance change

## Operation

Project Structure Maintenance Authorization Step **means** the node **in** the owning Workflow CA-O-015 that invokes **=1** existing Action, CA-O-013, with the following bindings.

| Required input or parameter | Bound source |
| --- | --- |
| Assessed proposal and exact effects | CA-O-140's exact proposal together with CA-O-141's returned assessment of that proposal. |
| Current state and applicable authorization/confidence threshold | CA-O-139's retained selected source identities/Revisions and the same Workflow Run's actual Operator authorization and effective Autonomous Confidence Threshold. |

For an invocation whose actual bound Action is Agentic, bind **=1** Integrated **or** Isolated context under CA-R-1527 from the admitted invocation's supplied `agentic_execution_context` runtime parameter **before** dispatch. Missing, ambiguous **or** unsupported values, **or** unavailable required context/capability, block that Agentic invocation; do **not** default **or** silently substitute. A Programmatic invocation does **not** acquire an Agent context. Applicable authority, permissions and remaining retry allowance come from the same Workflow Run; the binding grants no additional authority.

Return the referenced Action's exact result **to** CA-O-015 **without** copying **or** redefining the Action's behavior, changing its outcome, **or** choosing the next Step here. CA-O-015 owns every transition and terminal guard. Retain the exact Action/Step Revisions, input/result source identities, actual effects and resolved context with the Step Run under CA-R-1510/CA-R-1511; a source definition is **not** evidence of an executed Run.

## Details
