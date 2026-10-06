---
atom_id: CA-E-513
content_role: Evaluation
type: QA Case
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Atom Carrier Validation"
  depends_on:
    - "Workflow"
    - "Step"
    - "Action"
    - "Workflow/Relation Kind: On Result"
    - "Evaluation"
version: 2
updated_at: "2026-09-23 23:53:58 +0000"
relations:
  evaluation_for:
    - CA-O-080
    - CA-O-087
    - CA-O-088
  relates_to:
    - CA-E-486
    - CA-E-494
    - CA-E-500
---
# Summary

Validate the Atom Carrier Validation Workflow definition

## Claim

the Atom Carrier Validation definition check **must** reject a graph **or** binding that cannot preserve its declared read-only assessment boundary.

- require **=1** entry **and** **=1** Step node, a resolvable Step reference, **=1** Action per Step, explicit compatible input bindings, **and** admitted Workflow-scoped transitions.
- require reachable terminal outcomes for incomplete, invalid, valid, **and** execution-error cases as defined by the referenced Action; no outcome **may** be silently mapped **to** valid.
- verify that this graph is acyclic, contains no implicit retry **or** repair, **and** does **not** duplicate Action behavior inside its Step bindings **or** graph.
- verify that findings do **not** prevent assessment of independent targets, while missing authority **or** changed inputs cannot become proof of conformance.
- reference current self-sufficiency **and** source-binding Evaluations for the checked conditions; definition conformance **must not** be reported as a successful Tool execution.
