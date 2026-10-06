---
subjects:
  governs: "Project Settings/Authoritative Carrier"
  depends_on:
    - "Project Settings/Authoritative Carrier/Filename"
version: 7
updated_at: "2026-09-10 02:49:14 +0400"
relations:
  child_of:
    - CA-D-363
---
# Bind Project Settings to its authoritative TOML Carrier

the Project Settings Artifact for a Project named `<project_name>` **must** use `.caprmedio_<project_name>/caprmedio_<project_name>_settings.toml` as its **`=1`** authoritative TOML File Carrier.
