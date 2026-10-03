---
subject_scopes:
  - skill-boundary
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 3
updated_at: 2026-08-18 22:44:59
relations:
  child_of:
    - CAPRMEDIO-META-REQU-643--assign-one-authoritative-owner-to-each-governed-claim
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-520--own-deterministic-scripts-in-tools
---
# Keep CA and specialist skills thin

`/ca` and specialist Skills must contain only agent-facing instructions and thin routing or chaining declarations; they must reference Tools rather than embed or copy deterministic scripts and executable helpers.
