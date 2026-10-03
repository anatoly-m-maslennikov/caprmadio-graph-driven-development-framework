---
subject_scopes:
  - "runtime"
version: 8
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - "CA-M-261"
---
# Use one portable shared Skill runtime

All CAPRMEDIO Skills for one agent host invoke one versioned portable shared runtime that deterministically resolves the owning project, project-local governance, routing, and required session or Journal setup; thin wrappers duplicate no shared mechanics and fail closed when the runtime boundary cannot be resolved.
