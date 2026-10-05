---
atom_id: CA-P-1685
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
subjects:
  governs: "Wire target-bound Draft lifecycle"
  depends_on: [Atom, Carrier, History, Runtime, Tool, Evaluation]
version: 1
updated_at: "2026-10-05 05:04:38 +0000"
relations:
  is_decomposition_of: [CA-P-1677]
  blocks: [CA-P-1638]
---
# Summary

Wire target-bound Draft lifecycle

## Objective

Within <=15 minutes, wire target-bound Draft lifecycle.

## Details

After accepted P1683/P1684, own only atom_operations.py/lifecycle_intents.py and focused tests/test_draft_promotion_golden.py. Wire Create, Demotion, Draft Update, and Promotion in that order. Preserve external baseline edits. Retire caller draft_identity_evidence. Bind actual history and changed-artifact refs; retain old Draft until observed finalized promotion permits removal; exact pending retry cannot allocate another identity. Golden cases cover both real P1638 forgeries, ordinary creation/demotion/update/promotion, replay and finalization recovery. No source/shared/MCP/manifest edits.

Inputs: accepted D568@5 64d2e60303d9dceeaee694263ebd888daf4bd217a794830896b1c5837517559d, D570@4 462ff2638fdba7050c83c27c9a8f974c1008c431cb46b4d8d81212d207ea1f37 and D569@5 ada92dcacfcf906878e3c3e3964281abd8e9c8b99336042564d565d2a79dd523. One Task, one Agent; preserve others. No source/Plans/Git/runtime/image writes or permission workaround. Existing development worker focused tests only, not immutable-image proof. Choose best authorized options; record C/Question and continue. If work cannot fit fifteen minutes, save exact partial frontier and bounded remainder.

## Definition of Done

Save exact code/test hashes, concrete API, genuine focused evidence and remaining coverage. Partial results do not close the parent or mandatory runtime gates.
