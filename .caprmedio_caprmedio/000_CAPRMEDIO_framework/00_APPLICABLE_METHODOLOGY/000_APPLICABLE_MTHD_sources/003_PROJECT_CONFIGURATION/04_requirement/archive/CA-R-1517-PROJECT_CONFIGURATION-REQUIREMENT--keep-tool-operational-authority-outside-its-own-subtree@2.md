---
subjects:
  governs: "Tool"
  depends_on:
    - "Scope Unit"
    - "Action"
    - "Workflow"
    - "Atom/Content Role: Operations"
    - "Atom/Content Role: Evaluation"
    - "Methodology"
version: 2
updated_at: "2026-09-18 15:44:48 +0000"
relations:
  relates_to: [CA-R-1515, CA-R-1516, CA-R-1518]
---
# Keep Tool operational authority outside its own subtree

**in** the caprmedio Project, a Tool's implementation reference **to** a methodology Action **or** Workflow definition **must not** target an O Atom owned by the Tool's Scope Unit **or** **any** descendant of that Scope Unit.

- the restriction concerns the owner of the operational definition, **not** the location of the Tool's code, prompts, **or** runtime results.
- methodology Evaluations of their own Action **and** Workflow definitions under CA-R-1518 are **not** Tool implementation references **and** are **not** prohibited by this rule.

this restriction prevents self-reference through the Tool's own subtree; it does **not** establish that **all** indirect dependency cycles are absent.
