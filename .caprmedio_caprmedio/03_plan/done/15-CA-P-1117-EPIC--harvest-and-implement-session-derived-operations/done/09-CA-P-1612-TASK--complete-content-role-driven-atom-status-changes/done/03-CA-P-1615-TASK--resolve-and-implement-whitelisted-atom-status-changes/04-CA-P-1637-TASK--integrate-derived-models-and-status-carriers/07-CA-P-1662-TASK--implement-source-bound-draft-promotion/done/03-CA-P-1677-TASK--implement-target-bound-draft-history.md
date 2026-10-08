---
atom_id: CA-P-1677
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
  governs: "Implement target-bound Draft history"
  depends_on: [Atom, Carrier, History, Tool, Evaluation, Journal]
version: 1
updated_at: "2026-10-05 07:10:33 +0000"
relations:
  is_decomposition_of: [CA-P-1662]
  blocks: [CA-P-1638]
---
# Summary

Implement target-bound Draft history

## Objective

Implement target-bound Draft history through P1683-P1685; this is a composite, not an enlarged executable leaf.

## Details

After accepted P1676, implement only the existing Create/Demotion/Draft Update/Promotion lineage handoff in atom_operations.py and lifecycle_intents.py, with focused golden corpus additions. Preserve all external changes. The retained history entry must bind the actual current target path/bytes and direct origin; mutable caller/carrier fields alone must not select another identity. Cover both actual P1638 forgeries, ordinary create/demote/update/promote, changed Summary, missing/stale history and no-effect refusals. Existing development worker only. No shared route, source, manifest, environment/image or C447/C449 bypass.

P1676 now independently ACCEPTS exact D568@5 SHA-256 64d2e60303d9dceeaee694263ebd888daf4bd217a794830896b1c5837517559d, D570@4 462ff2638fdba7050c83c27c9a8f974c1008c431cb46b4d8d81212d207ea1f37 and D569@5 ada92dcacfcf906878e3c3e3964281abd8e9c8b99336042564d565d2a79dd523. Implement the unique current immutable history head and private exact-output-bound pending promotion, finalized only after actual output observation. Caller draft_identity_evidence is now retired, not corroboration. A focused draft_history.py helper is allowed if needed to keep source parsing/history/reservation logic cohesive. Golden tests first, then implementation. One Agent owns this complete bounded native delta; if actual remaining work cannot fit <=15 minutes, return exact partial frontier and bounded remainder rather than expand this leaf.

Choose the best authorized in-scope option when uncertain; record C/Question and continue. One Task, one Agent. You are not alone: preserve all other work. No broad harvesting, source campaign or denied-operation workaround.

## Definition of Done

Save exact source/code hashes, the actual bounded result, genuine evidence and remaining coverage. A rejected review or partial test does not close the parent or mandatory runtime gates.

### Current accepted completion

Required source and helper children are complete: P1675/P1676/P1681 accept the current target-bound history sources; P1683/P1684/P1690 implement independently accepted atomic history/pending recovery; P1685/P1694/P1699 complete native wiring and both original origin substitutions plus the later Update head gap. Current native acceptance is98%; focused native/status23 and previously accepted shared status/Journal8 pass. Required image/runtime proof remains separate.
