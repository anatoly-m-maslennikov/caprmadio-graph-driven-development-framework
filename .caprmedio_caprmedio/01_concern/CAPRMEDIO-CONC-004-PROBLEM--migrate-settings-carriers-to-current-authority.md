---
atom_id: CAPRMEDIO-CONC-004
cce_version: cce_1
cce_form: observation
subjects:
  governs:
    continuant:
      - "settings Carrier migration"
  depends_on:
    continuant:
      - "Project Settings"
      - "Framework Instance Settings"
      - "Carrier"
version: 3
updated_at: "2026-09-09 23:04:14 +0400"
relations:
  concern_about:
    - "CAPRMEDIO-META-REQU-619"
    - "CA-R-1402"
    - "CA-D-359"
    - "CA-D-364"
    - "CA-D-361"
    - "CA-D-366"
---
# Migrate settings Carriers to current authority

the existing `.caprmedio_caprmedio/caprmedio_project_settings.toml` still declares itself a generated Projection **and** retains Framework Instance fields, including Authority Modes. the Framework Instance Settings Carrier still resides under the legacy repository-level framework directory. the Atoms specify authoritative Project initialization inputs, separate instance choices, **and** project-owned locations, but the actual TOML Carriers, selected-value migration, **and** consuming Tools have **not** yet been reconciled. updating Atom authority does **not** establish settings migration **or** runtime readiness.
