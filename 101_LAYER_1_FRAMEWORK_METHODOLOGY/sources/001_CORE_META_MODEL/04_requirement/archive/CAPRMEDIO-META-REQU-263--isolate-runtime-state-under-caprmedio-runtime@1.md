---
subject_scope: framework-boundary
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-085--separate-active-authority-from-preserved-history
    - CAPRMEDIO-REQUIREMENT-META-109-all-governed-artifacts-live-under-caprmedio
---

# Requirement — Isolate runtime state under `.caprmedio_runtime`

Every CAPRMEDIO-owned runtime file lives under the current project's
`.caprmedio_runtime/` root whenever the host platform and invoked dependency
permit that location. Runtime files include process state, checkpoints, caches,
temporary materializations, recovery data, generated scratch, and other
reconstructible execution state.

When an operating system or external tool requires its native temporary or
cache location, CAPRMEDIO stores only the minimum transient adapter state there,
never treats it as governed authority, and cleans or reconciles it when the
owning operation ends. Runtime placement must not create files in ambient
repository directories.

The complete `.caprmedio_runtime/` tree remains non-authoritative: deleting it
may lose resumable progress or caches, but must not lose any governed artifact.

## Primary claim

CAPRMEDIO-owned reconstructible execution state is isolated under
`.caprmedio_runtime/` whenever technically possible.
