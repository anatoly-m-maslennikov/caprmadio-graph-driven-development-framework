---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Content Role: Plan/Type: Task/Assignee/Frontmatter"
  depends_on:
    - "Actor"
version: 9
updated_at: "2026-09-10 02:49:14 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize Explicit Task Assignee

a Markdown Task Atom Carrier **may** serialize one explicit Assignee override as top-level frontmatter property `assignee`, **and** omission **must** preserve the default Assignee.
