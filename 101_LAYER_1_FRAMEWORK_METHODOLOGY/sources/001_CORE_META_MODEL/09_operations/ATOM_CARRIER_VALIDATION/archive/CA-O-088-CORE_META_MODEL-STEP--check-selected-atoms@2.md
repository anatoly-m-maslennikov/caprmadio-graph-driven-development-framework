---
atom_id: CA-O-088
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Check Atoms Step"
  depends_on:
    - "Step"
    - "Action"
    - "Check Atoms"
    - "Workflow Run"
version: 2
updated_at: "2026-09-23 23:53:58 +0000"
relations:
  relates_to:
    - CA-O-087
---
# Summary

Check selected Atoms

## Claim

Check Atoms Step **means** the Workflow node that invokes **=1** Action, CA-O-087, with the admitted Workflow Run's source inventory, selector, applicable methodology, reference context, read boundaries, **and** execution limits.

- pass these inputs **without** independent reselection **or** inference from the Step's location.
- expose the Action's unchanged result tag **and** report payload **to** the Workflow.
