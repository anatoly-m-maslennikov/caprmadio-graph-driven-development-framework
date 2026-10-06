---
atom_id: CA-O-150
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Source Reconciliation Correction Step"
  depends_on:
    - "Step"
    - "Action"
    - "Source Reconciliation"
    - "Step/Agentic Execution Context"
    - "Workflow Run"
    - "Step Run"
version: 2
updated_at: "2026-10-04 17:42:12 +0000"
relations:
  relates_to:
    - CA-O-010
    - CA-O-008
    - CA-R-1509
    - CA-R-1511
    - CA-R-1527
global_tier: 11
---
# Summary

Apply the reconciliation source corrections

## Operation

Source Reconciliation Correction Step **means** the node **in** Workflow `CA-O-010` invoking **`=1`** Action, `CA-O-008`.

- bind the exact approved correction **and** its current source frontier from CA-O-149's recorded decision **and** the exact proposal/current selected frontier. retain the exact proposal, decision **and** source-frontier bindings supplied for this invocation, **when** applicable, rather than independently selecting **or** inferring them.
- for an invocation whose actual bound Action is Agentic, bind **`=1`** Integrated **or** Isolated context under `CA-R-1527-CORE_META_MODEL-GENERAL-REQUIREMENT--define-agentic-step-execution-context` from the admitted invocation's supplied `agentic_execution_context` runtime parameter **before** dispatch. missing, ambiguous **or** unsupported values, **or** unavailable required context/capability, return a blocked Agentic invocation; do **not** default **or** silently substitute. retain the selected context with the Step Run. this does **not** grant additional authority. a Programmatic invocation does **not** acquire an Agent context.
- retain exact Action/Step Revisions, input/source bindings, actual effects **and** returned results for the Step Run. pass the Action's unchanged result **and** payload **to** the Workflow **without** copying **or** redefining its behavior.
- remain within the Workflow's applicable approval, currentness, confidence, accepted revisit/recovery allowance **and** escalation guards. this Step does **not** authorize an extra retry, correction, publication, **or** decision.

## Details
