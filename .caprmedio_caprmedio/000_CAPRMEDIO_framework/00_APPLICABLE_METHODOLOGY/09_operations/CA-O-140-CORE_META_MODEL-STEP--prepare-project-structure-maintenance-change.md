---
atom_id: CA-O-140
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Project Structure Maintenance Preparation Step"
  depends_on: [Step, Action, Workflow, Workflow Run, Step Run, "Step/Agentic Execution Context"]
version: 2
updated_at: "2026-10-04 17:42:12 +0000"
relations:
  relates_to: [CA-O-015, CA-O-012, CA-O-139, CA-R-1509, CA-R-1510, CA-R-1511, CA-R-1527]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-140-CORE_META_MODEL-STEP--prepare-project-structure-maintenance-change.md
  source_atom_id: CA-O-140
  source_atom_revision: 2
  source_sha256: 8b24f3f42ed2d5b7a1fb048d78327ca62fb9c9e51c56692e1babbb525e0ed69c
  original_relations_sha256: f814cbea998ed9ed755793a97dd77377d892bc42a447d4ef31cdf1510f4cbb35
---
# Summary

Prepare project structure maintenance change

## Operation

Project Structure Maintenance Preparation Step **means** the node **in** the owning Workflow CA-O-015 that invokes **=1** existing Action, CA-O-012, with the following bindings.

| Required input or parameter | Bound source |
| --- | --- |
| Selected current state | CA-O-139's returned exact source identities and Revisions. |
| Requested structural change | The same CA-O-015 Workflow Run's admitted request, including the requested creation, rename, reparenting, reorder, path rebinding, removal, or reconciliation. |

For an invocation whose actual bound Action is Agentic, bind **=1** Integrated **or** Isolated context under CA-R-1527 from the admitted invocation's supplied `agentic_execution_context` runtime parameter **before** dispatch. Missing, ambiguous **or** unsupported values, **or** unavailable required context/capability, block that Agentic invocation; do **not** default **or** silently substitute. A Programmatic invocation does **not** acquire an Agent context. Applicable authority, permissions and remaining retry allowance come from the same Workflow Run; the binding grants no additional authority.

Return the referenced Action's exact result **to** CA-O-015 **without** copying **or** redefining the Action's behavior, changing its outcome, **or** choosing the next Step here. CA-O-015 owns every transition and terminal guard. Retain the exact Action/Step Revisions, input/result source identities, actual effects and resolved context with the Step Run under CA-R-1510/CA-R-1511; a source definition is **not** evidence of an executed Run.

## Details
