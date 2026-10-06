---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Atom/Content Role: Plan/Type: Task/Executable Leaf"
  depends_on:
    - "Atom/Content Role: Plan/Type: Task"
    - "Atom/Content Role: Plan/Type: Task/Definition of Done"
    - "Atom/Content Role: Plan/Direct Work Decomposition"
    - "AI Agent"
version: 1
updated_at: "2026-09-20 23:55:10 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-989", "CA-R-1212", "CA-R-1536"]}
---
# Bound Executable Leaf Tasks

**every** Task Atom with no direct subordinate Task **must** define work estimated at **`<=15`** minutes for one assigned AI Agent, provide sufficient inputs, required output, **and** verification, **and** contain no unresolved Operator decision; a containing composite Task **may** have a larger roll-up estimate.
