---
atom_id: CA-D-363
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Project Settings/Authoritative Carrier/Filename"
  depends_on:
    - "File Carrier"
    - "File Carrier/Format"
version: 5
updated_at: "2026-09-10 02:49:14 +0400"
relations:
  child_of:
    - CA-D-362
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize Project Settings Filename

the authoritative Project Settings TOML File Carrier filename **must** match `caprmedio_<project_name>_settings.toml`, where `<project_name>` is the exact lowercase Project name.
