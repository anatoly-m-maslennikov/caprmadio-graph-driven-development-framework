---
subject_scopes:
  - feature-boundary
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 5
updated_at: 2026-08-23 15:33:04 +0400
---
# Use a common Tool CLI interface

Every Tool must expose the same machine-readable CLI contract for Tool kind, capability identity, help, input schema, result envelope, diagnostics, and exit status. Every Finder, including every Checker, must be strictly read-only with respect to governed Atoms and Journals; every Doer must support a dry-run mode that returns its resolved targets, complete planned effects, and validation results without mutation.
