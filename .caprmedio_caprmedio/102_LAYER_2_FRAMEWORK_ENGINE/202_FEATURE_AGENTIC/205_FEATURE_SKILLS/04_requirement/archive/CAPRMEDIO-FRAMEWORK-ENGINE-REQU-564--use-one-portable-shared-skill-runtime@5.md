---
subject_scopes:
  - runtime
tier: core
version: 5
updated_at: 2026-08-21 02:55:24
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-D-001-PRINCIPLE-DELIVERY--provide-replaceable-technical-realizations
---
# Use one portable shared Skill runtime

All CAPRMEDIO Skills for one agent host invoke one versioned portable shared runtime that deterministically resolves the owning project, project-local governance, routing, and required session or Journal setup; thin wrappers duplicate no shared mechanics and fail closed when the runtime boundary cannot be resolved.
