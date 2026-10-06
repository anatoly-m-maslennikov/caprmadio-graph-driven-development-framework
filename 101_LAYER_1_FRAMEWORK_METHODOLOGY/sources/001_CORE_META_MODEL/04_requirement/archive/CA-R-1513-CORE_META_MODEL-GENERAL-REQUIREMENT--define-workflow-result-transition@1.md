---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Workflow/Relation Kind: On Result"
  depends_on:
    - "Workflow"
    - "Step"
    - "Step Run"
    - "Workflow Run"
    - "Relation Kind"
version: 1
updated_at: "2026-09-18 14:16:20 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Define Workflow result transition

ON_RESULT **means** the Workflow-scoped directed Relation from a source Step **to** a next Step, qualified by an explicit condition on the source Step Run's result.

- **every** endpoint refers **to** a Step **in** the same Workflow, **not** directly **to** an Action definition.
- a transition **may** be followed **only** **when** its condition **and** the Workflow's authorization **and** retry gates are satisfied.
- a terminal outcome ends the Workflow Run **without** inventing a Step **or** Action for that outcome. this Relation does **not** redefine Subject DEPENDS_ON **or** a Task prerequisite Relation.
