---
atom_id: CA-D-361
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - Project Configuration/Authoritative Carrier/Content
  depends_on:
    continuant:
      - Tool
      - Extension
version: 1
updated_at: 2026-09-04 03:52:00 +0400
relations:
  child_of:
    - CA-D-359
---
# Serialize Framework Settings Content in TOML

the authoritative caprmedio_framework_settings TOML Carrier **must** encode operator-editable confidence thresholds, the framework control-root locator, **`>=1`** code-root locators, active **and** background Tools with their settings, **and** enabled **or** disabled Extensions with retained per-Extension settings; it **must not** contain Atom Frontmatter, Atom ID, Atom Revision metadata, Atom relations, rationale, **or** provenance.
