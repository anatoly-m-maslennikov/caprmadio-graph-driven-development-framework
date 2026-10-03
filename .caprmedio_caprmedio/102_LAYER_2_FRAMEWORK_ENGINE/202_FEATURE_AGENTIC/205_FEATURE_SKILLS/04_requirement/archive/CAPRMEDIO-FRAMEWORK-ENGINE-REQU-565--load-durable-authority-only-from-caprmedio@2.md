---
subject_scopes:
  - skill-boundary
version: 2
updated_at: 2026-08-18 22:44:59
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-564--use-one-portable-shared-skill-runtime
    - CAPRMEDIO-METHODOLOGY-REQU-509--govern-session-engine-rehydration-behavior
---
# Load durable authority only from CAPRMEDIO

CAPRMEDIO Skills must load durable project authority only from the owning project's governed `.caprmedio/` graph; host- or agent-specific memory, instruction, and context files, including `MEMORY.md`, `AGENTS.md`, and equivalents, may supply only ephemeral session context and operative planning.
