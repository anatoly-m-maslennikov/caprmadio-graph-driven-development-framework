---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Workflow Run"
  depends_on:
    - "Workflow"
    - "Step Run"
    - "Action"
    - "Action/Execution Kind"
    - "Step/Agentic Execution Context"
    - "Tool"
    - "Applicable Methodology"
    - "Operator"
    - "Atom/Content Role: Implementation"
version: 3
updated_at: "2026-09-23 04:20:00 +0400"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1187", "CA-R-1178", "CA-R-1426", "CA-R-1519", "CA-R-1520", "CA-R-1516", "CA-R-1526", "CA-R-1527", "CA-R-1528", "CA-R-1529"]}
---
# Provide Workflow orchestration from methodology

WORKFLOW_ORCHESTRATOR **must** be the APPS Scope Unit that provides a conforming executor of the applicable methodology Workflow model under CA-R-1519 **and** CA-R-1520.

- the application owns coordination of an accepted request across its Workflow Runs; Tools remain realizations of individual methodology Actions under CA-R-1516.
- support Programmatic Actions **and** interactive Agentic Steps under CA-R-1526 **and** CA-R-1527. for an Agentic Step, return the applicable `ACTION_PROMPT` plus its invocation envelope through MCP; the main session selects in-session execution **or** an isolated subagent, then submits the decision **and** result through the next MCP call. only that result permits transition **to** the next Step. retain coordination state rather than requiring the session **to** remember the procedure. Tool-call evidence follows CA-R-1528.
- applicable Workflow definitions, input bindings, result conditions, **and** continuation rules determine execution. the application **must not** maintain a second independently authored Update-to-Replace rule **or** another Workflow-specific policy.
- the application's RMED specifies its execution behavior; Workflow definitions are governed inputs, **not** a requirement **to** use those Workflows **to** build the application.
- the application implements the methodology conformance requirements. its existence is **not** a backward Demand from FRAMEWORK_METHODOLOGY **to** FRAMEWORK_ENGINE.

The application is one immediate unordered APPS Scope Unit. Its declaration does not install a service **or** replace an existing specialized execution component.
