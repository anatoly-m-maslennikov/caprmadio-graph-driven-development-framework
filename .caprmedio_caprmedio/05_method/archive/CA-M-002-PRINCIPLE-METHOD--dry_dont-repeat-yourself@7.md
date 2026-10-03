---
subject_scopes:
  - principles
version: 7
updated_at: 2026-08-21 07:29:53
relations:
  child_of:
    - CA-INTENT
---
# DRY: Don't repeat yourself

CAPRMEDIO must apply Don't Repeat Yourself (DRY) to governed meaning: each meaning has one canonical owner capable of resolving it completely and unambiguously; every other use must reference, derive, generate, or explicitly adapt that owner without becoming a duplicate definition.

## Formal statement

Let \(M\) be the set of governed meanings, \(C(m)\) the set of canonical owners of meaning \(m\), and \(\operatorname{Owner}(u)\) the owner containing use \(u\).

\[
\forall m\in M:\ |C(m)|=1
\]

\[
\forall m\in M,\forall c\in C(m):\operatorname{CanResolveCompletely}(c,m)\land\operatorname{CanResolveUnambiguously}(c,m)
\]

For each \(m\), let \(c_m\) be the unique member of \(C(m)\). For every use \(u\) of \(m\) outside \(c_m\):

\[
\operatorname{Uses}(u,m)\land\operatorname{Owner}(u)\ne c_m
\Rightarrow
\operatorname{Mode}(u,c_m,m)\in
\{\operatorname{reference},\operatorname{derive},\operatorname{generate},\operatorname{declaredAdaptation}\}
\]
