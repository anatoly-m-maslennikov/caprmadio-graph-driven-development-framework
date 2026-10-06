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
version: 3
updated_at: "2026-09-10 02:49:14 +0400"
relations:
  child_of:
    - CA-D-362
---
# Serialize Project Settings Filename

the authoritative Project Settings TOML File Carrier filename **must** match `caprmedio_<project_name>_settings.toml`, where `<project_name>` is the exact lowercase Project name.
