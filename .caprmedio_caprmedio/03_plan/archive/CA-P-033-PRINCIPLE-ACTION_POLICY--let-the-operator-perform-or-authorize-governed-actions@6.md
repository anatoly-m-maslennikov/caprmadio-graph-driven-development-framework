---
atom_id: CA-P-033
subject_scopes:
  - principles
version: 6
updated_at: 2026-09-05 00:41:24 +0400
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
