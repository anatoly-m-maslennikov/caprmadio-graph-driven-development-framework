---
subject_scopes:
  - framework-boundary
tier: core
version: 1
updated_at: 2026-08-19 00:58:37
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - F4F-REQUIREMENT-261-prohibit-active-recursion
---
# Advance self-hosting through N plus one transitions

Active framework version `N` may govern creation and validation of version `N+1`; version `N+1` gains authority only through explicit adoption and must never retroactively govern its own creation or validation.
