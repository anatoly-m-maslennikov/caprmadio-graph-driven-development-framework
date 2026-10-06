---
subject_scope: artifact-model
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-196--three-axis-artifact-routing
---

# Requirement — Explicit three-axis route

Routing values are declared metadata. Authority, provenance, priority,
lifecycle state, applicability, and scope path remain independent.

## Primary claim

Every governed artifact explicitly declares one revision_mode, one content_role, and one governance_locus; other metadata remains outside this route.

## Rationale

Independent explicit axes prevent filenames, folders, workflow position, authority, or lifecycle from silently reclassifying an artifact.
