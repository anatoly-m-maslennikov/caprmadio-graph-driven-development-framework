---
cce_version: cce_1
cce_form: placement
subjects:
  governs: "CAPRMEDIO/Temporary State Carrier Root"
  depends_on: []
version: 7
updated_at: "2026-09-15 03:15:32 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Place Disposable Temporary State

the CAPRMEDIO Project **must** place disposable scratch, staging, test cache,
atomic-write intermediate, build intermediate, **and** interrupted-cleanup
Carriers under `.caprmedio_tmp/`.

deleting `.caprmedio_tmp/` **must not** delete governed authority, Project
Journal history, installed Framework Engine releases, runtime logs, sessions,
databases, service state, **or** resumable state.
