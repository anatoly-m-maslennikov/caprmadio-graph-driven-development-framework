---
subjects:
  governs: "artifact-operations"
  depends_on: []
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 10
updated_at: "2026-09-16 23:48:40 +0000"
---
# Patch artifact relations

The framework must provide one deterministic generic Artifact Tool that adds, replaces, or removes explicitly selected typed relation targets and `relational_endpoints` descriptors by canonical project-graph node reference, including relative Scope Unit references that use exact full names and resolve from the source Artifact owner, while validating permitted relation kind, source and target classes, direction, lifecycle, cardinality, Content-role applicability, and endpoint identity without changing the Artifact body.

This Tool owns generic relation-patch mechanics only. It must not be exposed or applied as a substitute for a CAPRMEDIO Markdown Atom operation; `ATOM_UPDATE` owns declared Atom updates and `REBIND_ATOM_RELATIONS` owns its sealed Atom-rebinding case, including their target, revision, transaction, and MCP-gated effect semantics.
