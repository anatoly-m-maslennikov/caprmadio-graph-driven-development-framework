---
subject_scopes:
  - artifact-operations
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 4
updated_at: 2026-08-23 15:59:05 +0400
---
# Create an artifact carrier

The framework must provide one deterministic generic Artifact Tool that allocates a canonical artifact ID and filename and creates one carrier from its structural owner, Content role, title, required metadata, and body without silently overwriting an existing carrier.

This Tool owns generic carrier-construction mechanics only. `ATOM_CREATE` owns CAPRMEDIO Markdown Atom admission, filename, stable-identity, revision, bulk-preflight, and MCP-gated effect semantics; the generic Tool must not become a public alternative for creating such Atoms.
