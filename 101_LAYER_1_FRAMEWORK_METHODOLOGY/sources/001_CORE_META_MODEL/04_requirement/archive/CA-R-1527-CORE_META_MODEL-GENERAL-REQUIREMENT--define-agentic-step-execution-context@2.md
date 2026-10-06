---
subjects:
  governs: "Step/Agentic Execution Context"
  depends_on:
    - "Step"
    - "Action/Execution Kind"
    - "Workflow"
    - "Step Run"
    - "AI Agent"
    - "Operator"
version: 2
updated_at: "2026-09-20 15:47:25 +0000"
relations: {"relates_to": ["CA-R-1509", "CA-R-1526", "CA-R-1525"]}
---
# Define agentic Step execution context

Agentic Step Execution Context **means** the context selected by a Step's invocation binding for its Agentic Action: Integrated **or** Isolated.

- Integrated: the current participating session receives the Action's bound inputs **and** instructions, performs the Action, **and** returns its result **to** the executor.
- Isolated: a separate AI Agent context receives the Action's bound inputs **and** instructions, performs the Action, **and** returns its result **to** the executor.
- an Agentic Step invocation resolves **`=1`** admitted context through its declared binding **before** dispatch. the binding **may** use an explicitly supplied runtime parameter; a missing **or** unsupported context blocks admission rather than causing silent substitution.
- the same Action definition **may** be reused **in** either context **when** its required capabilities are available. do **not** duplicate an Action merely **to** select another context.
- a Workflow **may** mix Programmatic Steps, Integrated Agentic Steps, **and** Isolated Agentic Steps. the context belongs **to** the invocation, **not** **to** a second Workflow classification **or** the Action's identity; it does **not** apply **to** a Programmatic Action as an Agent context.
- the actual Step Run retains its selected context. Isolated does **not** mean unrestricted, fully autonomous, concurrent, **or** unable **to** request Operator input. Integrated does **not** grant the session additional authority.
