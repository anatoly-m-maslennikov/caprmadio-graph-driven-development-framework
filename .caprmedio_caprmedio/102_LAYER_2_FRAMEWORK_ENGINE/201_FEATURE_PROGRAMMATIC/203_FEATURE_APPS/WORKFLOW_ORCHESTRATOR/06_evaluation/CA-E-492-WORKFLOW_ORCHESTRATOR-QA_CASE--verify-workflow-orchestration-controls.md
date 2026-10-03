---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Workflow Run"
  depends_on:
    - "Workflow"
    - "Step"
    - "Step Run"
    - "Action"
    - "Tool"
    - "Operator"
    - "Applicable Methodology"
    - "Implementation"
version: 3
updated_at: "2026-09-20 15:47:25 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"evaluation_for": ["CA-R-1522", "CA-R-1523", "CA-M-302"], "relates_to": ["CA-E-489", "CA-E-495", "CA-E-496", "CA-E-497"]}
---
# Verify Workflow orchestration controls

the Evaluation **must** check WORKFLOW_ORCHESTRATOR's observable conformance **and** client-control behavior against its RMED.

1. submit an admitted Workflow with a deliberately long-running Action; require an accepted-work identifier **before** Action completion.
2. disconnect the submitting client, reconnect using that identifier, **and** inspect progress **and** the final result **without** creating another Run.
3. exercise an admitted Operator-input wait **and** cancellation request; require responsive controls **and** a distinction between requested cancellation **and** confirmed termination.
4. provide valid methodology fixtures with different declared continuation mappings; require the application **to** follow the supplied definitions rather than a hard-coded Update-to-Replace branch.
5. submit a malformed definition rejected by the applicable methodology checks; require a visible definition-validation failure rather than invented execution behavior.
6. submit a valid definition with an unavailable required worker **or** capability, missing invocation input, **or** absent current permission; require a distinct execution-admission block while preserving the valid definition **and** its validation result.

7. execute an admitted mixed-context fixture: preserve the same reusable Action identity across Integrated **and** Isolated invocations, return the Integrated input **and** instruction through MCP, **and** dispatch Programmatic Steps **without** an Agent-context requirement.
8. reconnect **without** earlier session conversation: recover the pending invocation, exact Run identities, relevant results, next instruction, **and** return route from executor state; do **not** replay an already performed effect merely **to** reconstruct context.
9. let an Agentic Step make several Tool calls: require nested canonical Journal evidence **without** invented Workflow nodes **or** a second execution-history authority.

fail on blocked coordination, lost accepted work, unauthorized effects, false completion, **or** independently authored Workflow policy. these are application tests; they consume methodology correctness authority rather than redefining it.
