---
subject_scopes:
  - self-hosting
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-086--bounded-recursive-self-hosting
    - CAPRMEDIO-GOV-REQU-292--explicit-methodology-synchronization
---

# Keep local methodology installation empty

This CAPRMEDIO source project must keep `.caprmedio/methodology` unmaterialized:
the path may be absent or empty, but it must contain no files or directories.
Only an explicit operator request may populate or synchronize it; ordinary
development, resolution, validation, and self-hosting must use the framework
source in the repository root without creating a mirror.
