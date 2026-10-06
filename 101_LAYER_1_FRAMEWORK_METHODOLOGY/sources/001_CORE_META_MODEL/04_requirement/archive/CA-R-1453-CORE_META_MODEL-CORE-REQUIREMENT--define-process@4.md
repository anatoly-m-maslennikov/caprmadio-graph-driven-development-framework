---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Process"
  depends_on:
    - "Action"
    - "Actor"
    - "Journal/Record"
version: 4
updated_at: "2026-09-13 01:25:33 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Define Process

a Process **means** one reusable flow graph whose nodes reference Actions **and** whose explicit control flow governs their order **and**, under explicit accepted conditions, selection **or** revisiting of nodes. the node references reuse Action definitions **without** copying **or** redefining them for **every** Process; the Process definition is distinct from a particular execution **and** its Journal Records. doer, finder, checker/test, **and** quality-gate evaluation illustrate Action responsibilities, **not** a closed taxonomy of Actions **or** Actors. the control flow preserves applicable accepted success, retry-budget, **and** escalation conditions; the Process definition does **not** itself authorize concurrent execution, arbitrary recursion, **or** unlimited retries.
