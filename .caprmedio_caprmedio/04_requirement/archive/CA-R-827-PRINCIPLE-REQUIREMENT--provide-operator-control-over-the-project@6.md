---
subject_scopes:
  - principles
version: 6
updated_at: 2026-08-21 06:08:16
relations:
  child_of:
    - CA-INTENT
---
# Provide Operator control over the project

CAPRMEDIO must keep project evolution outside the CAPRMEDIO instance under the Operator's control.

## Formal statement

Let \(S\) be the set of governed states, \(P(s)\) the governed project parts outside the CAPRMEDIO instance in state \(s\), and \(O\) the Operator.

\[
\forall s\in S,\forall x\in P(s):\operatorname{CanControl}(O,x,s)
\]
