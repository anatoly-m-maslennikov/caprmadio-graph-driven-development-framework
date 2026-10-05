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
version: 2
updated_at: "2026-10-05 01:57:56 +0000"
relations:
  evaluation_for: [CA-R-1825]
---
# Summary

Verify model-driven status dispatch

## Scope

Current status-model resolution for one selected Atom.

## Claim

Use fixtures with distinct admitted Content Role status models. Verify Tool-side Change Status and Archive derive only the actual carried Role and optional Type's current authoritative model, exact source/revision and destination mapping; a request with caller-forged Role/Type/model identity, unavailable, ambiguous, stale, mismatched or unadmitted authority/status is rejected with its diagnostic and no write. Verify that no fixed status list makes an otherwise valid model-specific request succeed or fail.

## Details

### Acceptance criteria

Each result identifies the resolved model source/revision, operation and authoritative destination decision. Prove Role/Type precedence, exact status casing, source-currentness, destination creation and collision handling, and same-status no-op. Rejected and preview cases leave all Carriers and history unchanged.
