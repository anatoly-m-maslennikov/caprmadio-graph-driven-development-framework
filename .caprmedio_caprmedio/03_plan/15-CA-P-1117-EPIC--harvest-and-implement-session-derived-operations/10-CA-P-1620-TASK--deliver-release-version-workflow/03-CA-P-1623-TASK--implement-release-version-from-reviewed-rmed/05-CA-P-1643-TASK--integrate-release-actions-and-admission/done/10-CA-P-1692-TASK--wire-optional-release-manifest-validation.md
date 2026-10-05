---
atom_id: CA-P-1692
content_role: Plan
type: Plan
label: Task
work_sequence_number: 10
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
subjects:
  governs: "Wire optional Release manifest validation"
  depends_on: [Tool, Manifest, Workflow, Evaluation]
version: 1
updated_at: "2026-10-05 06:14:04 +0000"
relations:
  is_decomposition_of: [CA-P-1643]
  blocks: [CA-P-1644]
---
# Summary

Wire optional Release manifest validation

## Objective

Within <=15 minutes, wire optional additive Release source validation into the canonical manifest loader.

## Details

After P1687, own only MCP/selected_routes.py and new tests/test_release_manifest_admission.py. The loader preserves its current fifteen-route schema/digest/query checks when Release is absent and admits the optional sixteenth entry only with the exact accepted D572 record and source pins. Reject raw duplicate JSON keys, malformed or stale evidence before shared support. Preserve D527's request shape and current registry; no production manifest writes, live registration or dispatch, APP/provider edits, image/runtime work or C447/C449 workaround. This preparatory loader change does not establish a working sixteenth capability. Golden compatibility and strict refusal tests first with disposable Project fixtures.

## Definition of Done

Actual fifteen-route regressions and additive admission/refusal tests pass with exact code hashes. Native Release entrypoint/provider/registration and functional proof remain required.

### Current completed result

selected_routes.py `08efa0655e9bb4bc9616312d322b03d9793a6f158b9506f81865e744e51b011e`; tests `9ccea36dae9b6ee3319e4e7064354b7acc10cfa7185cbaa287b3e88079b875a5`. Twenty-one scoped tests pass: seven loader, eight admission and six existing guards. Raw duplicate keys reject before collapse; exact fifteen or trailing additive Release loading preserves existing source/query/self/binding digest checks. Static public registration remains fifteen; D527 and production manifest remain unchanged. The broader twenty-seven run had two old status-fixture failures, tracked by C464/P1695 rather than claimed clean. Native Release providers, registration and actual functional proof remain required.
