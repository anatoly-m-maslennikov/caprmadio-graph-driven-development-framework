---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Implementation Process"
  depends_on:
    - "Process"
    - "Action"
    - "Implementation Preparation"
    - "Evaluation Implementation"
    - "Requirement Implementation"
    - "Implementation Evaluation"
    - "Implementation Repair"
    - "Implementation Retry Control"
    - "Spec"
    - "Operator"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Implementation"
version: 4
updated_at: "2026-09-17 14:50:12 +0000"
relations: {"child_of":["CA-M-261"],"relates_to":["CA-M-266","CA-O-061","CA-O-024","CA-M-270","CA-O-017","CA-O-018","CA-O-019","CA-O-020","CA-O-021"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Implement Evaluations before required behavior

Implementation Process **means** the core Process for executing the selected implementation mode against current RMED **and** complete execution inputs through the following reusable Actions.

| Node **and** Action reference | Result condition | Next node **or** outcome |
|---|---|---|
| prepare — CA-O-017, Prepare implementation work | next ready work prepares an Evaluation implementation | implement-evaluation |
| prepare — CA-O-017 | next ready work realizes a Requirement, including a prerequisite needed by an Evaluation | implement-requirement |
| prepare — CA-O-017 | next ready work executes an applicable Evaluation | evaluate |
| prepare — CA-O-017 | applicable work complete **and** **all** applicable Evaluations pass, with **none** failed, blocked, **or** unevaluated | report successful completion; stop |
| prepare — CA-O-017 | unresolved authority conflict, prerequisite cycle, **or** incomplete work with no ready next work | stop **and** report the blocker **to** the Operator; do **not** report completion |
| implement-evaluation — CA-O-018, Implement Evaluations | selected work completed **or** sufficient existing implementation reused under the selected mode | prepare, retaining completed work |
| implement-requirement — CA-O-019, Implement Requirements | selected work completed | prepare, retaining completed work |
| evaluate — CA-O-020, Run implementation Evaluations | selected Evaluations pass | prepare, retaining results for the evaluated candidate |
| evaluate — CA-O-020 | an Evaluation fails | retry-control |
| retry-control — CA-O-024, Control implementation retries | the next retry is permitted | repair, starting the permitted fix-and-evaluate round **and** counting it under CA-O-024 |
| retry-control — CA-O-024 | repair is prohibited, requires unresolved approval, has an unmet confidence gate, **or** has no remaining retry allowance | stop **and** report the remaining failures **to** the Operator |
| repair — CA-O-021, Repair nonconforming Implementation | permitted correction completed | prepare, resolving affected work **and** required re-evaluation **without** resetting the execution's retry budget |
| repair — CA-O-021 | a governing RMED change is needed | obtain the disposition required by CA-O-061; **after** an authorized change is completed, resume at prepare against the new baseline |
| **any** Action | unmet confidence **or** authorization gate, unresolved authority conflict, **or** failed **or** blocked work with no admitted recovery route | stop **and** report the exact state **to** the Operator |

the prepare node selects residual ready work **in** the prerequisite-respecting order returned by CA-O-017; it is **not** permission **to** rerun completed work **or** reset a retry allowance. Evaluation preparation is distinct from Evaluation execution: preparation receives precedence wherever prerequisites permit, **not** an absolute barrier against the Requirement implementation that an Evaluation consumes. use CA-O-024 **to** control **every** failed-Evaluation recovery; an authorized governing change requires renewed work **and** Evaluation resolution under CA-O-061, **not** reuse of stale completion evidence. the prerequisite graph **must** remain acyclic; permitted evaluate-fix revisits **and** runtime loops are **not** by themselves circular prerequisites.
