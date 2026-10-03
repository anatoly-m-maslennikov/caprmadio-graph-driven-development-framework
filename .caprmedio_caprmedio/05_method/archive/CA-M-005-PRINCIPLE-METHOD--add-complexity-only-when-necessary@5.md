---
subject_scopes:
  - principles
version: 5
updated_at: 2026-08-21 04:57:22
relations:
  child_of:
    - CA-INTENT
---
# Add complexity only when necessary

CAPRMEDIO may admit or retain a mechanism only when existing mechanisms cannot preserve a required outcome or a material governed distinction.

## Formal statement

Let \(M\) be the admitted mechanisms and \(Q\) the required outcomes and material governed distinctions. For every mechanism \(m\):

\[
(\operatorname{Admit}(m)\lor\operatorname{Retain}(m))\Rightarrow\exists q\in Q:\neg\operatorname{Preserves}(M\setminus\{m\},q)
\]
