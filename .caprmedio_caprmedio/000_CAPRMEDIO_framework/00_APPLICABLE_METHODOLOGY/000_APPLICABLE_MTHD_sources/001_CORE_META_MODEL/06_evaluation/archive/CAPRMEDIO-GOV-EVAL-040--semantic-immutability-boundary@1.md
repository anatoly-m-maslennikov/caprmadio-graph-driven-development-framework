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
      - CAPRMEDIO-GOV-REQU-416--identity-migration-preserves-atomic-content
      - CAPRMEDIO-GOV-REQU-417--semantic-immutability-boundary
---

# Test Case — Enforce the semantic immutability boundary

Accept a complete one-to-one migration that changes only canonical identity and
carrier-representation fields. Reject any migration that changes a claim,
rationale, authority, provenance fact, scope or applicability meaning,
creation priority, relation meaning or connected artifact, or QA condition,
criterion, threshold, or expected disposition.

Also prove that lifecycle state and effective priority change only through
append-only events or derived state, and that a semantic correction uses a new
successor atom rather than a migrated predecessor.

## Primary claim

Deterministic validation distinguishes permitted identity or carrier recoding from a forbidden atomic semantic mutation.
