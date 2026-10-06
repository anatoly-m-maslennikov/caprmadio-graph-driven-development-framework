---
subject_scopes:
  - methodology
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-086--bounded-recursive-self-hosting
---
# Synchronize installed methodology only on command

CAPRMEDIO maintainers edit the reusable methodology only in its repository-root
source. An ordinary source edit never rewrites
`.caprmedio/000_caprmedio_framework/` and no workflow copies installed files back into
the root source.

An explicit operator synchronization command performs the one-way
root-to-installed refresh. Until that command runs, the installed methodology
remains the last accepted snapshot and may intentionally differ from the
working source.

## Rationale

Separating authoring from installation keeps ordinary edits bounded, preserves a reviewable installed snapshot, and prevents accidental bidirectional drift.
