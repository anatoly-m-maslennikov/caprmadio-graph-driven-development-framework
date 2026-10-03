---
subject_scopes:
  - authority
version: 6
updated_at: 2026-08-21 04:57:22
relations:
  child_of:
    - CA-INTENT
---
# Make accepted requirements checkable

CAPRMEDIO must make every accepted Requirement checkable when it is used to govern work or evaluate a result. A check may be contained directly or supplied through a linked Evaluation. A formal predicate is a contained Evaluation only when its required inputs, procedure, and binary result interpretation are recoverable.

## Formal statement

Let \(R\) be the set of Requirements and \(E\) the set of Evaluation procedures.

\[
\forall r\in R:\bigl(\operatorname{Accepted}(r)\land\operatorname{UsedToGovernOrEvaluate}(r)\bigr)\Rightarrow\exists e\in E:\operatorname{Checks}(e,r)\land\operatorname{Recoverable}(\operatorname{Inputs}(e))\land\operatorname{Recoverable}(\operatorname{Procedure}(e))\land\operatorname{Recoverable}(\operatorname{BinaryResultInterpretation}(e))\land\operatorname{Result}(e,r)\in\{\operatorname{pass},\operatorname{fail}\}\land\bigl(\operatorname{ContainedBy}(e,r)\lor\operatorname{LinkedFrom}(e,r)\bigr)
\]
