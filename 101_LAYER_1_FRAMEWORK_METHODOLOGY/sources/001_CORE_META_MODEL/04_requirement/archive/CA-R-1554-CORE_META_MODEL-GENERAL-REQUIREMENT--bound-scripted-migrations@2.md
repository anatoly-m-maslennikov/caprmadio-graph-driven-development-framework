---
subjects:
  governs: "AI Agent/authorization"
  depends_on:
    - "Step"
    - "AI Agent"
    - "Scripted Migration"
    - "Target Set"
version: 2
updated_at: "2026-09-21 00:39:50 +0000"
relations: {}
---
# Bound Scripted Migrations

an AI Agent that performs a Scripted Migration **must** satisfy **all** of these participation conditions:

- bind the migration **to** an exact governed Target Set;
- fail **when** an expected target is absent;
- produce a reviewable change set.

these conditions constrain the AI Agent's participation; they do **not** define the migration's Steps **or** Workflow control flow **or** grant additional mutation authority.
