---
subjects:
  governs: "Step Run/Invocation"
  depends_on:
    - "Step Run"
    - "Workflow Run"
    - "Step"
    - "Action"
    - "Action/Execution Kind"
    - "Step/Agentic Execution Context"
    - "Artifact/Revision"
    - "Operator"
    - "Journal"
version: 2
updated_at: "2026-09-20 15:47:25 +0000"
relations: {"relates_to": ["CA-R-1527", "CA-R-1519", "CA-R-1520", "CA-R-1525"]}
---
# Provide self-contained agentic Step invocations

an executor dispatching **or** resuming an Agentic Step **must** provide a self-contained invocation sufficient for the receiving context **to** perform the admitted Action **without** remembering the Workflow procedure from earlier conversation.

- identify the Workflow Run **and** Step Run, exact admitted definition bindings, bound inputs **or** accessible references, relevant prior results **and** actual effects, applicable permissions, **and** required output.
- provide the instruction derived from the Action **and** its Step binding, including how **to** return the result **or** request missing input. the instruction is a derived presentation of governing authority, **not** another independently maintained procedure.
- the executor retains execution state **and** selects subsequent Steps from the Workflow's declared transitions. the participating session **or** separate Agent context performs the requested Action; it need **not** reconstruct **or** remember what the Workflow will do next.
- an Integrated invocation returns this context **and** instruction through the session interface; an Isolated invocation supplies it **to** the separate context. no particular transport is required by this core rule.
- requesting participation **or** returning a prompt does **not** itself complete a Step Run. repeated delivery **or** reconnection **must not** imply permission **to** repeat already performed effects; report actual results against the identified invocation.
- a terminal Workflow handoff still follows CA-R-1520: end the predecessor Run **and** let the executor admit a separate successor. a session instruction **must not** silently resume an ended Run **or** bypass approval.
