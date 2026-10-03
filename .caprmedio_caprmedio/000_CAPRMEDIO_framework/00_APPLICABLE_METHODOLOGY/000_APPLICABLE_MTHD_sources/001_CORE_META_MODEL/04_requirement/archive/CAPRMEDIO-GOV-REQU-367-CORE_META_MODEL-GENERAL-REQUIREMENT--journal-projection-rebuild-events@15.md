---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Projection Rebuild"
  depends_on:
    - "Work Journal/Action"
    - "Projection"
    - "Journal/Record"
version: 15
updated_at: "2026-09-17 04:08:48 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Journal Projection Rebuild Events

**every** Projection Rebuild **must** have **`=1`** Work Journal Action whose terminal Event records the rebuild outcome.

acceptance of that Event into the Journal does **not**, by itself, make the Projection current. currentness remains subject **to** the Projection's applicable source **and** validation requirements; the accepted Event preserves the observed outcome **without** replacing those requirements.
