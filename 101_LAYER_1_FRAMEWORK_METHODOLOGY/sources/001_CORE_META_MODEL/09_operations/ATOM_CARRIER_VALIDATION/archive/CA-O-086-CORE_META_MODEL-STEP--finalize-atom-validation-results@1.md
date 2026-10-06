---
atom_id: CA-O-086
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Finalize Atom Validation Step"
  depends_on:
    - "Step"
    - "Action"
    - "Finalize Atom Carrier Validation"
    - "Step Run"
version: 1
updated_at: "2026-09-23 23:38:45 +0000"
relations:
  relates_to:
    - CA-O-083
    - CA-O-084
    - CA-O-085
---
# Summary

Finalize Atom validation results

## Claim

Finalize Atom Validation Step **means** the Workflow node that invokes **=1** Action, CA-O-083, with the prepared payload from CA-O-084 **and** the assessment payload from CA-O-085 **in** the same Workflow Run.

- preserve any incomplete assessment **and** existing findings; do **not** replace them with an empty success result.
- expose the Action's unchanged terminal result **and** report payload **to** the Workflow.
