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
      - operations:release_record
      - operations:deployment_record
      - operations:environment_state
      - operations:health_record
      - operations:incident_record
version: 15
updated_at: 2026-09-15 05:51:38
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
---
# Register Type Values for Operations Atoms

Release Record, Deployment Record, Environment State, Health Record, **and** Incident Record **must** be registered as internal values of `Atom/Content Role: Operations/Type`.
