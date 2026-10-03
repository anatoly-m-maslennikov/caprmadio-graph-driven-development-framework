---
atom_id: CA-D-366
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - Project Settings/Authoritative Carrier/Content
  depends_on:
    continuant:
      - Project
      - Atom/Identifier/Project Prefix
      - Authority Mode
version: 1
updated_at: 2026-09-04 04:05:44 +0400
relations:
  child_of:
    - CA-D-364
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_LOCAL_CONFIGURATION/07_delivery/CA-D-366-LOCAL_CONFIGURATION-CORE-DELIVERY--serialize-project-settings-content-in-toml.md
---
# Serialize Project Settings Content in TOML

the authoritative Project Settings TOML Carrier **must** encode Project identity, Project Prefix, **and** Authority Modes **and** **must not** encode confidence thresholds, framework root locators, Tool settings, **or** Extension settings.
