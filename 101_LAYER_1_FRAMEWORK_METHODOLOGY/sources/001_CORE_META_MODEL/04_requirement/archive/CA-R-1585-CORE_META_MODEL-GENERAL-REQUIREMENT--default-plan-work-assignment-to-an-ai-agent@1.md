---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Assignee"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "AI Agent"
version: 1
updated_at: "2026-09-22 14:41:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1584"]}
---
# Default Plan work assignment to an AI Agent

**if** a Plan Atom has its own work **and** no explicit Assignee, **then** its effective Assignee **must** be **=1** AI Agent selected **to** execute that work.
