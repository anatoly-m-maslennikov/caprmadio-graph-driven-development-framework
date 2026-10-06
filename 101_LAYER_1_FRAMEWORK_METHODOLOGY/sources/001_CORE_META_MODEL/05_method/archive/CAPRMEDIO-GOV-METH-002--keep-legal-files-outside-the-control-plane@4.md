---
subjects:
  - layout
tier: core
version: 4
updated_at: 2026-08-23 01:44:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---

# Keep legal files outside the control plane

The repository license remains the root `LICENSE` carrier. Retained third-party
licenses and no-license notices live in the root `LICENSES` directory.

These legal carriers are distribution inputs, not CAPRMEDIO methodology, applied
artifacts, settings, runtime state, or historical CAPRMEDIO data. They therefore do
not live inside `.caprmedio` and are not visible to skill discovery or semantic
compilation.

Source provenance stores each legal carrier's globally unique filename.
Provenance validation resolves that filename only within `LICENSES`; it does
not perform a repository-wide search or treat the legal file as CAPRMEDIO authority.
