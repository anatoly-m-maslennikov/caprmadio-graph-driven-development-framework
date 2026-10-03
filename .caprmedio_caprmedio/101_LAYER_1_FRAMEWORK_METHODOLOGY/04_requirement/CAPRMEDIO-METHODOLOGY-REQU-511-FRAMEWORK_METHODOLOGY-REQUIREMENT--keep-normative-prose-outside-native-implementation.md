---
subject_scopes:
  - implementation-boundary
version: 6
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CAPRMEDIO-METHODOLOGY-REQU-510-FRAMEWORK_METHODOLOGY-CORE-REQUIREMENT--keep-native-implementation-semantically-clean
---
# Keep normative prose outside native Implementation

prose embedded **in** source code, configuration, tests, **and** executable evaluations **must not** restate requirements, business rationale, intended outcomes, **or** future behavior; necessary comments **and** docstrings **may** explain **only** non-obvious current mechanics **and** operative interfaces.
