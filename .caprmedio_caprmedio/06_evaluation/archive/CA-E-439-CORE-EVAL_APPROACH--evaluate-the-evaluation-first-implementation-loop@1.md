---
atom_id: CA-E-439
cce_version: "cce_1"
cce_form: "evaluation"
subjects:
  governs:
    occurrent:
      - "Project/Implementation/execution"
  depends_on:
    continuant:
      - "Spec"
      - "Atom/Content Role: Requirement"
      - "Atom/Content Role: Method"
      - "Atom/Content Role: Evaluation"
      - "Atom/Content Role: Delivery"
      - "Atom/Content Role: Implementation"
    occurrent:
      - "Dependency Order Derivation"
version: 1
updated_at: "2026-09-05 18:40:03 +0400"
relations:
  child_of:
    - "CA-E-001"
  evaluation_for:
    - "CA-M-267"
    - "CA-M-239"
---
# Evaluate the Evaluation-first implementation loop

the implementation-loop Evaluation **must** return `fail` **if** unchanged mode, RMED, **and** complete execution inputs yield different applicable tasks **or** ordering, a consumer runs **before** its prerequisite, Atom ID overrides a prerequisite, a cycle is admitted, feasible Evaluation-preparation precedence is omitted **or** left implicit, **or** an absolute E-first barrier prevents preparation of an Evaluation prerequisite. it **must** also return `fail` **if** applicable Methods **or** Delivery boundaries are omitted from Evaluation **or** Requirement implementation, Atom ID resolves a Method conflict, preparation of an Evaluation is reported as its execution, **or** completion is reported with **any** applicable Evaluation failed, blocked, **or** unevaluated. repeated evaluate-fix execution **and** runtime loops alone **must not** be rejected as prerequisite cycles.
