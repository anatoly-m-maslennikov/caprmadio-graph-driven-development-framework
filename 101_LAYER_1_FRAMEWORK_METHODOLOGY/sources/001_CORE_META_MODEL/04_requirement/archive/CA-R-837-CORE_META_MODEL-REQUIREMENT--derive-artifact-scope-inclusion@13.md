---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "scope-topology"
  depends_on: []
version: 13
updated_at: "2026-09-10 07:15:17 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Derive Artifact scope inclusion

For **every** Artifact contained **in** a Scope Unit, the resolver **must** derive its one direct Scope Unit from its canonical carrier address **and** include that Artifact **in** **every** Scope Unit on the direct Unit's complete ancestor path; missing, multiple, unknown, **or** cyclic scope ownership is invalid.

An Atom with no containing Scope Unit uses the separately governed Scope rule under CA-R-930; a failed Scope Unit resolution does **not** establish that no containing Scope Unit exists.
