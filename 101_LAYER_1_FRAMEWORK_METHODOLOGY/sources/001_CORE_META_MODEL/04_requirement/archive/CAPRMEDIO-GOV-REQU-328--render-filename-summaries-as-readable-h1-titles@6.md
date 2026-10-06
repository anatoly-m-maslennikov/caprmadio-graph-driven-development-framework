---
subject_scopes:
  - carrier-format
version: 6
updated_at: 2026-08-21 04:43:43
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-122
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Render filename summaries as readable H1 titles

Every role-classified Markdown Atom must begin its body with exactly one H1 that repeats only
the current filename Summary in human-readable form. The H1 uses spaces
instead of filename hyphens and may apply normal capitalization and punctuation
without changing, narrowing, extending, or interpreting the summary's meaning.

The H1 must not repeat the Artifact Type, identity, scope, lifecycle
position, or other carrier-derived fact. It is a derived navigation label, not
an independent semantic claim or source of authority. A governed Summary rename
updates the filename and H1 together without changing the assigned Atom-ID segment.
