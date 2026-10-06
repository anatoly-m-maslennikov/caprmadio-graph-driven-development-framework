---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Workflow"
  depends_on:
    - "Step"
    - "Action"
    - "Workflow Run"
    - "Workflow/Relation Kind: On Result"
    - "Step/Agentic Execution Context"
version: 2
updated_at: "2026-09-20 15:47:25 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Define Workflow

a Workflow **means** one reusable graph whose nodes are Steps **and** whose edges are typed, directed Relations owned by the Workflow graph kind.

- **every** Step references its Action **and** binds its parameters **and** inputs under CA-R-1509; the graph reuses Action definitions **without** copying them.
- the typed Relations define admitted control flow, including conditional branches **and** revisits. result-dependent next-Step edges use CA-R-1513.
- the graph preserves its accepted success, retry-budget, **and** escalation conditions; it does **not** itself authorize concurrent execution, arbitrary recursion, **or** unlimited retries.
- invocation context is selected per Agentic Step under CA-R-1527; a mixed graph needs no separate Integrated **or** Isolated Workflow identity.
- the reusable graph is distinct from a Workflow Run. doer, finder, checker/test, **and** quality-gate evaluation remain examples of Action responsibilities, **not** a closed Action taxonomy.
