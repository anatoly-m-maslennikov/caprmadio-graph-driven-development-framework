---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Markdown Atom Carrier/YAML Frontmatter/Scalar"
  depends_on:
    - "Markdown Atom Carrier/Main Content"
version: 9
updated_at: "2026-09-10 02:49:14 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize Safe Frontmatter Scalars

the YAML Frontmatter of a Markdown Atom Carrier **must** serialize registered YAML-safe controlled string values as plain scalars **and** **must** place uncontrolled human prose **in** Main Content.
