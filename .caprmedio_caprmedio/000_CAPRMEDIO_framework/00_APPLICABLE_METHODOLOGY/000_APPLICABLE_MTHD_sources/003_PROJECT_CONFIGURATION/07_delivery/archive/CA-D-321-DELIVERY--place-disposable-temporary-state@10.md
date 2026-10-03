---
subjects:
  governs: "CAPRMEDIO/Temporary State Carrier Root"
  depends_on: []
version: 10
updated_at: "2026-09-15 03:15:32 +0400"
relations: {}
atom_id: "CA-D-321"
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
---
# Place Disposable Temporary State

the caprmedio Project **must** place disposable scratch, staging, test cache, atomic-write intermediate, build intermediate, **and** interrupted-cleanup Carriers under `.caprmedio_tmp/`.

deleting `.caprmedio_tmp/` **must not** delete governed authority, Project Journal history, installed Framework Engine releases, runtime logs, sessions, databases, service state, **or** resumable state.
