---
subjects:
  governs: "Tool/ATOM_READ"
  depends_on:
    - "Atom"
    - "Artifact/Carrier"
    - "Scope Unit"
version: 10
updated_at: "2026-09-17 04:11:29 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
cce_version: cce_1
cce_form: obligation
---
# Read CAPRMEDIO Markdown Atoms

the `ATOM_READ` Tool is the canonical Finder for resolving one **or** many CAPRMEDIO Markdown Atoms from an exact repository-relative path, full filename, filename stem, **or** Atom ID. for **every** resolved Atom, it **must** return content **only**, metadata **only**, **or** both. Metadata **must** include the raw frontmatter **and** identity, placement, **and** lifecycle facts derived from the carrier filename **and** location. it **may** use generic metadata retrieval but owns Atom resolution **and** output-view semantics. Missing **or** ambiguous selectors **must** fail explicitly, **and** the Tool **must** never mutate governed project truth.

CA-O-047 defines the read-only Action; CA-E-302 owns the corresponding conformance checks.
