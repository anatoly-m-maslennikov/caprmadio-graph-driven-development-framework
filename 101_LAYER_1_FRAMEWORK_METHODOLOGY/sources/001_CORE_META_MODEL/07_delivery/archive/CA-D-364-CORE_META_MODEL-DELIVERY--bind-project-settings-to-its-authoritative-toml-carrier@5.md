---
atom_id: CA-D-364
cce_version: cce_1
cce_form: delivery
subjects:
  governs: "Project Settings/Authoritative Carrier"
  depends_on:
    - "Project Settings/Authoritative Carrier/Filename"
version: 5
updated_at: "2026-09-10 02:49:14 +0400"
relations:
  child_of:
    - CA-D-363
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Bind Project Settings to its authoritative TOML Carrier

the Project Settings Artifact for a Project named `<project_name>` **must** use `.caprmedio_<project_name>/caprmedio_<project_name>_settings.toml` as its **`=1`** authoritative TOML File Carrier.
