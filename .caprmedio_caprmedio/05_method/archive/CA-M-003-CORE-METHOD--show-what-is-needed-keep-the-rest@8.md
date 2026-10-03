---
atom_id: CA-M-003
subject_scopes:
  - principles
version: 8
updated_at: 2026-09-05 00:51:50 +0400
relations:
  child_of:
    - CA-R-1420
---
# Show what is needed; keep the rest

CAPRMEDIO must preserve information necessary for governed use, expose only the currently justified sufficient set for the task, and keep unexposed preserved information recoverable.

## Formal statement

Let \(P\) be preserved information, \(N\) information necessary for governed use, \(J(t)\) the currently justified sufficient information set for task \(t\), \(E(t)\) information exposed to that task, and \(K\) recoverable information.

\[
N\subseteq P
\]

For every task \(t\):

\[
\operatorname{CurrentlyJustified}(J(t),t)
\quad\land\quad
\operatorname{SufficientFor}(J(t),t)
\quad\land\quad
J(t)\subseteq P
\quad\land\quad
E(t)=J(t)
\]

\[
P\setminus E(t)\subseteq K
\]
