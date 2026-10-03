---
subjects:
  governs: "artifact-operations"
  depends_on:
    - "Artifact"
    - "Artifact/Carrier"
    - "Atom/Content Role"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 11
updated_at: "2026-09-17 19:56:34 +0000"
---
# Create an artifact carrier

the framework **must** provide one deterministic generic Artifact Tool that allocates the canonical identity **and** filename required by the admitted Artifact Carrier schema **and** creates one Carrier from its structural owner **and** the inputs required by that schema, **without** silently overwriting an existing Carrier.

this Tool owns generic carrier-construction mechanics **only**. `ATOM_CREATE` owns CAPRMEDIO Markdown Atom admission, filename, stable-identity, revision, bulk-preflight, **and** MCP-gated effect semantics; the generic Tool **must not** become a public alternative for creating such Atoms.
