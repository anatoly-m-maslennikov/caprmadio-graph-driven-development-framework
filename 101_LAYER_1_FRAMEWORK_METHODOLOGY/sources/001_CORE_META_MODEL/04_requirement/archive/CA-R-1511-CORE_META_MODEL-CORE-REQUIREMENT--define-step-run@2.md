---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Step Run"
  depends_on:
    - "Step"
    - "Workflow Run"
    - "Action"
    - "Journal/Record"
    - "Step/Agentic Execution Context"
    - "Tool"
version: 2
updated_at: "2026-09-20 15:47:25 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Define Step Run

a Step Run **means** **`=1`** actual execution of **`=1`** Step within **`=1`** Workflow Run, invoking the Step's **`=1`** referenced Action with the bound parameters **and** inputs for that run.

- separate executions of the same Step are distinct Step Runs; they reuse the Step **and** Action definitions.
- an Agentic Step Run records its resolved invocation context under CA-R-1527. its internal Tool-call evidence is associated with this Run under CA-R-1528; a Tool call **or** repeated delivery of a pending invocation does **not** itself create another Step Run.
- the Step Run is distinct from its definition **and** from its Journal Records. a recorded attempt **or** failure **must not** be represented as successful completion.
