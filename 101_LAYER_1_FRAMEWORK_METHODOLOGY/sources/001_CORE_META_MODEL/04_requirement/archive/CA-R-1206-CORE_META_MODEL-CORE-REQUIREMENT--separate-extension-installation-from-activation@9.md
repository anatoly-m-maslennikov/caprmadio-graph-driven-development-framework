---
cce_version: cce_1
cce_form: separation
subjects:
  governs: "Extension Installation"
  depends_on:
    - "Extension"
    - "Project Configuration"
version: 9
updated_at: "2026-09-11 23:47:49 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Separate Extension Installation from Activation

installing an Extension **must** make its immutable authority available **to** Project Configuration **without** making the Extension authority applicable **to** the current Project.
