---
cce_version: cce_1
cce_form: requirement
subjects:
  governs: "Atom/Claim"
  depends_on:
    - "GOVERNS"
    - "Subject"
version: 8
updated_at: "2026-09-14 04:00:22 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Split at Multiple Governed Subject Boundaries

an Atom **must** be split **if** its Claim governs **`>1`** canonical targets through GOVERNS Subject Relations, whether those targets are Entities, Actions, **or** Processes.
