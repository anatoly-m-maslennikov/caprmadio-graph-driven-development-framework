---
atom_id: CA-O-151
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: "Source Reconciliation Publication Step"
  depends_on:
    - "Step"
    - "Action"
    - "Source Reconciliation"
    - "Step/Agentic Execution Context"
    - "Workflow Run"
    - "Step Run"
version: 1
updated_at: "2026-10-04 17:42:12 +0000"
relations:
  relates_to:
    - CA-O-010
    - CA-O-009
    - CA-R-1509
    - CA-R-1511
    - CA-R-1527
global_tier: 11
---
# Summary

Publish the reconciled source projection

## Operation

Source Reconciliation Publication Step **means** the node **in** Workflow `CA-O-010` invoking **`=1`** Action, `CA-O-009`.

- bind the final assessed frontier, valid decisions, **and** selected Projection Delivery authority from CA-O-147's current assessment result, applicable retained CA-O-149 decisions, **and** admitted Workflow Run Delivery inputs. retain the exact proposal, decision **and** source-frontier bindings supplied for this invocation, **when** applicable, rather than independently selecting **or** inferring them.
- for an Agentic invocation, use Integrated context under `CA-R-1527-CORE_META_MODEL-GENERAL-REQUIREMENT--define-agentic-step-execution-context`; this does **not** grant additional authority. a Programmatic invocation does **not** acquire an Agent context. missing required context **or** capability returns a blocked invocation rather than silent substitution.
- retain exact Action/Step Revisions, input/source bindings, actual effects **and** returned results for the Step Run. pass the Action's unchanged result **and** payload **to** the Workflow **without** copying **or** redefining its behavior.
- remain within the Workflow's applicable approval, currentness, confidence, accepted revisit/recovery allowance **and** escalation guards. this Step does **not** authorize an extra retry, correction, publication, **or** decision.

## Details
