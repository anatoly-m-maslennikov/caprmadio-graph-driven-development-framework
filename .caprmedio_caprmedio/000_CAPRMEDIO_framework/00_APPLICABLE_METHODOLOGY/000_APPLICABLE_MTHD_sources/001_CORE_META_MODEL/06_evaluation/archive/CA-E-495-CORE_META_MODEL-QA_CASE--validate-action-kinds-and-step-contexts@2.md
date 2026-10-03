---
subjects:
  governs: "Step/Agentic Execution Context"
  depends_on:
    - "Action/Execution Kind"
    - "Action"
    - "Step"
    - "Workflow"
    - "Step Run"
    - "Operator"
version: 2
updated_at: "2026-09-20 15:47:25 +0000"
relations: {"evaluation_for": ["CA-R-1526", "CA-R-1527", "CA-R-1509"]}
---
# Validate Action kinds and Step contexts

the Evaluation **must** check that Action Execution Kind **and** Agentic Step Execution Context remain distinct **and** support reuse **without** duplicate definitions.

- a Programmatic Action interacts with the Operator through code **without** AI judgment: accept Programmatic classification.
- code delegates the declared responsibility's judgment **to** an AI Agent: require Agentic classification rather than classifying by the surrounding code.
- two Steps invoke the same Agentic Action **in** Integrated **and** Isolated contexts with valid bindings: accept the shared Action identity **and** distinct invocation contexts.
- one Workflow mixes Programmatic, Integrated Agentic, **and** Isolated Agentic Steps: accept **without** a Workflow-wide context classification.
- missing **or** unavailable required context: block execution admission; do **not** silently select a substitute **or** classify a well-formed definition as malformed merely because a worker is unavailable.
- a Tool call appears inside an Agentic Step Run: retain **`=1`** declared Action for that Step rather than inferring another Step from the call.
- choosing Isolated grants additional permission, suppresses required Operator input, **or** permits concurrent mutations automatically: reject.

use definition fixtures **and** invocation evidence. these checks do **not** claim that an executor Implementation has been tested.
