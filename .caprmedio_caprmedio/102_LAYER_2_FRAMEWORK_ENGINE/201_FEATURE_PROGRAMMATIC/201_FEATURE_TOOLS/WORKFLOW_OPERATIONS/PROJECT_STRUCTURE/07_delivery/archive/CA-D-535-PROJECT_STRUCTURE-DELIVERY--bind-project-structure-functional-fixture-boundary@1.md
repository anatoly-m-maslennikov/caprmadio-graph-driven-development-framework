---
atom_id: CA-D-535
content_role: Delivery
type: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 19:29:30 +0000"
subjects:
  governs: "Tool/PROJECT_STRUCTURE functional fixture boundary"
  depends_on: [Tool, Scope Unit, Project Structure, Evaluation, Implementation]
relations:
  relates_to: [CA-E-549, CA-E-550, CA-E-551, CA-E-552]
---
# Summary

Bind PROJECT_STRUCTURE functional fixture boundary

## Scope

The disposable-project input/output boundary for the four golden functional cases.

## Claim

Delivery **must** provide an isolated project fixture whose authoritative TOML, reference/Carrier observations, request, expected result, and preservation/breakage assertions are inspectable independently.

## Details

- Fixture input includes declared Ordered and Unordered siblings, known incoming references, parent-owned attachments, observed Carrier content, and a captured TOML revision.
- Fixture output preserves pre/post TOML text or revision, exact Tool result, actual effect set, unchanged unrelated content check, and available Workflow/Action/Journal evidence references.
- This is a future implementation/test delivery boundary; saved RMED does not claim a runtime fixture or a passing functional run.
