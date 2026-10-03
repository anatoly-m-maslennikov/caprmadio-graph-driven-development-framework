---
atom_id: CAPRMEDIO-GOV-REQU-336
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "public-interface"
  depends_on: []
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 11
updated_at: "2026-09-11 22:30:02 +0400"
relations: {}
---
# Resolve skill routing precedence

Skill routes **must** resolve by explicit precedence: project-local CAPRMEDIO routes override framework routes, which override provider-global routes.
