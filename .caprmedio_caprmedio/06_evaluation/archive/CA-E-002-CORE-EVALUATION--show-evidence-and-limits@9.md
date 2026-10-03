---
atom_id: CA-E-002
subject_scopes:
  - authority
version: 9
updated_at: 2026-09-05 00:51:50 +0400
relations:
  child_of:
    - CA-R-1420
---
# Show evidence and limits

Every governed conclusion offered for reliance must be bound to recoverable evidence, material uncertainty, and conditions under which reliance begins, changes, and ends.

## Formal statement

Let \(C\) be the set of governed conclusions. For every \(c\in C\):

\[
\operatorname{OfferedForReliance}(c)\Rightarrow\operatorname{BoundToRecoverable}(c,\operatorname{Evidence}(c))\land\operatorname{BoundToRecoverable}(c,\operatorname{MaterialUncertainty}(c))\land\operatorname{BoundToRecoverable}(c,\operatorname{BeginConditions}(c))\land\operatorname{BoundToRecoverable}(c,\operatorname{ChangeConditions}(c))\land\operatorname{BoundToRecoverable}(c,\operatorname{EndConditions}(c))
\]
