---
atom_id: CA-P-1545
content_role: Plan
type: Plan
label: Task
work_sequence_number: 19
current_scope_unit: caprmedio
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Repair Journal query snapshot trust and golden coverage"
  depends_on: [Implementation, Workflow, Action, Evaluation, Journal]
version: 3
updated_at: "2026-10-04 22:41:20 +0000"
relations:
  is_decomposition_of: [CA-P-1520]
  blocks: [CA-P-1547]
---
# Summary

Repair Journal query snapshot trust and golden coverage

## Objective

Within <=15 minutes, complete this bounded repair or acceptance packet with saved source-bound evidence.

## Details

Latest repair: CA-P-1547 found successful parser statistics were lost when local selector admission rejected a filter. The worker now records parser consumption before local selector validation. Invalid and protected selectors retain exact token/depth/IN statistics; all 14 Journal tests passed in Docker. The native opaque snapshot and bounded query proof are otherwise unchanged. Fresh CA-P-1547 acceptance remains required.

Inputs: accepted CA-P-1535 Journal source pins and CA-P-1544 REJECT, especially CA-R-1861/1865/1866, CA-M-334, CA-D-556 and CA-E-575 through CA-E-579. Ownership: only FIND_AND_FETCH_JOURNAL_EVENTS implementation, package export and its tests. Authenticate/retain captured snapshots on the server; never trust caller-rehashed records, members, settings or roots. Verify the configured canonical _journal boundary and retained members-to-records derivation without continuation enumeration or implicit recapture; preserve sealed-prefix append semantics and public snapshot information without leaking raw internal records. A changed or unknown snapshot must fail truthfully. Add adversarial forged-record/member/root/configuration cases, arrays/objects, malformed/missing-ID/unreadable input, actual bounded budget diagnostics and protected-sentinel access-count proof. Integrate CA-P-1548's additive sole-parser statistics API after it lands for truthful consumption; do not own query_filter.py or create another parser. Retain existing API behavior where safe; coordinate any opaque-handle compatibility change with root before MCP integration. E578/E580 admitted shared-Run/standalone execution proof remains CA-P-1527, not falsely claimed by pure core tests. Reproduce failures before repairs and pass the real golden corpus in the existing disposable development Docker worker. No source/Plan/Journal/MCP/manifest edits, no real Project mutations.

Inherit CA-P-1117's 90% confidence threshold and explicit mechanical Git save exception. You are not alone; preserve other workers' edits and use apply_patch. No harvesting, FPF, broad audit, permission bypass, deployment or unrelated changes. Root owns Plan updates and commits. If unfinished, return exact remainder; do not mark the aggregate Epic Done.

### Definition of Done

The owned packet has actual scoped evidence and a truthful saved result. The final fifteen-Workflow Docker/MCP proof remains separate.

### Result

Done for the bounded repair only. Journal snapshots are opaque server-retained capabilities; forged records, members, configured roots and changed handle metadata fail closed. Continuations verify retained canonical Journal prefixes and exclude later appends. Diagnostics use the sole parser's observed statistics. Root ran all 13 Journal golden tests in the disposable Docker worker successfully. The shared parser's 7 tests also passed. Code is included in 615b49250; no MCP, queue, Run-recording or fresh-image claim is made. Handles remain process-local and return unknown-snapshot after restart. CA-P-1547 independently reviews the repaired contract; CA-P-1527 must bind capture to the actual pre-Run dispatch lifecycle without implicit recapture.
