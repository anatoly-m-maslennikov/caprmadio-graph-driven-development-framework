---
atom_id: CA-D-407
cce_version: cce_1
cce_form: placement
subjects:
  governs: "Default Settings/Carrier"
  depends_on:
    - "Default Settings"
    - "File Carrier"
    - "Scope Unit"
    - "Methodology Source"
version: 2
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  child_of:
    - "CA-R-1441"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Store Default Settings with the Core Meta-Model source

the Default Settings Artifact **must** use `caprmedio_framework_default_settings.toml` **at** the root of the CORE_META_MODEL source Scope Unit as its **`=1`** authoritative TOML File Carrier.
