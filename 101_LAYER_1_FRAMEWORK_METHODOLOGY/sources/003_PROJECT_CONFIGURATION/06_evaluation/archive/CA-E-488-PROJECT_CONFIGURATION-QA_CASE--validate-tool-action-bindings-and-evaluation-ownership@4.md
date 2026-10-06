---
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
version: 4
updated_at: "2026-09-23 23:53:58 +0000"
relations:
  evaluation_for: [CA-R-1515, CA-R-1516, CA-R-1517, CA-R-1518]
---
# Validate Tool Action bindings and Evaluation ownership

the Evaluation of a caprmedio Tool's methodology binding **must** check the canonical Action owner, binding cardinality, **and** division of Evaluation responsibility under CA-R-1515 through CA-R-1518.

## Cases and expected results

- the Tool implements **`=1`** resolvable applicable Action owned by a methodology source outside the Tool's subtree: pass the binding check.
- the Tool has **`=0`** **or** **`>1`** implemented Action bindings, an unresolved definition, **or** a copied operational definition owned by the Tool: fail.
- an implementation reference targets an O Atom owned by the Tool's Scope Unit **or** a descendant: fail. a methodology Evaluation checking its own O definition **must not** fail this Tool-only containment rule.
- Tool Evaluations check the Tool's realization of its Action while methodology Evaluations check the operational definitions: pass the responsibility check.
- a Tool Evaluation independently owns Action **or** Workflow definition-validity rules: fail for misplaced authority; invoking an existing methodology check does **not** transfer that authority.
- a Workflow contains an unresolved Step Action **or** an unbounded retry loop: report the defect against the methodology definition through its methodology Evaluation, rather than silently repairing the Workflow inside the Tool's specification.

report binding conformance separately from actual Implementation results. valid ownership **and** references alone **must not** be reported as proof that the Tool works **or** that **all** indirect cycles are absent.
