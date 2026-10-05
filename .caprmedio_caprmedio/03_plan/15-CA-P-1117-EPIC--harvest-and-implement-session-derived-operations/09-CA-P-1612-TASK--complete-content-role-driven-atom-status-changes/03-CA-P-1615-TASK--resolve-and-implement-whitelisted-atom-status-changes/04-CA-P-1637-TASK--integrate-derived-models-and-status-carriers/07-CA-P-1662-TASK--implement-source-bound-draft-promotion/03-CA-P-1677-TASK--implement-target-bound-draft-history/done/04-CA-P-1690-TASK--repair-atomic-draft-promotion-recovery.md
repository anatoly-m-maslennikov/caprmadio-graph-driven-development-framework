---
atom_id: CA-P-1690
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
subjects:
  governs: "Repair atomic Draft promotion recovery"
  depends_on: [Atom, Tool, Manifest, Evaluation, Runtime]
version: 1
updated_at: "2026-10-05 06:14:04 +0000"
relations:
  is_decomposition_of: [CA-P-1677]
  blocks: [CA-P-1685]
---
# Summary

Repair atomic Draft promotion recovery

## Objective

Within <=15 minutes, repair atomic Draft promotion recovery.

## Details

Own only draft_history.py, draft_promotion_pending.py and their focused tests. Independent review reproduced two consuming promotion children for one head, and unrecoverable terminal-receipt failure after old-Draft removal. Make per-head match/validate/append consumption atomic, recover an exact already-observed successor without requiring its consumed Draft, and expose a supported pending lookup/recovery API for native P1685 before fresh identity/output preparation. Golden first forced concurrent finalizers, terminal-write failure plus Draft removal, stable exact retry, competing request refusal and no second identity. Preserve current APIs and external/native edits. No source/Plans/Git/image/runtime-repo or permission workaround; focused disposable tests only.

## Definition of Done

Actual focused regression and failure cases pass with exact hashes and recovery evidence. This bounded repair does not close parent integration or mandatory image/Release gates.

### Current completed result

Independent re-review ACCEPT at97%: sixteen focused helper cases pass, including the two originally rejecting probes. Concurrent finalizers converge on the same successor; terminal-write failure plus old-Draft removal now returns finalized on recovery and replay, with history_entries2. Current history SHA b6cda4302807a1ac7c1cbc79aecc12878559a2d65745d4e83e7fcd17491cb6d2; pending SHA d1583d06afd35915a030ef5114802ce65d1f4fce7a0667d1b80a510208aa4410. Native P1694 and current native review remain required.
