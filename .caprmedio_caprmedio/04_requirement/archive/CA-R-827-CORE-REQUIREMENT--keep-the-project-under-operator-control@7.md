---
atom_id: CA-R-827
subject_scopes:
  - principles
version: 7
updated_at: 2026-09-05 01:05:19 +0400
relations:
  child_of:
    - CA-P-033
---
# Keep the project under Operator control

CAPRMEDIO must keep project evolution outside the CAPRMEDIO instance under the Operator's control.

## Formal statement

Let \(S\) be the set of governed states, \(P(s)\) the governed project parts outside the CAPRMEDIO instance in state \(s\), and \(O\) the Operator.

\[
\forall s\in S,\forall x\in P(s):\operatorname{CanControl}(O,x,s)
\]
