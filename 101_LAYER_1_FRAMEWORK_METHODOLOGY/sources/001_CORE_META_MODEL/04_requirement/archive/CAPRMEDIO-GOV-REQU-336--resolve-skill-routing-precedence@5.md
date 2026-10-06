---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    continuant:
      - public-interface
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 5
updated_at: 2026-08-23 15:00:38
relations:
  child_of:
    - CA-R-1054
---
# Resolve skill routing precedence

Skill routes MUST resolve by explicit precedence: project-local CAPRMEDIO routes override framework routes, which override provider-global routes.
