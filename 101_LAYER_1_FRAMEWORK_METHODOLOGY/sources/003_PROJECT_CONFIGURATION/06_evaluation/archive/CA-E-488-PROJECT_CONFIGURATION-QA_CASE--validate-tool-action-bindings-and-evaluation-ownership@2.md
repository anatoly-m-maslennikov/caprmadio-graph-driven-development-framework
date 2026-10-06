---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Tool"
  depends_on:
    - "Action"
    - "Workflow"
    - "Step"
    - "Methodology"
    - "Methodology Source"
    - "Scope Unit"
    - "Atom/Content Role: Operations"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Implementation"
version: 2
updated_at: "2026-09-23 23:42:09 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for: [CA-R-1515, CA-R-1516, CA-R-1517, CA-R-1518]
---
# Validate Tool Action bindings and Evaluation ownership

the Evaluation of a caprmedio Tool's methodology binding **must** check the canonical Action **or** admitted Workflow owner, binding cardinality, **and** division of Evaluation responsibility under CA-R-1515 through CA-R-1518.

## Cases and expected results

- the Tool implements **`=1`** resolvable applicable Action owned by a methodology source outside the Tool's subtree: pass the binding check.
- an Action-bound Tool has **`=0`** **or** **`>1`** implemented Action entry bindings, an unresolved definition, **or** a copied operational definition owned by the Tool: fail.
- `VALIDATE_ATOMS` binds **`=1`** applicable CA-O-080 Workflow entry outside its own subtree, with resolvable constituent Steps **and** Actions: pass its explicitly admitted binding check. missing **or** additional entry bindings, silently substituted Workflow behavior, **or** an invented wrapper Action **to** conceal duplicated graph authority: fail.
- an implementation reference targets an O Atom owned by the Tool's Scope Unit **or** a descendant: fail. a methodology Evaluation checking its own O definition **must not** fail this Tool-only containment rule.
- Tool Evaluations check the Tool's realization of its Action **or** admitted Workflow while methodology Evaluations check the operational definitions: pass the responsibility check.
- a Tool Evaluation independently owns Action **or** Workflow definition-validity rules: fail for misplaced authority; invoking an existing methodology check does **not** transfer that authority.
- a Workflow contains an unresolved Step Action **or** an unbounded retry loop: report the defect against the methodology definition through its methodology Evaluation, rather than silently repairing the Workflow inside the Tool's specification.

report binding conformance separately from actual Implementation results. valid ownership **and** references alone **must not** be reported as proof that the Tool works **or** that **all** indirect cycles are absent.
