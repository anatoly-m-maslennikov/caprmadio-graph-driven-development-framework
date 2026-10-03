---
subject_scopes:
  - artifact-operations
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 4
updated_at: 2026-08-23 15:59:05 +0400
---
# Read artifact metadata

The framework must provide one deterministic generic Artifact Tool that returns selected frontmatter fields and derived carrier identity for one artifact without loading its body, with explicit results for absent fields and parse errors.

This Tool owns form-agnostic metadata retrieval only. It does not define CAPRMEDIO Markdown Atom selector, lifecycle, identity, or output-view semantics; when used for an Atom, `ATOM_READ` owns the public Atom operation and may use this Tool only as a helper.
