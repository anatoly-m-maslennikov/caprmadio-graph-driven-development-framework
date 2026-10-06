---
atom_id: CA-O-157
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 17:42:12 +0000"
subjects:
  governs: "Applicable Methodology Compilation/Step: publish"
  depends_on:
    - "Workflow"
    - "Step"
    - "Action"
    - "Workflow Run"
    - "Applicable Methodology"
    - "Publish Reconciled Projection"
    - "Atom"
    - "Atom/Revision"
    - "Atom/Claim"
    - "Applicable Methodology/Conflict"
    - "Applicable Methodology/Source Frontier Digest"
    - "Carrier"
    - "Projection/Type: Reconciled Projection"
relations:
  relates_to: [CA-O-011, CA-O-009]
---
# Summary

Publish the Applicable Methodology

## Operation

this Step is the publish node **of** CA-O-011, Applicable Methodology Compilation, invoking **`=1`** Action, CA-O-009, Publish Reconciled Projection.

### Inputs and parameters

bind the final reassessed source frontier from CA-O-153, the corresponding selection from CA-O-152, required valid decisions from CA-O-155 when applicable, and the Workflow Run's selected Projection Delivery authority.

preserve **every** selected Atom ID, exact source Revision, authority owner, **and** Claim under CA-R-1314 **and** CA-R-1316; enforce CA-R-1461 **and** CA-D-305 **and** CA-D-306 source identity, exact source Carrier bytes **and** Carrier form. fail **without** changing Applicable Methodology membership **if** **any** conflict remains unresolved **or** **any** required approval is invalid. produce the same ordered Applicable Methodology membership from the same resolved source frontier.

## Details
