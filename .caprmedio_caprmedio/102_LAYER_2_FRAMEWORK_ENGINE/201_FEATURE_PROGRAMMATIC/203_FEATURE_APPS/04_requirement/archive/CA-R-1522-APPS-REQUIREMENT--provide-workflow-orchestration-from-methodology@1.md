---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Workflow Run"
  depends_on:
    - "Workflow"
    - "Step Run"
    - "Action"
    - "Tool"
    - "Applicable Methodology"
    - "Operator"
    - "Atom/Content Role: Implementation"
version: 1
updated_at: "2026-09-18 21:23:47 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1187", "CA-R-1178", "CA-R-1426", "CA-R-1519", "CA-R-1520", "CA-R-1516"]}
---
# Provide Workflow orchestration from methodology

APPS **must** provide the WORKFLOW_ORCHESTRATOR application as a conforming executor of the applicable methodology Workflow model under CA-R-1519 **and** CA-R-1520.

- the application owns coordination of an accepted request across its Workflow Runs; Tools remain realizations of individual methodology Actions under CA-R-1516.
- applicable Workflow definitions, input bindings, result conditions, **and** continuation rules determine execution. the application **must not** maintain a second independently authored Update-to-Replace rule **or** another Workflow-specific policy.
- the application's RMED specifies its execution behavior; Workflow definitions are governed inputs, **not** a requirement **to** use those Workflows **to** build the application.
- the application implements the methodology conformance requirements. its existence is **not** a backward Demand from FRAMEWORK_METHODOLOGY **to** FRAMEWORK_ENGINE.

the application name does **not** by itself declare a new Scope Unit, install a service, **or** replace an existing specialized execution component.
