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
status: Done
subjects:
  governs: "Wire target-bound Draft lifecycle"
  depends_on: [Atom, Carrier, History, Runtime, Tool, Evaluation]
version: 1
updated_at: "2026-10-05 07:10:33 +0000"
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

### Current accepted completion

P1694 and independently accepted P1699 complete this bounded native wiring. Create, Demotion, Draft Update and Promotion use accepted D568@5/D570@4/D569@5 retained target history and exact pending recovery. Native nine and model-status fourteen tests pass; the isolated owned staged delta also passes all23 without including external legacy-migration changes. Isolated atom_operations.py 0eac7b8166843480e82a23158510f0b643a98ccc73f5cccfb0df9b0385ab62ea; isolated lifecycle_intents.py 7bce9d70bdeb6681aaf5ce448b5412c34526e02dd4182b0e1bc08aae24050f2b. No actual image/MCP or permission-bound work is closed.
