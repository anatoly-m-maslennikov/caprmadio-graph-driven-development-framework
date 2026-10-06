---
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Plan/Plan Type: Task/Assignee"
  depends_on:
    continuant:
      - AI Agent
atom_id: CA-R-1081
cce_version: cce_1
cce_form: conditional
version: 3
updated_at: 2026-08-28 22:31:24 +0400
relations:
  child_of:
    - CA-R-1079
---
# Default Task Assignee to an AI Agent

**if** a Task Atom has no explicit Assignee, **then** its effective Assignee **must** be one AI Agent selected to execute that Task.
