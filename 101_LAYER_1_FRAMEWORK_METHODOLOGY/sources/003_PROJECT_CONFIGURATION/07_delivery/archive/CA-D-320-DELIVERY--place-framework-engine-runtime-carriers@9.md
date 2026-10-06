---
cce_version: cce_1
cce_form: placement
subjects:
  governs: "CAPRMEDIO/Framework Engine Runtime Carrier Root"
  depends_on: []
version: 9
updated_at: "2026-09-15 04:04:21 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Place Framework Engine Runtime Carriers

the caprmedio Project **must** place its selected running Framework Engine releases, stable launchers, Tools, Apps, Skills, logs, sessions, databases, service state, **and** resumable execution state under `.caprmedio_runtime/`.

the Framework Engine Runtime Carrier Root **must** remain non-authoritative. its selected releases, stable launchers, Tools, Apps, **and** Skills **must** be reconstructible from governed source **and** configuration. its logs, sessions, databases, service state, **and** resumable execution state **may** contain a non-reconstructible operational timeline. deleting the Runtime Carrier Root **may** require reinstallation **or** lose operational history but **must not** delete governed authority **or** Project Journal history.
