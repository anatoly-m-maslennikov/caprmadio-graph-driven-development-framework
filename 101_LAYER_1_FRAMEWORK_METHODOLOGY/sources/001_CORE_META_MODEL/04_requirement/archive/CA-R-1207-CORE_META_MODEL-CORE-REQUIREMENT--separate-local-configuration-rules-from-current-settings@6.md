---
atom_id: CA-R-1207
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Local Configuration
  depends_on:
    continuant:
      - Project
      - Extension
      - Framework Instance Settings
version: 6
updated_at: 2026-09-07 09:59:57 +0000
relations: {}
---
# Separate Local Configuration Rules from Current Settings

the Local Configuration **must** own Project-specific expansion rules, constraints, **and** defaults **only** **where** the Core Meta-Model permits expansion; current Extension activation **and** selected Extension revisions **must** remain owned by the Framework Instance Settings Artifact, **not** duplicated in Local Configuration Atoms.
