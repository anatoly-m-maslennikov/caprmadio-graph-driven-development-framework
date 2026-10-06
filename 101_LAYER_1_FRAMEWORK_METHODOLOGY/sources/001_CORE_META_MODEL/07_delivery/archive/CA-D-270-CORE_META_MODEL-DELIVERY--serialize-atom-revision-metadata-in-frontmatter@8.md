---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Revision/Frontmatter"
  depends_on:
    - "Atom/Revision/Version"
    - "Atom/Revision/Updated At"
version: 8
updated_at: "2026-09-10 02:49:14 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize Atom Revision Metadata in Frontmatter

**every** Markdown Atom Revision Carrier **must** serialize its positive integer Version as `version` **and** its Project-time Updated At value as `updated_at` **in** YAML frontmatter.
