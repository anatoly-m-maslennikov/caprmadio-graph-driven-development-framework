---
atom_id: CA-D-275
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Plan/Type: Task/Assignee/Frontmatter"
  depends_on:
    continuant:
      - Actor
version: 5
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
---
# Serialize Explicit Task Assignee

a Markdown Task Atom Carrier **may** serialize one explicit Assignee override as top-level frontmatter property `assignee`, **and** omission **must** preserve the default Assignee.
