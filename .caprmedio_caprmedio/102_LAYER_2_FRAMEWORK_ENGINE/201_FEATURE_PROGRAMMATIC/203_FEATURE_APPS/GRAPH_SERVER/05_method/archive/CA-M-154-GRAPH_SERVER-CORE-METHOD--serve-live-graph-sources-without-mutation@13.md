---
subjects:
  governs: "artifact-query"
  depends_on: []
version: 13
updated_at: 2026-09-23 04:20:00 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  method_for:
    - CA-R-1077
  derived_from:
    - CA-A-057
---
# Serve live graph sources without mutation

Serve current graph inputs through this procedure:

1. Start the headless local service through the shared Tool environment without requiring `GRAPH_UI`, **and** keep logs **and** service state beneath its owned `.caprmedio_runtime` directory.
2. Accept **only** a canonical path supplied by the MRT source-lineage manifest **and** resolve it as either a registered `stg_requirements_subjects.md` **or** `stg_requirements_lineage_sections.md` **in** an active structural-unit root **or** a regular active Atom Markdown file below `.caprmedio`.
3. Reject absolute external paths, traversal, symlink escape, inactive lifecycle directories, unregistered STG files, unregistered Markdown, non-Markdown source content, write verbs, **and** **every** mutation request.
4. Read the current source bytes once **and** return the source kind, raw UTF-8 content, SHA-256 digest, canonical repository-relative path, **and** active **or** current status **without** removing frontmatter, rewriting STG content, **or** generating source-specific HTML.
5. Keep **every** request strictly read-only; stopping the service **or** deleting `.caprmedio_runtime` **must not** change an Atom, STG Projection, MRT Projection, **or** Journal.
6. Return explicit not-found, not-active, not-current, invalid-path, invalid-encoding, **and** digest-mismatch results so any Tool, MCP client, **or** optional UI can distinguish stale projections, changed Atoms, **and** unavailable sources.
