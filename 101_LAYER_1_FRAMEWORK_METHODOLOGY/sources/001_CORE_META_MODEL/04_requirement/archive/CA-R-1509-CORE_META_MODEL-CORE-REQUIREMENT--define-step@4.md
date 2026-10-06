---
subjects:
  governs: "Step"
  depends_on:
    - "Workflow"
    - "Action"
    - "Atom/Content Role: Operations/Type: Step"
    - "Step Run"
    - "Action/Execution Kind"
    - "Step/Agentic Execution Context"
    - "Tool"
version: 4
updated_at: "2026-09-21 00:57:42 +0000"
relations: {"relates_to": ["CA-R-1569"]}
---
# Define Step

a Step **means** a node **in** a Workflow, defined by **`=1`** Step Atom, that specifies invocation of **`=1`** Action with the parameters **and** inputs for that invocation.

- the binding identifies the source of **every** required input **or** parameter, including a Workflow input **or** an earlier Step result **when** applicable; it need **not** fix runtime values **in** the definition.
- different Steps **may** reference the same Action with different bindings **without** copying **or** redefining that Action.
- an Agentic invocation selects Integrated **or** Isolated context under CA-R-1527; a Programmatic invocation does **not** acquire an Agent context by this rule.
- the Step definition is distinct from its referenced Action **and** from a Step Run. internal Tool calls remain execution details under CA-R-1528, **not** additional Step definitions.
