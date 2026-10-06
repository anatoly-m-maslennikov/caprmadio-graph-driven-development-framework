---
cce_version: cce_1
cce_form: obligation
subjects:
  - settings
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
project_graph_state:
  artifact_timestamps:
    timezone: local
version: 7
updated_at: 2026-08-23 12:02:00
relations:
  child_of:
    - CAPRMEDIO-META-REQU-163--define-configuration-selection-and-precedence
    - CA-R-1054
---
# Configure the Artifact timestamp timezone

CAPRMEDIO resolves `updated_at` in the operator's local timezone by default. The project setting `[artifact_timestamps].timezone` MAY select `local`, `UTC`, or an IANA timezone name; every emitted value uses `YYYY-MM-DD HH:MM:SS`, and the setting supplies its timezone interpretation.
