---
subject_scopes:
  - authority
version: 8
updated_at: 2026-08-21 06:08:16
relations:
  child_of:
    - CA-INTENT
---
# Bound every reliance

Every governed conclusion offered for reliance must be bound to recoverable evidence, material uncertainty, and conditions under which reliance begins, changes, and ends.

## Formal statement

Let \(C\) be the set of governed conclusions. For every \(c\in C\):

\[
\operatorname{OfferedForReliance}(c)\Rightarrow\operatorname{BoundToRecoverable}(c,\operatorname{Evidence}(c))\land\operatorname{BoundToRecoverable}(c,\operatorname{MaterialUncertainty}(c))\land\operatorname{BoundToRecoverable}(c,\operatorname{BeginConditions}(c))\land\operatorname{BoundToRecoverable}(c,\operatorname{ChangeConditions}(c))\land\operatorname{BoundToRecoverable}(c,\operatorname{EndConditions}(c))
\]
