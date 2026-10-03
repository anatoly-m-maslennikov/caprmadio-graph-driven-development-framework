---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Atom/Content Role"
  depends_on:
    - "Spec Content Roles"
    - "Change Content Roles"
    - "Atom/Claim"
    - "Action"
    - "Workflow"
    - "Step"
    - "Implementation"
    - "Carrier"
version: 2
updated_at: "2026-09-21 00:57:42 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"evaluation_for": ["CA-R-1548", "CA-R-1549", "CA-R-1550", "CA-R-1339", "CA-R-1340", "CA-R-1343", "CA-R-1530", "CA-R-1569"]}
---
# Validate Specification, Change, and Implementation classification

the classification Evaluation **must** fail **if** an Atom's Content Role does **not** match its actual contribution under the Specification, Change, **and** Implementation definitions.

| Claim contribution | Expected classification |
|---|---|
| a model definition, required property, **or** permission governing a Concern, Analysis, Task, Action, **or** Workflow | Requirement |
| a convention for authoring **or** constructing that content | Method |
| a falsifiable correctness check | Evaluation |
| a Carrier's fields, format, **or** placement | Delivery |
| a particular unresolved issue, analytical finding, **or** intended Task | the matching Concern, Analysis, **or** Plan role |
| a particular reusable Action behavior, Workflow graph, Step invocation binding, **or** Actor participation/authorization behavior | Operations |
| a current realization of accepted specification | Implementation |

reusing the specified content's role as the specification's role **must** fail this check. a long-lived Concern **or** reusable Workflow **must not** fail merely because its lifetime is long.
