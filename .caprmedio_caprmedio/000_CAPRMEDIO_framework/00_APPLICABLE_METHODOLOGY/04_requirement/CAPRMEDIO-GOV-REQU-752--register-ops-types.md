---
cce_version: cce_1
cce_form: requirement
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Operations/Type"
project_graph_state:
  artifacts:
    enabled_types:
      - ops:release_record
      - ops:deployment_record
      - ops:environment_state
      - ops:health_record
      - ops:incident_record
version: 9
updated_at: 2026-08-29 04:33:13 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
    - CA-R-1054
  replacement_of:
    - CAPRMEDIO-GOV-REQU-332--register-ops-subtypes
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_LOCAL_CONFIGURATION/04_requirement/CAPRMEDIO-GOV-REQU-752--register-ops-types.md
---
# Register Type Values for Operations Atoms

GOVERNANCE registers Release Record, Deployment Record, Environment State, Health Record, **and** Incident Record with their existing lowercase Carrier tokens as internal values of `Atom/Content Role: Operations/Type`.
