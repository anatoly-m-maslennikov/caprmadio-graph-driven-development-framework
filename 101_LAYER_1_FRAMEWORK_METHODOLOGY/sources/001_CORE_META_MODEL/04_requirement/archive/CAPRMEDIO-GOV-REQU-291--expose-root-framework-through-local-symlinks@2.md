---
subject_scopes:
  - self-hosting
version: 2
updated_at: 2026-08-19 22:22:41
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Expose root framework through local symlinks

This CAPRMEDIO source project must expose its Git-tracked, non-hidden root files
and directories under `.caprmedio/000_caprmedio_framework` using relative
symlinks only. CAPRMEDIO project version, release, and changelog entries are
excluded because they describe this project rather than the reusable framework.
The directory contains no copied or independently maintained content; its
deterministic link set is a mechanical root view for recursive discovery and
operator convenience.
