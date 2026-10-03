---
subject_scopes:
  - principles
version: 8
updated_at: 2026-08-21 07:29:53
relations:
  child_of:
    - CA-INTENT
---
# Support Operator priorities for project trade-offs

CAPRMEDIO must support implementing Operator-established priorities for possible project trade-offs in the CAPRMEDIO instance.

## Formal statement

Let \(I\) be the current CAPRMEDIO instance, \(T\) the possible project trade-offs, and \(\Pi_O(T)\) the admissible priority models established by the Operator.

\[
\forall \pi\in\Pi_O(T):
\operatorname{CanImplementPriorityModel}(I,\pi)
\]
