---
subject_scopes:
  - carrier-format
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 3
updated_at: 2026-08-21 03:26:58
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-487--encode-projection-update-time-without-version
  child_of:
    - CAPRMEDIO-META-REQU-166--projections-have-updated-at
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Encode Projection updated at

Every Projection frontmatter carries `updated_at` in `YYYY-MM-DD HH:MM:SS` format as the time of its latest completed rebuild in the configured Artifact timestamp timezone. Projection revision metadata consists exactly of `updated_at`; `updated_at` alone does not establish currentness.
