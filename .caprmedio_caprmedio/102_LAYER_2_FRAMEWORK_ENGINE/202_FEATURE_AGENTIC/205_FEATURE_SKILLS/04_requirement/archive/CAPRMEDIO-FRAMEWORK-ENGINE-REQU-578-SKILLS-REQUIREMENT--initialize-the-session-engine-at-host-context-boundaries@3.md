---
atom_id: CAPRMEDIO-FRAMEWORK-ENGINE-REQU-578
subject_scopes:
  - session-engine
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 3
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CAPRMEDIO-METHODOLOGY-REQU-507-FRAMEWORK_METHODOLOGY-CORE-REQUIREMENT--automatically-initialize-the-session-engine
---
# Initialize the session engine at host context boundaries

Each supported agent-host adapter must initialize the CAPRMEDIO session engine at the host's session-start and post-compaction boundaries without requiring `/ca` invocation.
