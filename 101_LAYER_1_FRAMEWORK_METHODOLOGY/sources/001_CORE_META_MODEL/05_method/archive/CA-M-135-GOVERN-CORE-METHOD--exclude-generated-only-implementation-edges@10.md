---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - provenance
version: 10
updated_at: 2026-08-29 02:40:41 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-R-1054
---
# Exclude generated-only implementation edges

Commit-provenance validation inspects **every** commit **in** the governed range. A commit contributes an implementation relation, implementation coverage, **or** semantic traceability edge **only** **when** it changes **`>=1`** non-generated governed path.

A generated-only commit is an auditable refresh transaction. It retains its required provenance but cannot become an implementation input to the semantic graph that produced the generated carrier. A mixed commit participates because it includes a substantive governed change.
