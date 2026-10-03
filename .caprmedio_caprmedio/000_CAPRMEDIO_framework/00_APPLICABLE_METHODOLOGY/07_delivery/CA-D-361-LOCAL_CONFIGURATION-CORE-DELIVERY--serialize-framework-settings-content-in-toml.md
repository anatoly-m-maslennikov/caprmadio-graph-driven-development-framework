---
atom_id: CA-D-361
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - Framework Instance Settings/Authoritative Carrier/Content
  depends_on:
    continuant:
      - Tool
      - Extension
version: 2
updated_at: 2026-09-04 04:05:44 +0400
relations:
  child_of:
    - CA-D-359
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_LOCAL_CONFIGURATION/07_delivery/CA-D-361-LOCAL_CONFIGURATION-CORE-DELIVERY--serialize-framework-settings-content-in-toml.md
---
# Serialize Framework Settings Content in TOML

the authoritative caprmedio_framework_settings TOML Carrier **must** encode operator-editable confidence thresholds, the framework control-root locator, **`>=1`** code-root locators, active **and** background Tools with their settings, **and** enabled **or** disabled Extensions with retained per-Extension settings; it **must not** contain Project identity, Project Prefix, Authority Modes, Atom Frontmatter, Atom ID, Atom Revision metadata, Atom relations, rationale, **or** provenance.
