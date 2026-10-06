---
cce_version: cce_1
cce_form: obligation
subjects:
  - evaluation
version: 5
updated_at: 2026-08-23 12:02:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-R-1054
  resolution_of:
    - CAPRMEDIO-GOV-CONC-054--how-should-proof-currentness-be-represented
---
# Generate the proof currentness Catalog

CAPRMEDIO generates a non-authoritative proof-currentness Catalog from governed proof dependency frontiers encoded under GOV REQU 010 and their additional invalidation conditions. The Catalog reports each proof as `current`, `stale`, or `unknown`, marks only the smallest direct and transitive dependency closure affected by a change, never infers currentness from timestamps alone, and never mutates the historical proof record.
