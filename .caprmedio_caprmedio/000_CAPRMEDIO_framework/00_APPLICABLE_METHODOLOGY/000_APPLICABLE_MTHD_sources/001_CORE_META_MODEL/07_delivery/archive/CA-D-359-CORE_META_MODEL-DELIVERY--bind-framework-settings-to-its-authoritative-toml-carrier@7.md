---
cce_version: cce_1
cce_form: delivery
subjects:
  governs: "Framework Instance Settings/Authoritative Carrier"
  depends_on:
    - "File Carrier"
    - "File Carrier/Format"
version: 7
updated_at: "2026-09-10 02:49:14 +0400"
relations:
  child_of:
    - CA-D-358
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Bind Framework Settings to Its Authoritative TOML Carrier

the Framework Instance Settings Artifact for a Project named `<project_name>` **must** use `.caprmedio_<project_name>/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml` as its **`=1`** authoritative TOML File Carrier.
