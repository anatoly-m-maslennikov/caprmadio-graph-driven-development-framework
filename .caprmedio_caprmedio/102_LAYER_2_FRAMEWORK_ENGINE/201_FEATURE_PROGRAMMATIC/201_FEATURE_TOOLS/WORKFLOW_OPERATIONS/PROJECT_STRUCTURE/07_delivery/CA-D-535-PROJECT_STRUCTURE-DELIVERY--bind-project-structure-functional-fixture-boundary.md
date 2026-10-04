---
atom_id: CA-D-535
content_role: Delivery
type: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-04 23:02:03 +0400"
subjects:
  governs: "Tool/PROJECT_STRUCTURE functional fixture boundary"
  depends_on: [Tool, Scope Unit, Project Structure, Evaluation, Implementation]
relations:
  relates_to: [CA-E-549, CA-E-550, CA-E-551, CA-E-552]
---
# Summary

Bind PROJECT_STRUCTURE functional fixture boundary

## Scope

The disposable-project input/output boundary for the four golden functional cases, including the one shared CA-D-527 request/result interface.

## Claim

Delivery **must** provide an isolated project fixture whose authoritative TOML, reference/Carrier observations, one CA-D-527 request/result, route `structural_result`, and preservation/breakage assertions are inspectable independently.

## Details

- Fixture input includes declared Ordered and Unordered siblings, nonempty labels, structural levels, navigational numbers, explicit and inherited authority modes, known incoming references, parent-owned attachments, observed Carrier content, captured TOML revision, and an explicit direct-parent Goal-coverage disposition for Create/Move.
- Fixture output preserves pre/post TOML text or revision, the exact D527 service result and separate `structural_result`, actual effect set, unchanged unrelated content check, and available Workflow/Action/Journal evidence references. It includes the default-preview/no-effect, unstarted-denial/no-effect, successful explicit-execute, and partial/authorized-rollback cases from CA-E-549/551/552 without a duplicate route envelope.
- This is a future implementation/test delivery boundary; saved RMED does not claim a runtime fixture or a passing functional run.
