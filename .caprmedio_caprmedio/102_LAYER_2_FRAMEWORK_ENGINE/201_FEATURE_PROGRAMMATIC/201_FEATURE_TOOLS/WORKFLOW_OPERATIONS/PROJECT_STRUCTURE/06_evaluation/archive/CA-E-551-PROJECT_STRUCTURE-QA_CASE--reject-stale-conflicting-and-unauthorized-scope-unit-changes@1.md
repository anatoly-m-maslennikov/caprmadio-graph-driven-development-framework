---
atom_id: CA-E-551
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 19:29:30 +0000"
subjects:
  governs: "Tool/PROJECT_STRUCTURE rejection cases"
  depends_on: [Tool, Scope Unit, Project Structure, Operator]
relations:
  relates_to: [CA-R-1662, CA-R-1829, CA-R-1830, CA-R-1831]
---
# Summary

Reject stale, conflicting, and unauthorized Scope Unit changes

## Scope

Negative functional cases for currentness, declaration constraints, and approval boundaries.

## Claim

The Evaluation **must** prove the Tool stops before mutation for stale state, duplicate identity/order, a parent cycle, an Unordered `local_order`, or insufficient exact authorization.

## Details

- Mutate the selected TOML/references after preparation to obtain `stale`; submit duplicate identity/order and a parent cycle to obtain `conflict`; submit a folder-only observation or expired/insufficient approval to obtain `permission_denied` or `blocked`.
- Assert unchanged authoritative declarations and Carrier content for every case, exact failure reason and affected set, and no fabricated Run where dispatch never began.
