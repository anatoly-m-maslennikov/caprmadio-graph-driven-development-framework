---
atom_id: CA-D-274
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Plan/Type: Task/Author/Frontmatter"
  depends_on:
    continuant:
      - Actor
version: 4
updated_at: 2026-08-29 04:33:13 +0400
relations: {}
---
# Serialize Explicit Task Author

a Markdown Task Atom Carrier **may** serialize one explicit Author override as top-level frontmatter property `author`, **and** omission **must** preserve the default Author.
