---
subjects:
  governs: "Atom/Content Role: Plan/Type: Task/Assignee"
  depends_on:
    - "AI Agent"
atom_id: CA-R-1081
cce_version: cce_1
cce_form: conditional
version: 8
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  child_of:
    - CA-R-1079
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Default Task Assignee to an AI Agent

**if** a Task Atom has no explicit Assignee, **then** its effective Assignee **must** be one AI Agent selected to execute that Task.
