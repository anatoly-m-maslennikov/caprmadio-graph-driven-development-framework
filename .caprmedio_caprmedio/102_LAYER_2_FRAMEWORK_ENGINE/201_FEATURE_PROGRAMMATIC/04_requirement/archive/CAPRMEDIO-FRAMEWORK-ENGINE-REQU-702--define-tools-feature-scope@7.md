---
subject_scopes:
  - feature-boundary
version: 7
updated_at: 2026-08-23 15:33:04 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
---
# Define the TOOLS Feature scope

`TOOLS` with filename token `TOOLS` is one unordered Feature Scope Unit owned immediately by `PROGRAMMATIC` at Structural level `3`. It owns independently executable Tools classified by behavior as Hooks, Finders, or Doers, with Checkers governed as a Finder specialization rather than a separate Scope Unit. Hooks emit triggers into Tool flows and have no read, classification, or mutation authority beyond observing their registered boundary.
