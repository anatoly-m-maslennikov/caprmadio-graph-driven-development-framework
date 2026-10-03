---
subjects:
  governs: "feature-boundary"
  depends_on: []
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 8
updated_at: "2026-09-16 23:48:40 +0000"
---
# Use a common Tool CLI interface

Every Tool must expose the same machine-readable CLI contract for Tool kind, capability identity, help, input schema, result envelope, diagnostics, and exit status. Every Finder, including every Checker, must be strictly read-only with respect to governed Atoms and Journals; every Doer must support a dry-run mode that returns its resolved targets, complete planned effects, and validation results without mutation.
