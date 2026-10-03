---
subject_scopes:
  - provenance
tier: core
version: 3
updated_at: 2026-08-19 22:22:41
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-METH-030--generated-only-provenance-boundary
  resolution_of:
    - CAPRMEDIO-GOV-CONC-025--generated-refresh-self-reference
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---

# Exclude generated-only implementation edges

Commit-provenance validation inspects every commit in the governed range. A
commit contributes an implementation relation, implementation coverage, or
semantic traceability edge only when it changes at least one non-generated
governed path.

A generated-only commit is an auditable refresh transaction. It retains its
required provenance but cannot become an implementation input to the semantic
graph that produced the generated carrier. A mixed commit participates because
it includes a substantive governed change.
