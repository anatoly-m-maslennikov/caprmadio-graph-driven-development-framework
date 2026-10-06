---
cce_version: cce_1
cce_form: requirement
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Delivery/Type"
project_graph_state:
  artifacts:
    enabled_types:
      - delivery:release_definition
      - delivery:environment_definition
version: 9
updated_at: 2026-08-29 04:33:13 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
    - CA-R-1054
  replacement_of:
    - CAPRMEDIO-GOV-REQU-331--register-delivery-subtypes
---
# Register Type Values for Delivery Atoms

GOVERNANCE registers Release Definition with Carrier token `release_definition` **and** Environment Definition with Carrier token `environment_definition` as internal values of `Atom/Content Role: Delivery/Type`.
