---
artifact_subtype: rationale
subject_scopes:
  - session-access
version: 2
updated_at: 2026-08-18 22:44:59
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  rationale_for:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-580--require-per-run-approval-for-raw-session-access
---
# Bound raw session access

Raw transcript reads consume tokens and may expose unrelated or protected context, so per-run operator approval bounds both cost and access.
