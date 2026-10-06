---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Assignee/Carrier"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Plan/Type: Plan/Assignee"
    - "File Carrier"
version: 1
updated_at: "2026-09-22 14:41:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1584", "CA-R-1585"]}
---
# Serialize explicit Plan Assignees

a Plan File Carrier **may** serialize **=1** explicit Assignee override as top-level frontmatter `assignee`; omission **must** preserve CA-R-1585 for its own work rather than copying the default.
