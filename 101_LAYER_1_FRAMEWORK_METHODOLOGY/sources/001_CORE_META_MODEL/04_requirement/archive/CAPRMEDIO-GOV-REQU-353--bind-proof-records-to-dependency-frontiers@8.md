---
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - provenance
version: 8
updated_at: 2026-08-29 02:40:41 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-R-1054
  resolution_of:
    - CAPRMEDIO-GOV-CONC-054--how-should-proof-currentness-be-represented
---
# Bind proof records to dependency frontiers

CAPRMEDIO binds **every** governed proof record to a machine-readable frontier of the exact Artifact **and** Implementation revisions, configurations, evaluators, environments, **and** material inputs under which its observation was produced. GOV REQU 010 defines the required `proof_frontier_refs` representation; prose is reserved for additional invalidation conditions that cannot be encoded **without** loss.
