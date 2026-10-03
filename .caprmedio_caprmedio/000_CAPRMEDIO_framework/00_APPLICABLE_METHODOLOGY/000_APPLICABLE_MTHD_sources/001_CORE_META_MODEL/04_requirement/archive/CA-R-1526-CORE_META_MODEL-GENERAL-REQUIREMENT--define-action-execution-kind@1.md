---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Action/Execution Kind"
  depends_on:
    - "Action"
    - "AI Agent"
    - "Tool"
    - "Operator"
version: 1
updated_at: "2026-09-20 15:47:25 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1452"]}
---
# Define Action Execution Kind

Action Execution Kind **means** the distinction between execution by code **and** execution requiring AI Agent judgment for an Action's declared responsibility.

- Programmatic: code performs the Action according **to** its specified behavior, **without** delegating interpretation **or** judgment **to** an AI Agent. programmatic interaction with the Operator does **not** by itself make the Action Agentic.
- Agentic: an AI Agent interprets the supplied context **and** instructions **to** perform the Action. the AI Agent **may** call Tools within its admitted authority.
- classify an invocation by the responsibility actually delegated, **not** by whether its transport **or** surrounding executor is implemented **in** code. code that delegates the Action's judgment **to** an AI Agent does **not** make that Action Programmatic.
- the distinction does **not** select the Agent's execution context, grant permissions, **or** change the Action's semantic boundary. Tool calls **do not** by themselves create additional Actions **or** Workflow Steps.
