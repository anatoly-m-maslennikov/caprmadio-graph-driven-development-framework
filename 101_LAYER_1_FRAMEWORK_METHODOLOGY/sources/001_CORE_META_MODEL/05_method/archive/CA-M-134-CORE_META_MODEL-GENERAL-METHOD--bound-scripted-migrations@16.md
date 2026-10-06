---
atom_id: CA-M-134
cce_version: cce_1
cce_form: method
subjects:
  governs: "Scripted Migration"
  depends_on:
    - "Target Set"
version: 16
updated_at: "2026-09-16 23:48:40 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Bound Scripted Migrations

**to** perform a Scripted Migration, the Agent **must** bind it to an exact governed Target Set, fail **when** an expected target is absent, **and** produce a reviewable change set.
