---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: check_of
    targets:
      - CAPRMEDIO-GOV-METH-030--generated-only-provenance-boundary
---

# Test Case — Enforce the generated-only provenance boundary

Create a temporary Git repository with a substantive commit, a generated-only
refresh commit, and a mixed commit. Give every commit valid provenance
trailers. The relation builder must retain the substantive and mixed commit
edges and omit the generated-only edge.

Run traceability, health, commit-provenance, lineage, and complete DSET gates.

This emitted Test atom is immutable. Later correction requires a successor Test
and append-only lifecycle event.

## Primary claim

A repository fixture proves that substantive and mixed commits form implementation relations while a generated-only refresh commit does not.
