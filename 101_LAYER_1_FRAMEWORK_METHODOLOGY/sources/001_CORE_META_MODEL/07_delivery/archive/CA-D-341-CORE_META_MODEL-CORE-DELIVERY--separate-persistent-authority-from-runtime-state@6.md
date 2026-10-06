---
atom_id: CA-D-341
cce_version: cce_1
cce_form: separation
subjects:
  governs: "Carrier/Storage Boundary"
  depends_on:
    - "Framework-Owned Carrier"
    - "Project-Owned Carrier"
    - "Runtime State Carrier"
version: 6
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Separate Persistent Authority from Runtime State

Framework-Owned **and** Project-Owned persistent Carriers **must** remain outside Runtime State so Runtime State cleanup cannot remove canonical authority **or** Journal history.
