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
version: 13
updated_at: "2026-09-11 22:30:02 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
---
# Register Type Values for Operations Atoms

Release Record, Deployment Record, Environment State, Health Record, **and** Incident Record **must** be registered as internal values of `Atom/Content Role: Operations/Type`.
