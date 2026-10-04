---
atom_id: CA-D-537
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 18:30:17 +0000"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/REVERT_CHANGES/Delivery"
  depends_on: [Tool, Workflow, Action, Journal, Implementation]
relations:
  delivery_for: [CA-R-1834, CA-E-553, CA-E-554]
---
# Summary

Bind REVERT_CHANGES delivery boundaries

## Scope

The delivery boundary between REVERT_CHANGES, governed reversal capabilities, and shared Run/Journal support.

## Claim

REVERT_CHANGES **must** deliver manifest validation, currentness guards, ordered effect orchestration, and truthful result assembly, while delegated governed effects and shared Journal serialization retain their existing authority.

## Details

Implementation belongs at the CA-D-536 entrypoint with functional mocks under the same Tool package. It calls supported governed effect capabilities only after admission/currentness checks; it never replaces CA-O-131's semantics, deletes history, performs a Git reset, or implements an internal failure rollback. It passes exact Run/Step/Action identity and evidence references to the accepted shared J01–J08 support and consumes its durable/pending receipts; it must not fork a second Journal schema or claim an unconfirmed append as durable.

Delivery is incomplete until CA-E-553 and CA-E-554 run through the real MCP boundary in the required Docker image. This RMED carrier authorizes no code before independent RMED review and no runtime-success claim.
