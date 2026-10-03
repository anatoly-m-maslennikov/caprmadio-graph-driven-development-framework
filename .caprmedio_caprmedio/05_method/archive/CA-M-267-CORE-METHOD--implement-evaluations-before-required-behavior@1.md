---
atom_id: CA-M-267
cce_version: "cce_1"
cce_form: "method"
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
      - "Atom/Content Role: Plan/Type: Task"
    occurrent:
      - "Dependency Order Derivation"
version: 1
updated_at: "2026-09-05 18:40:03 +0400"
relations:
  child_of:
    - "CA-M-261"
  relates_to:
    - "CA-M-239"
    - "CA-M-266"
    - "CA-M-268"
    - "CA-M-269"
    - "CA-M-270"
---
# Implement Evaluations before required behavior

**to** execute the selected implementation mode, resolve its current RMED **and** complete execution inputs, **then** perform the applicable work through this procedure:

1. derive the applicable tasks **and** their explicit prerequisites. give preparation of Evaluation implementations precedence over Requirement realization wherever actual prerequisites permit it; represent that precedence **in** the execution dependencies **before** deriving the order under CA-M-239. use Atom ID **only** **to** break remaining ties between ready tasks, **and** reject a prerequisite cycle. unchanged mode, RMED, **and** complete execution inputs **must** yield the same applicable tasks **and** order.
2. implement the applicable Evaluations using **all** Methods governing that work within its Delivery boundaries; reuse sufficient existing Evaluation implementations **when** the selected mode permits reuse. this is **not** an absolute barrier against a prerequisite that those Evaluations consume.
3. implement the Requirements using **all** applicable Methods within the applicable Delivery boundaries. a Method conflict requires an authority disposition rather than an Atom-ID winner.
4. run **all** applicable Evaluations against the candidate Implementation **when** their execution prerequisites are available; distinguish preparation of an Evaluation from its execution.
5. **if** an Evaluation fails, **then** fix nonconforming Implementation **and** repeat the applicable work under CA-M-269. correcting the implementation of an Evaluation is Implementation work; changing governing RMED follows CA-M-268.
6. report successful completion **only** **when** **all** applicable Evaluations pass, with **none** failed, blocked, **or** unevaluated. an unresolved authority conflict **or** prerequisite cycle requires escalation rather than automatic continuation.

the prerequisite graph **must** remain acyclic; repeated evaluate-fix work **and** runtime loops are **not** by themselves circular prerequisites.
