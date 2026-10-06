---
subject_scopes:
  - artifact-catalog
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
project_settings:
  artifacts:
    enabled_subtypes:
      - ops:release_record
      - ops:deployment_record
      - ops:environment_state
      - ops:health_record
      - ops:incident_record
version: 3
updated_at: 2026-08-19 04:33:37
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-473--register-release-record-ops-subtype
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Register Ops subtypes

GOV must register these direct subtypes of the internal `ops` Atom Type:

| Subtype | Governed unit |
| --- | --- |
| `release_record` | One successful release event with the exact frozen version and released manifest. |
| `deployment_record` | One bounded deployment event and its factual outcome. |
| `environment_state` | One bounded observation of the deployed state of one environment. |
| `health_record` | One bounded observation set describing runtime health. |
| `incident_record` | One bounded production incident and its observed impact. |

These subtypes record enacted facts and do not establish normative specification or planning authority.
