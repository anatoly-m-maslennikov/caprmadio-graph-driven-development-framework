---
subject_scopes:
  - principles
version: 9
updated_at: 2026-08-22 00:53:40
relations:
  child_of:
    - CA-INTENT
---
# Provide one project graph as the operating model

CAPRMEDIO must use one explicit typed project graph as the canonical operating representation of governed project meaning and state.

## Formal statement

Let \(U\) be the set of Scope Units, \(A\) the set of Artifacts, and \(E\) the set of registered typed edges. Let \(X\) be the set of governed project meanings and states.

\[
V=U\mathbin{\dot\cup}A,\qquad G=(V,E),\qquad
\forall x\in X:\operatorname{HasCanonicalRepresentation}(x,G)
\]
