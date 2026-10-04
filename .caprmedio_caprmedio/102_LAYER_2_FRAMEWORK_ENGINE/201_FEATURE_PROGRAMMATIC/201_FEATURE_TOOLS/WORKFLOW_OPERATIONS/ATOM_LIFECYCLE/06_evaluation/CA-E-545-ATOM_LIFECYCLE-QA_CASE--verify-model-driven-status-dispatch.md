---
atom_id: CA-E-545
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Workflow Operations/Atom Lifecycle/Status Dispatch"
  depends_on: ["Atom", "Atom/Status", "Artifact/Carrier"]
version: 1
updated_at: "2026-10-04 18:30:23 +0000"
relations:
  evaluation_for: [CA-R-1825]
---
# Summary

Verify model-driven status dispatch

## Scope

Current status-model resolution for one selected Atom.

## Claim

Use fixtures with distinct admitted Content Role status models. Verify Change Status and Archive resolve only the fixture's current admitted model and model revision; a request with an unavailable, ambiguous, stale, or unadmitted status is rejected with its diagnostic and no write. Verify that no fixed status list makes an otherwise valid model-specific request succeed or fail.

## Details

### Acceptance criteria

Each result identifies the resolved model revision and operation. Rejected and preview cases leave all Carriers and history unchanged.
