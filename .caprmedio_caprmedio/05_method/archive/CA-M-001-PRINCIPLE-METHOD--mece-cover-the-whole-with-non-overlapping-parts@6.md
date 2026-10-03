---
atom_id: CA-M-001
subject_scopes:
  - principles
version: 6
updated_at: 2026-09-05 00:44:25 +0400
relations:
  child_of:
    - CA-INTENT
---
# MECE: Cover the whole with non-overlapping parts

CAPRMEDIO must use Mutually Exclusive, Collectively Exhaustive (MECE) canonical decompositions whenever a decomposition claims to cover a declared universe, within that universe and at that level of abstraction.

## Formal statement

For every canonical decomposition \(D=\{d_i\}_{i\in I}\) that claims to cover a declared universe \(U\) at one level of abstraction:

\[
\bigcup_{i\in I}d_i=U
\quad\land\quad
\forall i,j\in I:\ i\ne j\Rightarrow d_i\cap d_j=\varnothing
\]
