---
atom_id: CA-R-1522
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
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
version: 4
updated_at: "2026-10-03 19:26:44 +0400"
relations: {"relates_to": ["CA-R-1187", "CA-R-1178", "CA-R-1426", "CA-R-1519", "CA-R-1520", "CA-R-1516", "CA-R-1526", "CA-R-1527", "CA-R-1528", "CA-R-1529"]}
---
# Provide Workflow orchestration from methodology

WORKFLOW_ORCHESTRATOR **must** be the APPS Scope Unit that provides a conforming executor of the applicable methodology Workflow model under CA-R-1519 **and** CA-R-1520.

- the application owns coordination of an accepted request across its Workflow Runs; Tools remain realizations of individual methodology Actions under CA-R-1516.
- support Programmatic Actions **and** Agentic Steps. the Operator selects caller-coordinated execution **or** independent execution through an admitted worker adapter. independent execution launches isolated Agents **and** records their admitted results **without** requiring a live main session. caller-coordinated execution returns the Action prompt **and** invocation envelope through MCP. **only** admitted results permit progress; retain coordination state rather than requiring the session **to** remember the procedure.
- applicable Workflow definitions, input bindings, result conditions, **and** continuation rules determine execution. the application **must not** maintain a second independently authored Update-to-Replace rule **or** another Workflow-specific policy.
- the application's RMED specifies its execution behavior; Workflow definitions are governed inputs, **not** a requirement **to** use those Workflows **to** build the application.
- the application implements the methodology conformance requirements. its existence is **not** a backward Demand from FRAMEWORK_METHODOLOGY **to** FRAMEWORK_ENGINE.

The application is one immediate unordered APPS Scope Unit. Its declaration does not install a service **or** replace an existing specialized execution component.
