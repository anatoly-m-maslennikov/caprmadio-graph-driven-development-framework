---
subjects:
  governs: "artifact-query"
  depends_on: []
version: 14
updated_at: "2026-10-05 00:11:50 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  method_for:
    - CA-R-1077
  derived_from:
    - CA-A-057
atom_id: CA-M-154
content_role: Method
status: Active
current_scope_unit: GRAPH_SERVER
claim_target_scope_unit: GRAPH_SERVER
local_tier: Core
global_tier: 12
---
# Summary

Serve live graph sources without mutation

## Scope

GRAPH_SERVER contribution represented by this existing legacy Atom.

## Claim

Serve current graph inputs through this procedure:

1. Start the headless local service through the shared Tool environment without requiring `GRAPH_UI`, **and** keep disposable service state beneath its owned `.caprmedio_runtime` directory, and deliver technical and business runtime Journal records to their explicitly configured governed sinks.
2. Accept **only** a canonical path supplied by the MRT source-lineage manifest **and** resolve it as either a registered `stg_requirements_subjects.md` **or** `stg_requirements_lineage_sections.md` at a registered persistent Projection destination beneath `.caprmedio_caprmedio/_projection/` **or** a regular active authoritative Atom Markdown file below the configured Project control root, excluding Projection copies.
3. Reject absolute external paths, traversal, symlink escape, inactive lifecycle directories, unregistered STG files, unregistered Markdown, non-Markdown source content, write verbs, **and** **every** mutation request.
4. Read the current source bytes once **and** return the source kind, raw UTF-8 content, SHA-256 digest, canonical repository-relative path, **and** active **or** current status **without** removing frontmatter, rewriting STG content, **or** generating source-specific HTML.
5. Keep every source-read request strictly read-only with respect to its requested Atom and Projection inputs; configured technical or business logging may only append admitted observations to its own Journal, without changing accepted history; stopping the service or cleaning disposable runtime state **must not** change an Atom, STG Projection, MRT Projection, or accepted Journal history. Preserve runtime Journal records in configured local or remote sinks; this procedure does not authorize deletion of a runtime directory containing Journal history.
6. Return explicit not-found, not-active, not-current, invalid-path, invalid-encoding, **and** digest-mismatch results so any Tool, MCP client, **or** optional UI can distinguish stale projections, changed Atoms, **and** unavailable sources.
