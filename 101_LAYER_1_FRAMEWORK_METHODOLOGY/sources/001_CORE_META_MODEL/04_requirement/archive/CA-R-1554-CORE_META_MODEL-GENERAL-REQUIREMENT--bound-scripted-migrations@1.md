---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "AI Agent/authorization"
  depends_on:
    - "Step"
    - "AI Agent"
    - "Scripted Migration"
    - "Target Set"
version: 1
updated_at: "2026-09-21 00:39:50 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Bound Scripted Migrations

an AI Agent that performs a Scripted Migration **must** satisfy **all** of these participation conditions:

- bind the migration **to** an exact governed Target Set;
- fail **when** an expected target is absent;
- produce a reviewable change set.

these conditions constrain the AI Agent's participation; they do **not** define the migration's Steps **or** Workflow control flow **or** grant additional mutation authority.
