---
subject_scopes:
  - principles
version: 7
updated_at: 2026-08-21 06:08:16
relations:
  child_of:
    - CA-INTENT
---
# Use lossless selective exposure

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
