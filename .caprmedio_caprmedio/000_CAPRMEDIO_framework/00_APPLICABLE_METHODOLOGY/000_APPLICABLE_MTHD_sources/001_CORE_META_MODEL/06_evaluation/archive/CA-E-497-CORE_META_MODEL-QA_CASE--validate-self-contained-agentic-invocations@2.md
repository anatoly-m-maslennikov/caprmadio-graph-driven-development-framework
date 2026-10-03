---
subjects:
  governs: "Step Run/Invocation"
  depends_on:
    - "Step Run"
    - "Workflow Run"
    - "Step"
    - "Action"
    - "Operator"
    - "Artifact/Revision"
version: 2
updated_at: "2026-09-20 15:47:25 +0000"
relations: {"evaluation_for": ["CA-R-1529", "CA-M-304"]}
---
# Validate self-contained agentic invocations

the Evaluation **must** check that an Agentic Step invocation can be understood **and** resumed from its supplied context **without** remembered Workflow procedure.

- remove earlier conversation from an Integrated session: the supplied invocation still identifies the requested Action, inputs, evidence, actual effects, authority boundaries, expected result, **and** return route.
- supply the invocation **to** an Isolated context: require the same admitted responsibility **and** constraints rather than implicit access **to** the parent conversation.
- omit required context **or** make a referenced input inaccessible: require a visible missing-input result, **not** guessed execution.
- deliver the same pending invocation again: preserve its identity **and** actual effects; repeated delivery **must not** imply a new Run **or** authorization **to** replay effects.
- provide a prompt that contradicts its bound definition **or** expands permission: reject the instruction even **if** it is self-contained.
- a Step result returns **or** a Workflow hands off: the executor owns the declared routing; a returned prompt alone is **not** Step completion **or** successor completion.

check exact supplied evidence, **not** a claim that the session will remember how **to** proceed.
