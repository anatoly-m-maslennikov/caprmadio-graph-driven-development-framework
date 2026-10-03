---
subject_scopes:
  - skill-boundary
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 6
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CAPRMEDIO-META-REQU-643--assign-one-authoritative-owner-to-each-governed-claim
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-520--own-deterministic-scripts-in-tools
---
# Keep CA and specialist skills thin

`/ca` **and** specialist Skills **must** contain **only** agent-facing instructions **and** thin routing **or** chaining declarations; they **must** reference Tools rather than embed **or** copy deterministic scripts **and** executable helpers.
