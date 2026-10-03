---
subject_scopes:
  - principles
version: 5
updated_at: 2026-08-21 04:57:22
relations:
  child_of:
    - CA-INTENT
---
# MECE: Mutually exclusive, collectively exhaustive

CAPRMEDIO must use Mutually Exclusive, Collectively Exhaustive (MECE) canonical decompositions whenever a decomposition claims to cover a declared universe, within that universe and at that level of abstraction.

## Formal statement

For every canonical decomposition \(D=\{d_i\}_{i\in I}\) that claims to cover a declared universe \(U\) at one level of abstraction:

\[
\bigcup_{i\in I}d_i=U
\quad\land\quad
\forall i,j\in I:\ i\ne j\Rightarrow d_i\cap d_j=\varnothing
\]
