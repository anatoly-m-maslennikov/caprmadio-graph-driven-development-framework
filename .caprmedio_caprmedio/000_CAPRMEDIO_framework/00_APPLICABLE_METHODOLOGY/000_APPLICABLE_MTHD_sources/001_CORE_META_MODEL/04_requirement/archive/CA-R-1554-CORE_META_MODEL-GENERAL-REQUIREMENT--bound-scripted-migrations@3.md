---
subjects:
  governs: "AI Agent/authorization"
  depends_on:
    - "Step"
    - "AI Agent"
    - "Scripted Migration"
    - "Target Set"
version: 3
updated_at: "2026-09-21 00:39:50 +0000"
relations: {}
atom_id: "CA-R-1554"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Bound Scripted Migrations

an AI Agent that performs a Scripted Migration **must** satisfy **all** of these participation conditions:

- bind the migration **to** an exact governed Target Set;
- fail **when** an expected target is absent;
- produce a reviewable change set.

these conditions constrain the AI Agent's participation; they do **not** define the migration's Steps **or** Workflow control flow **or** grant additional mutation authority.
