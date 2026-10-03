---
subjects:
  governs:
    continuant:
      - artifact-migration
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 6
updated_at: 2026-08-30 16:44:07 +0400
---
# Apply an artifact migration

The framework must provide one deterministic generic Artifact Tool that applies one approved migration plan only when its recorded preconditions still match, commits all carrier and reference mutations as one rollbackable transaction, and appends the governed migration event through the Work Journal Tool.

This Tool owns generic migration-transaction mechanics only. `MIGRATE_ATOM_IDENTITY` and `REBIND_ATOM_RELATIONS` own their sealed CAPRMEDIO Markdown Atom migration and rebinding semantics, including their exact source, revision, relation, and MCP-gated effect boundaries; the generic Tool must not become a public alternative for those Atom changes.
