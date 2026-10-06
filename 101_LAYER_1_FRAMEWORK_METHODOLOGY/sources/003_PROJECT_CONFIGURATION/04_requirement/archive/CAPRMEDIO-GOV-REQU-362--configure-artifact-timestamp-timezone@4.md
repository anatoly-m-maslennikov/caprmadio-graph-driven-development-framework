---
subject_scopes:
  - settings
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
project_graph_state:
  artifact_timestamps:
    timezone: local
version: 4
updated_at: 2026-08-21 00:21:06
relations:
  child_of:
    - CAPRMEDIO-META-REQU-163--define-configuration-selection-and-precedence
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Configure the Artifact timestamp timezone

CAPRMEDIO resolves `updated_at` in the operator's local timezone by default. The project setting `[artifact_timestamps].timezone` may select `local`, `UTC`, or an IANA timezone name; every emitted value uses `YYYY-MM-DD HH:MM:SS`, and the setting supplies its timezone interpretation.
