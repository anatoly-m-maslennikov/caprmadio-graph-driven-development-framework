---
atom_id: CA-O-143
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: "Project Structure Maintenance Application Step"
  depends_on: [Step, Action, Workflow, Workflow Run, Step Run, "Step/Agentic Execution Context"]
version: 1
updated_at: "2026-10-04 17:42:12 +0000"
relations:
  relates_to: [CA-O-015, CA-O-014, CA-O-142, CA-R-1509, CA-R-1510, CA-R-1511, CA-R-1527]
---
# Summary

Apply project structure maintenance change

## Operation

Project Structure Maintenance Application Step **means** the node **in** the owning Workflow CA-O-015 that invokes **=1** existing Action, CA-O-014, with the following bindings.

| Required input or parameter | Bound source |
| --- | --- |
| Exact authorized proposal | CA-O-140's proposal as bound by CA-O-142's returned authorization for its exact effects. |
| Unchanged selected source state | CA-O-139's selected source identities/Revisions retained by that authorization; CA-O-014 owns the currentness recheck. |
| Explicit Carrier changes, recoverable cutover and authorized recovery boundary | The same exact proposal/authorization from CA-O-140 and CA-O-142, not an inferred broader mutation or recovery permission. |

An Agentic invocation uses Integrated context under CA-R-1527; a Programmatic invocation does **not** acquire an Agent context. Applicable authority, permissions and remaining retry allowance come from the same Workflow Run; the binding grants no additional authority.

Return the referenced Action's exact result **to** CA-O-015 **without** copying **or** redefining the Action's behavior, changing its outcome, **or** choosing the next Step here. CA-O-015 owns every transition and terminal guard. Retain the exact Action/Step Revisions, input/result source identities, actual effects and resolved context with the Step Run under CA-R-1510/CA-R-1511; a source definition is **not** evidence of an executed Run.

## Details
