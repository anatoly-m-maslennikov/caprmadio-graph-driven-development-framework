---
atom_id: CAPRMEDIO-FRAMEWORK-ENGINE-REQU-565
subject_scopes:
  - skill-boundary
version: 3
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-564-SKILLS-CORE-REQUIREMENT--use-one-portable-shared-skill-runtime
    - CAPRMEDIO-METHODOLOGY-REQU-509-FRAMEWORK_METHODOLOGY-REQUIREMENT--govern-session-engine-rehydration-behavior
---
# Load durable authority only from CAPRMEDIO

CAPRMEDIO Skills must load durable project authority only from the owning project's governed `.caprmedio/` graph; host- or agent-specific memory, instruction, and context files, including `MEMORY.md`, `AGENTS.md`, and equivalents, may supply only ephemeral session context and operative planning.
