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
# Break initial recursion with a Bootstrap Seed

A self-hosting framework must break its initial recursion through a finite, non-recursive Bootstrap Seed accepted by an external operator. The Seed governs creation, validation, and adoption of the first active framework version, cannot validate itself, and must remain immutable as provenance after that version is adopted.
