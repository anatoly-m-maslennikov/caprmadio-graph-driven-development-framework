---
subject_scopes:
  - "runtime"
tier: "core"
version: 6
updated_at: "2026-09-05 03:48:00 +0400"
llm_session_ids:
  - "codex:019f591f-04f6-70f2-8de7-828b7cccc69d"
relations:
  child_of:
    - "CA-M-261"
---
# Use one portable shared Skill runtime

All CAPRMEDIO Skills for one agent host invoke one versioned portable shared runtime that deterministically resolves the owning project, project-local governance, routing, and required session or Journal setup; thin wrappers duplicate no shared mechanics and fail closed when the runtime boundary cannot be resolved.
