---
atom_id: CA-D-377
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Framework Instance Settings/Carrier/Atom metadata exclusion"
  depends_on:
    - "Framework Instance Settings"
    - "Atom"
    - "Artifact/Revision"
version: 3
updated_at: "2026-09-09 23:04:14 +0400"
relations:
  child_of:
    - "CA-D-361"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Exclude Atom metadata from Framework Instance Settings

the Framework Instance Settings TOML Carrier **must not** contain Atom Frontmatter, Atom ID, Atom Revision metadata, Atom relations, rationale, **or** provenance; its Revision binding follows CA-D-360.
