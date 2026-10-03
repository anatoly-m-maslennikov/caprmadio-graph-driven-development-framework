---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - settings
version: 13
updated_at: 2026-09-04 04:05:44 +0400
relations:
  child_of:
    - CA-R-1052
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_LOCAL_CONFIGURATION/05_method/CA-M-137-GOVERN-CORE-METHOD--resolve-both-settings-artifacts-and-the-scope-unit-graph-separately.md
---
# Resolve Both Settings Artifacts and the Scope Unit Graph Separately

**every** CAPRMEDIO Skill **must** resolve caprmedio_framework_settings through its authoritative TOML Carrier, resolve caprmedio_<project_name>_settings through the authoritative Project Settings TOML Carrier for the current Project, **and** resolve the Project Scope Unit Graph through its registered generated Projection addresses, **without** substituting a Projection for either settings authority **or** treating either Settings Artifact as derived graph state.
