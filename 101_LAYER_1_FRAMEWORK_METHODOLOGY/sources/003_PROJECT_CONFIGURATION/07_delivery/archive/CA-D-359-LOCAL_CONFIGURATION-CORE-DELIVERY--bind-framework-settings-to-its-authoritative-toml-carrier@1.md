---
atom_id: CA-D-359
cce_version: cce_1
cce_form: delivery
subjects:
  governs:
    continuant:
      - Project Configuration/Authoritative Carrier
  depends_on:
    continuant:
      - File Carrier
      - File Carrier/Format
version: 1
updated_at: 2026-09-04 03:52:00 +0400
relations:
  child_of:
    - CA-D-358
---
# Bind Framework Settings to Its Authoritative TOML Carrier

caprmedio_framework_settings **must** use `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_LOCAL_CONFIGURATION/caprmedio_framework_settings.toml` as its **`=1`** authoritative TOML File Carrier.
