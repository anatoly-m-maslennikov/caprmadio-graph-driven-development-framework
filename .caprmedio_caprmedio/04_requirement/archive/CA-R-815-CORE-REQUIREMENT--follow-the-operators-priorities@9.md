---
atom_id: CA-R-815
subject_scopes:
  - principles
version: 9
updated_at: 2026-09-05 00:41:24 +0400
relations:
  child_of:
    - CA-P-033
---
# Follow the Operator's priorities

CAPRMEDIO must support implementing Operator-established priorities for possible project trade-offs in the CAPRMEDIO instance.

## Formal statement

Let \(I\) be the current CAPRMEDIO instance, \(T\) the possible project trade-offs, and \(\Pi_O(T)\) the admissible priority models established by the Operator.

\[
\forall \pi\in\Pi_O(T):
\operatorname{CanImplementPriorityModel}(I,\pi)
\]
