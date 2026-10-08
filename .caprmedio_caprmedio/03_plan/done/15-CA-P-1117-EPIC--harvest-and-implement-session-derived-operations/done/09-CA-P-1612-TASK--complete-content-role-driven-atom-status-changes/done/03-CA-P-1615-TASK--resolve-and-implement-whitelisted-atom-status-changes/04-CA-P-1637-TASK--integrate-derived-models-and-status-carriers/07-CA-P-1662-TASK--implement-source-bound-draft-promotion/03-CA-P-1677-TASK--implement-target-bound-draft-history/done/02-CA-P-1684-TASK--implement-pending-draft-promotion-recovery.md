---
atom_id: CA-P-1684
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
subjects:
  governs: "Implement pending Draft promotion recovery"
  depends_on: [Atom, Carrier, History, Runtime, Tool, Evaluation]
version: 1
updated_at: "2026-10-05 06:14:04 +0000"
relations:
  is_decomposition_of: [CA-P-1677]
  blocks: [CA-P-1685]
---
# Summary

Implement pending Draft promotion recovery

## Objective

Within <=15 minutes, implement pending Draft promotion recovery.

## Details

After P1683's concrete API exists, own only draft_promotion_pending.py and tests/test_draft_promotion_pending.py. Golden first. Implement private non-consuming pending transition storage with exact head/request/planned identity/output binding, competing-promotion refusal, same-transition retry, observed-output finalization and truthful pending failures. Pending state is ephemeral runtime context, not canonical history or a Journal. Coordinate P1683's API; no native lifecycle or source edits.

Inputs: accepted D568@5 64d2e60303d9dceeaee694263ebd888daf4bd217a794830896b1c5837517559d, D570@4 462ff2638fdba7050c83c27c9a8f974c1008c431cb46b4d8d81212d207ea1f37 and D569@5 ada92dcacfcf906878e3c3e3964281abd8e9c8b99336042564d565d2a79dd523. One Task, one Agent; preserve others. No source/Plans/Git/runtime/image writes or permission workaround. Existing development worker focused tests only, not immutable-image proof. Choose best authorized options; record C/Question and continue. If work cannot fit fifteen minutes, save exact partial frontier and bounded remainder.

## Definition of Done

Save exact code/test hashes, concrete API, genuine focused evidence and remaining coverage. Partial results do not close the parent or mandatory runtime gates.

## Result

Implemented private pending recovery: draft_promotion_pending.py `02bdedc025ebc21c4c1f6100a161c762bd510a52306db388aebf47c60ecf738e`; focused tests `a6329f9123c0134caa9cf69739ad550fd877d59315e2ac93b583bcab663c2767`. APIs reserve_pending_promotion, finalize_pending_promotion and pending_promotion_path bind exact head/request/planned identity/output without consuming history. Six focused tests and seven history regressions pass in disposable development fixtures. Terminal receipts make finalized retry idempotent after old-Draft removal. P1685 native wiring and independent code acceptance remain required; no actual Project promotion or MCP/image proof occurred.

### Current review disposition

Reopened after independent helper review REJECT at98%. Concurrent finalizers created two consuming successors; terminal-receipt recovery failed after old-Draft removal. Initial focused passes remain historical, not current acceptance. C462 and P1690 bind the repair and regression proof before native integration can close.

### Current completed result

Eight pending cases now pass, including concurrent public finalizers and terminal-write failure followed by Draft removal. Current pending module `d1583d06afd35915a030ef5114802ce65d1f4fce7a0667d1b80a510208aa4410` and tests `5ad7e9640a0054aa7a45e17da22b0353b5db0736dd23f1e00675b480b0a33639` are independently ACCEPT at97% through P1690. Supported lookup/recovery precedes missing-Draft validation and reuses one finalized successor. Native retry proof remains separate.
