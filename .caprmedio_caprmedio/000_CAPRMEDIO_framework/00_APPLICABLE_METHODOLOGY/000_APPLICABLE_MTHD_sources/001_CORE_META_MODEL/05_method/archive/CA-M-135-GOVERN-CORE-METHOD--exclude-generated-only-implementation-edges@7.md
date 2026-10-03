---
cce_version: cce_1
cce_form: method
subjects:
  - provenance
version: 7
updated_at: 2026-08-23 12:02:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-R-1054
---
# Exclude generated-only implementation edges

Commit-provenance validation inspects every commit in the governed range. A commit contributes an implementation relation, implementation coverage, or semantic traceability edge only when it changes at least one non-generated governed path.

A generated-only commit is an auditable refresh transaction. It retains its required provenance but cannot become an implementation input to the semantic graph that produced the generated carrier. A mixed commit participates because it includes a substantive governed change.
