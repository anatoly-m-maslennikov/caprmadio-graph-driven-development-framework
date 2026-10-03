---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 6
updated_at: 2026-08-23 17:40:00 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-1077
    - CA-M-154
  derived_from:
    - CA-A-057
---
# Live graph-source read safety and freshness

## Claim checked

The local graph service returns the actual current registered STG or active Atom source and digest without permitting filesystem escape, inactive-source disclosure, intermediate authority, or mutation.

## Applicable conditions

1. Serve `.caprmedio/mrt_atoms.html`, request one registered Subject STG, one registered lineage-section STG, and one valid active Atom from its lineage manifest, and require exact raw UTF-8 content, source kind, canonical repository-relative path, current status, and SHA-256 digest.
2. Reject an absolute external path, `..` traversal, a symlink escaping the project, an unregistered STG, a non-Markdown file, an unregistered Markdown file, an archived or otherwise inactive Atom, invalid UTF-8, and every non-read request.
3. Snapshot every governed file before and after valid and adversarial requests and require byte identity, unchanged paths, and no generated source-specific HTML.
4. Require service state and logs only beneath the service-owned `.caprmedio_runtime` directory and prove deleting that directory changes no Atom, STG, MRT, or Journal.
5. Change an STG and an active Atom after MRT generation, request them again, require the new source and digest, and require the browser to distinguish stale STG, stale MRT, and changed-Atom states rather than presenting recorded digests as current.
6. Move an Atom into an inactive lifecycle state and require an explicit not-active result with no fallback to archived content.

## Acceptance criteria

Every valid request returns the exact current registered STG or active Atom source and digest, every invalid or unsafe request fails closed, and no request can mutate or escape the governed read boundary.

## Failure disposition

Stop the graph service, reject the MRT interaction as unsafe or stale, and record a high-priority Concern naming the first leaked path, unauthorized read, mutation, or incorrect digest.
