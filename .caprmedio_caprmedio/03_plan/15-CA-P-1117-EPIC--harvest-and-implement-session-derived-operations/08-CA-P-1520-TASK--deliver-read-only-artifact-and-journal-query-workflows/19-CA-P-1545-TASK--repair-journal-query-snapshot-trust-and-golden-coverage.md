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
status: Active
subjects:
  governs: "Repair Journal query snapshot trust and golden coverage"
  depends_on: [Implementation, Workflow, Action, Evaluation, Journal]
version: 1
updated_at: "2026-10-04 22:09:50 +0000"
relations:
  is_decomposition_of: [CA-P-1520]
  blocks: [CA-P-1547]
---
# Summary

Repair Journal query snapshot trust and golden coverage

## Objective

Within <=15 minutes, complete this bounded repair or acceptance packet with saved source-bound evidence.

## Details

Inputs: accepted CA-P-1535 Journal source pins and CA-P-1544 REJECT, especially CA-R-1861/1865/1866, CA-M-334, CA-D-556 and CA-E-575 through CA-E-579. Ownership: only FIND_AND_FETCH_JOURNAL_EVENTS implementation, package export and its tests. Authenticate/retain captured snapshots on the server; never trust caller-rehashed records, members, settings or roots. Verify the configured canonical _journal boundary and retained members-to-records derivation without continuation enumeration or implicit recapture; preserve sealed-prefix append semantics and public snapshot information without leaking raw internal records. A changed or unknown snapshot must fail truthfully. Add adversarial forged-record/member/root/configuration cases, arrays/objects, malformed/missing-ID/unreadable input, actual bounded budget diagnostics and protected-sentinel access-count proof. Integrate CA-P-1548's additive sole-parser statistics API after it lands for truthful consumption; do not own query_filter.py or create another parser. Retain existing API behavior where safe; coordinate any opaque-handle compatibility change with root before MCP integration. E578/E580 admitted shared-Run/standalone execution proof remains CA-P-1527, not falsely claimed by pure core tests. Reproduce failures before repairs and pass the real golden corpus in the existing disposable development Docker worker. No source/Plan/Journal/MCP/manifest edits, no real Project mutations.

Inherit CA-P-1117's 90% confidence threshold and explicit mechanical Git save exception. You are not alone; preserve other workers' edits and use apply_patch. No harvesting, FPF, broad audit, permission bypass, deployment or unrelated changes. Root owns Plan updates and commits. If unfinished, return exact remainder; do not mark the aggregate Epic Done.

### Definition of Done

The owned packet has actual scoped evidence and a truthful saved result. The final fifteen-Workflow Docker/MCP proof remains separate.

