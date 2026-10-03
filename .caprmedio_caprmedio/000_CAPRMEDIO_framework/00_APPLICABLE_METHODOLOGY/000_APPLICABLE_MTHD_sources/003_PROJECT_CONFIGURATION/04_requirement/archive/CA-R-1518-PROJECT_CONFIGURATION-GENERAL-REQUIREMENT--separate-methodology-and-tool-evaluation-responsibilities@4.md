---
subjects:
  governs: "Atom/Content Role: Evaluation"
  depends_on:
    - "Methodology"
    - "Scope Unit"
    - "Action"
    - "Workflow"
    - "Step"
    - "Tool"
    - "Atom/Content Role: Operations"
    - "Atom/Content Role: Implementation"
    - "Evaluation For Relation"
version: 4
updated_at: "2026-09-23 23:53:58 +0000"
relations:
  relates_to: [CA-R-1018, CA-R-1514, CA-R-1515, CA-R-1516, CA-E-486]
---
# Separate methodology and Tool Evaluation responsibilities

**in** the caprmedio Project, Evaluation responsibility for operational definitions **and** their Tool implementations **must** follow this allocation:

- methodology source Scope Units own Evaluations of Action **and** Workflow definitions, including valid Action references, Step inputs, typed transitions, **and** termination **or** bounded retry conditions. these Evaluations **may** directly check O authority under CA-R-1018; checks for Steps **and** Runs reuse CA-E-486 **when** applicable.
- TOOLS **and** its Tool Scope Units own Evaluations of Tools: implementation behavior, interfaces, failures, **and** conformance **to** the Action implemented by the Tool. these Evaluations **must not** independently define the correctness rules of the referenced Action **or** Workflow.

checking whether a Tool realizes an Action correctly is distinct from checking whether that Action's definition is valid. a Tool test **may** use the methodology definition as its expected-behavior authority **without** taking ownership of definition validation.
