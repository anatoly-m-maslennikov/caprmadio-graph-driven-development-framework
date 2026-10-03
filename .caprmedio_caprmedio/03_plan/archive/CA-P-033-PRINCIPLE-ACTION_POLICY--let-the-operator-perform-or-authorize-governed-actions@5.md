---
subject_scopes:
  - principles
version: 5
updated_at: 2026-08-21 06:44:58
relations:
  child_of:
    - CA-INTENT
---
# Let the Operator perform or authorize governed actions

The Operator is the collective Actor with original authority over the project and its CAPRMEDIO instance and may perform or authorize governed actions within that authority.

## Formal statement

Let \(O\) be the Operator, \(P\) the project, \(I\) its CAPRMEDIO instance, and \(Q\) the set of governed actions.

\[
\operatorname{CollectiveActor}(O)\land\operatorname{OriginalAuthorityOver}(O,P)\land\operatorname{OriginalAuthorityOver}(O,I)
\]

\[
\forall q\in Q:\operatorname{WithinAuthority}(O,q)\Rightarrow\operatorname{MayPerformOrAuthorize}(O,q)
\]
