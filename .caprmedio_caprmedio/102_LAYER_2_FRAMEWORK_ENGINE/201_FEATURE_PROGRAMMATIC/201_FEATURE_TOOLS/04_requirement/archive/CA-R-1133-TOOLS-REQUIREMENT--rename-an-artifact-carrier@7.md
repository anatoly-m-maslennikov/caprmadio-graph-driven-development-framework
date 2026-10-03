---
subjects:
  governs: "artifact-operations"
  depends_on: []
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 7
updated_at: "2026-09-16 23:48:40 +0000"
---
# Rename an artifact carrier

The framework must provide one deterministic generic Artifact Tool that renames one artifact carrier under the active filename grammar, rejects collisions, rewrites governed canonical references, records the identity mapping, and rolls back the complete rename when any required rewrite fails.

This Tool owns generic rename mechanics only. `ATOM_MOVE` owns CAPRMEDIO Markdown Atom relocation, identity preservation, destination validation, bulk transaction, and MCP-gated effect semantics; the generic Tool must not become a public alternative for moving such Atoms.
