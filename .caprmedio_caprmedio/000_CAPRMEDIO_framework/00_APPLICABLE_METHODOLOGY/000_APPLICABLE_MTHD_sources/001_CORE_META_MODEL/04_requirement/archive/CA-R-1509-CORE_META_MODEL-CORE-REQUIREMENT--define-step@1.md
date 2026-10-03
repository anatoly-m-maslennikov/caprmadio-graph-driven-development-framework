---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Step"
  depends_on:
    - "Workflow"
    - "Action"
    - "Step Run"
version: 1
updated_at: "2026-09-18 14:16:20 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Define Step

a Step **means** a node **in** a Workflow that specifies invocation of **`=1`** Action with the parameters **and** inputs for that invocation.

- the binding identifies the source of **every** required input **or** parameter, including a Workflow input **or** an earlier Step result **when** applicable; it need **not** fix runtime values **in** the definition.
- different Steps **may** reference the same Action with different bindings **without** copying **or** redefining that Action.
- the Step definition is distinct from its referenced Action **and** from a Step Run.
