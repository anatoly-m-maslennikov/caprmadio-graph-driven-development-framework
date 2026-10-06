---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Workflow"
  depends_on:
    - "Workflow Run"
    - "Step"
    - "Action"
    - "Workflow/Relation Kind: On Result"
    - "Artifact/Revision"
    - "Operator"
version: 1
updated_at: "2026-09-18 21:23:47 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"evaluation_for": ["CA-R-1519", "CA-R-1520"]}
---
# Validate Workflow execution and handoff definitions

the Evaluation **must** check that a Workflow's declared execution **and** handoff behavior is complete under CA-R-1519 **and** CA-R-1520.

## Cases and expected results

- complete inputs, resolvable Actions, admitted transitions, explicit terminal outcomes, **and** an executor with the required capabilities: pass this definition check.
- a missing capability, unresolved input, missing continuation-selection rule, **or** absent applicable approval condition: reject the affected execution definition.
- a terminal handoff with the target Revision, complete continuation inputs, reason, check evidence, **and** performed-effect account: accept its declared continuation boundary.
- a handoff that resumes predecessor Steps, claims successor success **before** execution, bypasses approval, resets retries, **or** admits an unbounded continuation cycle: reject.
- a cross-Workflow ON_RESULT Step edge offered as a Run handoff: reject; the two relations have different endpoints **and** responsibilities.

report the exact failing source **and** condition. a valid definition does **not** prove executor Implementation correctness **or** that a Run occurred.
