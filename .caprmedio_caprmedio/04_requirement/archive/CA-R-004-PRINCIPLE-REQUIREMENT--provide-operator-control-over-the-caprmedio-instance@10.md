---
subject_scopes:
  - principles
version: 10
updated_at: 2026-08-21 06:08:16
relations:
  child_of:
    - CA-INTENT
---
# Provide Operator control over the CAPRMEDIO instance

CAPRMEDIO must keep its instance under the Operator's control, and no governed instance change may remove the Operator's ability to change the project through that instance.

## Formal statement

Let \(S\) be the set of governed states, \(I(s)\) the governed parts of the CAPRMEDIO instance in state \(s\), \(O\) the Operator, \(C_I(s)\) the admissible instance changes in \(s\), and \(T(c,s)\) the state produced by applying change \(c\) to \(s\).

\[
\forall s\in S,\forall x\in I(s):\operatorname{CanControl}(O,x,s)
\]

\[
\forall s\in S:\operatorname{CanChangeProjectThroughInstance}(O,s)
\]

\[
\forall s\in S,\forall c\in C_I(s),\ s'=T(c,s):\operatorname{CanChangeProjectThroughInstance}(O,s')
\]
