---
subject_scopes:
  - framework-boundary
version: 2
updated_at: 2026-08-21 20:51:16
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-014--support-repository-relative-work-areas
---

# Contract — Repository Work Area declaration

## Primary claim

An adopting repository owner declares either repository-level scope or one or
more existing repository-relative folders as Work Areas. The declaration may
cover local, deployable, library, documentation, methodology, data, or mixed
content without requiring code or deployability.

Every scope-dependent CAPRMEDIO consumer resolves the current accepted
declaration before work. Session continuity may retain a bounded reference but
cannot create, rename, reclassify, replace, or supersede the boundary.

## Conformance

Every scope-dependent consumer resolves either repository-level scope or the
applicable declared Work Areas. Absolute paths, paths outside the repository,
missing folders, and stale declarations do not conform.

## Compatibility

Content changes inside a Work Area do not change the boundary. A path rename,
removal, scope split, or scope merge requires an explicit reviewed successor
Contract and refresh of affected references and evidence. A simple repository
may remain one repository-level scope.
