---
atom_id: CA-O-085
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
  governs: "Assess Atom Carriers Step"
  depends_on:
    - "Step"
    - "Action"
    - "Assess Atom Carrier Conformance"
    - "Step Run"
version: 1
updated_at: "2026-09-23 23:38:45 +0000"
relations:
  relates_to:
    - CA-O-082
    - CA-O-084
---
# Summary

Assess prepared Atom Carriers

## Claim

Assess Atom Carriers Step **means** the Workflow node that invokes **=1** Action, CA-O-082, with the prepared payload returned by CA-O-084 **in** the same Workflow Run.

- bind targets, checks, fingerprints, selection evidence, **and** reference context **without** independently reselecting them.
- expose the Action's unchanged result tag **and** assessment payload **to** the Workflow.
