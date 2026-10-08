---
atom_id: CA-P-1689
content_role: Plan
type: Plan
label: Task
work_sequence_number: 8
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
subjects:
  governs: "Exclude ephemeral Release inventory"
  depends_on: [Atom, Tool, Manifest, Evaluation, Runtime]
version: 1
updated_at: "2026-10-05 06:14:04 +0000"
relations:
  is_decomposition_of: [CA-P-1643]
  blocks: [CA-P-1644]
---
# Summary

Exclude ephemeral Release inventory

## Objective

Within <=15 minutes, exclude ephemeral Release inventory.

## Details

Own only release_inventory.py, release_handoff.py, release_packaging.py and focused release inventory tests. The current collectors include actual .caprmedio_tmp receipts under Engine as package sources. Introduce one shared source-inventory selection which preserves all persistent declared resources and excludes clearly ephemeral caches/temp state and .DS_Store. Refuse secret-named carriers before reading their bytes; no secret is deliverable. Keep canonical source-tree digest semantics consistent. Golden first for temporary/bytecode changes, complete persistent inventory, secret refusal before reads and regression handoff/compiler/package pipelines. No source/Plans/Git/runtime/image or actual release writes; coordinate the current suite/delivery helpers and preserve other edits.

## Definition of Done

Actual focused regression and failure cases pass with exact hashes and recovery evidence. This bounded repair does not close parent integration or mandatory image/Release gates.

### Current completed result

Shared release_inventory.py `01275013d3ac485dad917b099a3e981e3ef0cdbdb720fcfb411110651e1fa00f`, handoff `fee6a8b402389cb14400e955252d8350abd8c6853e79c91e0b44ffc038010b95`, packaging `39004e9ea6cf910118fcc551e4f98a3ab409af21eb495ee3c6408d795f98c399`; tests `da86862db1406b23d5fbfa3df43dcc2e67f09bfa3d75a86e4bc06d9c15ec0196` and common compiler fixture `73292dec8bab8738adcbf546b7cba5af7fbbc0369796d029520588f43b68b56e`. Four inventory, five compiler, thirteen handoff, five package, two pipeline, twelve delivery, thirteen suite and fifteen fake-image cases all pass. Unknown persistent resources remain; transient changes do not change sealed inventory; secret-shaped sentinels refuse before reads. Only the current exact pinned Docker COPY dependency instruction is supported, not a general parser. No actual Project release or image was executed.
