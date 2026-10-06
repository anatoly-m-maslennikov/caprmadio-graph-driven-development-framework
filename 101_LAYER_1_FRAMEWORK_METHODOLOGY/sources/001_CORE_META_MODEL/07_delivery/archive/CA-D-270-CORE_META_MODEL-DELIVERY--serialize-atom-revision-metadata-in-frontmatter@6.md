---
atom_id: CA-D-270
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Revision/Frontmatter"
  depends_on:
    - "Atom/Revision/Version"
    - "Atom/Revision/Updated At"
version: 6
updated_at: "2026-09-16 23:48:40 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize Atom Revision Metadata in Frontmatter

**every** Markdown Atom Revision Carrier **must** serialize its positive integer Version as `version` **and** its Project-time Updated At value as `updated_at` **in** YAML frontmatter.
