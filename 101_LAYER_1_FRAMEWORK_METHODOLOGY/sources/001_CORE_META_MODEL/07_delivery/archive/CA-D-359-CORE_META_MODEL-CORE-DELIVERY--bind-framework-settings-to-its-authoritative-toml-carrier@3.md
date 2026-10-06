---
atom_id: CA-D-359
cce_version: cce_1
cce_form: delivery
subjects:
  governs:
    continuant:
      - Framework Instance Settings/Authoritative Carrier
  depends_on:
    continuant:
      - File Carrier
      - File Carrier/Format
version: 3
updated_at: "2026-09-09 23:04:14 +0400"
relations:
  child_of:
    - CA-D-358
---
# Bind Framework Settings to Its Authoritative TOML Carrier

the Framework Instance Settings Artifact for a Project named `<project_name>` **must** use `.caprmedio_<project_name>/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml` as its **`=1`** authoritative TOML File Carrier.
