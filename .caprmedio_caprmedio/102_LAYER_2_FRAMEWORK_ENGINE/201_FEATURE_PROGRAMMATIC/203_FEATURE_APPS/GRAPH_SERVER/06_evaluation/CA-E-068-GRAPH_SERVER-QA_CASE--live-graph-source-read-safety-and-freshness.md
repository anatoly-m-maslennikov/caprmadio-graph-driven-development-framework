---
subjects:
  governs: "evaluation"
  depends_on: []
version: 15
updated_at: "2026-10-05 00:12:28 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-R-1077
    - CA-M-154
  derived_from:
    - CA-A-057
atom_id: CA-E-068
content_role: Evaluation
status: Active
current_scope_unit: GRAPH_SERVER
claim_target_scope_unit: GRAPH_SERVER
local_tier: Standard
global_tier: 14
type: QA Case
---
# Summary

Live graph-source read safety and freshness

## Scope

GRAPH_SERVER contribution represented by this existing legacy Atom.

## Claim

## Claim checked

the headless graph service returns the actual current registered Projection **or** active Atom source **and** digest without `GRAPH_UI`, filesystem escape, inactive-source disclosure, intermediate authority, **or** mutation.

## Test case

1. Start `GRAPH_SERVER` with `GRAPH_UI` absent; request one registered Subject Projection, one registered lineage Projection, **and** one valid active Atom from a Tool **or** MCP client; require exact raw UTF-8 content, source kind, canonical repository-relative path, current status, **and** SHA-256 digest.
2. Reject an absolute external path, `..` traversal, a symlink escaping the project, an unregistered STG, a non-Markdown file, an unregistered Markdown file, an archived **or** **otherwise** inactive Atom, invalid UTF-8, **and** **every** non-read request.
3. Snapshot the requested Atom and persistent Projection inputs before and after valid and adversarial requests and require byte identity, unchanged paths, and no generated source-specific HTML. For configured logging Journals, require the accepted historical prefix to remain unchanged and permit only admitted append-only operational observations; read-only source access does not authorize editing or deleting Journal history.
4. Require disposable service state beneath the service-owned `.caprmedio_runtime` directory and technical and business log Journals in their configured local or remote sinks. Prove stopping or cleaning disposable state changes no Atom, STG, MRT, Project Work Journal, or accepted runtime Journal history; reject cleanup that would remove Journal records. Require persistent STGs under `.caprmedio_caprmedio/_projection/`, not Scope Unit authority folders.
5. Change a Projection **and** an active Atom after read-model generation, request them again, require the new source **and** digest, **and** require the client **to** distinguish stale Projection **and** changed-Atom states rather than presenting recorded digests as current.
6. Move an Atom into an inactive lifecycle state **and** require an explicit not-active result with no fallback **to** archived content.

## Acceptance criteria

**every** valid request returns the exact current registered STG **or** active Atom source **and** digest, **every** invalid **or** unsafe request fails closed, **and** no request can mutate **or** escape the governed read boundary.

## Failure disposition

Stop `GRAPH_SERVER`, reject the interaction as unsafe **or** stale, **and** record a high-priority Concern naming the first UI dependency, leaked path, unauthorized read, mutation, **or** incorrect digest.

## Sources

- [CA-R-1077 — Serve live graph sources read-only](../04_requirement/CA-R-1077-GRAPH_SERVER-REQUIREMENT--serve-live-graph-sources-read-only.md)
- [CA-M-154 — Serve live graph sources without mutation](../05_method/CA-M-154-GRAPH_SERVER-CORE-METHOD--serve-live-graph-sources-without-mutation.md)
