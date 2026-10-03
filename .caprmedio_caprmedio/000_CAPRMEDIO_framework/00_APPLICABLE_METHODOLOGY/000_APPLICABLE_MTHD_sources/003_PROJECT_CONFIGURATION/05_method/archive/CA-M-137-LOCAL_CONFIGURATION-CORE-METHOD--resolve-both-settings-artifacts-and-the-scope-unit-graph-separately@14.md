---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - settings
version: 14
updated_at: "2026-09-09 21:56:59 +0400"
relations:
  child_of:
    - CA-R-1052
---
# Resolve Both Settings Artifacts and the Scope Unit Graph Separately

**every** CAPRMEDIO Skill **must** resolve caprmedio_framework_settings through its authoritative TOML Carrier, resolve caprmedio_<project_name>_settings through the authoritative Project Settings TOML Carrier for the current Project, **and** resolve the Project Scope Unit Graph through its registered generated Projection addresses, **without** substituting a Projection for either settings authority **or** treating either Settings Artifact as derived graph state.
