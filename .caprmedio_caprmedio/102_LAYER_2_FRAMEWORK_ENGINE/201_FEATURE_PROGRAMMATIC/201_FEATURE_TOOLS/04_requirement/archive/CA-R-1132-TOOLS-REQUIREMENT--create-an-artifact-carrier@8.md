---
subjects:
  governs: "artifact-operations"
  depends_on: []
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 8
updated_at: 2026-08-30 16:44:07 +0400
---
# Create an artifact carrier

The framework must provide one deterministic generic Artifact Tool that allocates a canonical artifact ID and filename and creates one carrier from its structural owner, Content role, title, required metadata, and body without silently overwriting an existing carrier.

This Tool owns generic carrier-construction mechanics only. `ATOM_CREATE` owns CAPRMEDIO Markdown Atom admission, filename, stable-identity, revision, bulk-preflight, and MCP-gated effect semantics; the generic Tool must not become a public alternative for creating such Atoms.
