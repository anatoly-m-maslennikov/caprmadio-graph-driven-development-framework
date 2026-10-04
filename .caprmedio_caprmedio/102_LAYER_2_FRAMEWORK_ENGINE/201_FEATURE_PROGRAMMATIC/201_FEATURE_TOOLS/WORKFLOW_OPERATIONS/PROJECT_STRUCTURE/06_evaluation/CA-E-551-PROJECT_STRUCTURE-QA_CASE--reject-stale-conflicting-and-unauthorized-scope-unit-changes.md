---
atom_id: CA-E-551
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-04 23:02:03 +0400"
subjects:
  governs: "Tool/PROJECT_STRUCTURE rejection cases"
  depends_on: [Tool, Scope Unit, Project Structure, Operator]
relations:
  relates_to: [CA-R-1662, CA-R-1829, CA-R-1830, CA-R-1831]
---
# Summary

Reject stale, conflicting, and unauthorized Scope Unit changes

## Scope

Negative functional cases for currentness, complete declaration constraints, and approval boundaries through CA-D-527's shared service interface.

## Claim

The Evaluation **must** prove the Tool stops before mutation for stale state, invalid full declaration data, or insufficient exact authorization; service disposition stays distinct from a structural result state.

## Details

- Through one D527 request shape, mutate selected TOML/references after preview to obtain `stale`; submit duplicate identity/order, a parent cycle, blank label, incorrect structural level, negative navigation number, an Unordered `local_order`, an invalid authority mode, or invalid path to obtain `conflict` or the exact validation failure.
- Submit a folder-only observation, an expired/insufficient authorization, or an execute request that cannot pass D527 admission. Assert the applicable unstarted D527 `declined` or `blocked` disposition, no Run/Event identity, no structural effect, and no fabricated structural completion; do not manufacture a route-specific service result.
- Assert unchanged authoritative declarations and Carrier content for every case, exact failure reason and affected set, and the separately reported direct-parent Goal-coverage disposition where Create or Move exposes a gap.
