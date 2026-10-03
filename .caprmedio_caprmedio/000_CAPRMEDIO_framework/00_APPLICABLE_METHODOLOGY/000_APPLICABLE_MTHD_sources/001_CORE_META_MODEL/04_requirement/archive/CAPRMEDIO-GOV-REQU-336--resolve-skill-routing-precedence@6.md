---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    continuant:
      - public-interface
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 6
updated_at: 2026-08-29 01:16:37 +0400
relations:
  child_of:
    - CA-R-1054
---
# Resolve skill routing precedence

Skill routes **must** resolve by explicit precedence: project-local CAPRMEDIO routes override framework routes, which override provider-global routes.
