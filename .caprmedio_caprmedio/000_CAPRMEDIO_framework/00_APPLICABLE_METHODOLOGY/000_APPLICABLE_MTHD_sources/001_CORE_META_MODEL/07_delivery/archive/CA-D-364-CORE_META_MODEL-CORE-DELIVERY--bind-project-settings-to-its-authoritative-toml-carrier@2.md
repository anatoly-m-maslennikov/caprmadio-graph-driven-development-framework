---
atom_id: CA-D-364
cce_version: cce_1
cce_form: delivery
subjects:
  governs:
    continuant:
      - Project Settings/Authoritative Carrier
  depends_on:
    continuant:
      - Project Settings/Authoritative Carrier/Filename
version: 2
updated_at: "2026-09-09 23:04:14 +0400"
relations:
  child_of:
    - CA-D-363
---
# Bind Project Settings to its authoritative TOML Carrier

the Project Settings Artifact for a Project named `<project_name>` **must** use `.caprmedio_<project_name>/caprmedio_<project_name>_settings.toml` as its **`=1`** authoritative TOML File Carrier.
