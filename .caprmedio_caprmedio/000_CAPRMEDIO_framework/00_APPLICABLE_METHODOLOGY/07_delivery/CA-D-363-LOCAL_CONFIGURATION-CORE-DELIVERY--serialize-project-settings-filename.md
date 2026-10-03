---
atom_id: CA-D-363
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - Project Settings/Authoritative Carrier/Filename
  depends_on:
    continuant:
      - File Carrier
      - File Carrier/Format
version: 1
updated_at: 2026-09-04 04:05:44 +0400
relations:
  child_of:
    - CA-D-362
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_LOCAL_CONFIGURATION/07_delivery/CA-D-363-LOCAL_CONFIGURATION-CORE-DELIVERY--serialize-project-settings-filename.md
---
# Serialize Project Settings Filename

the authoritative Project Settings TOML File Carrier filename **must** match `caprmedio_<project_name>_settings.toml`, where `<project_name>` is the exact lowercase Project name.
