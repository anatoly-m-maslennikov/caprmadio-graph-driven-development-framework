---
atom_id: CA-D-275
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - Task/Assignee/Frontmatter
  depends_on:
    continuant:
      - Actor
version: 1
updated_at: 2026-08-28 23:15:00 +0400
relations: {}
---
# Serialize Explicit Task Assignee

a Markdown Task Atom Carrier **may** serialize one explicit Assignee override as top-level frontmatter property `assignee`, and omission **must** preserve the default Assignee.
