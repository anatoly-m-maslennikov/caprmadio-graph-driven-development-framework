---
subject_scopes:
  - principles
version: 4
updated_at: 2026-08-21 06:08:16
relations:
  child_of:
    - CA-INTENT
---
# Let AI Agents act only under delegated authority

An AI Agent has no original authority, cannot create or expand its own authority, and may perform or authorize a governed action only when a current Operator-established delegation or rule permits that complete action, target, and decision boundary.

## Formal statement

Let \(A\) be the set of AI Agents, \(Q\) the set of governed actions, and \(B_c\) the set of current Operator-established authorization bindings, including delegations and rules.

\[
\forall a\in A:\neg\operatorname{OriginalAuthority}(a)\land\neg\operatorname{MayCreateOrExpandOwnAuthority}(a)
\]

\[
\forall a\in A,\forall q\in Q:\operatorname{MayPerformOrAuthorize}(a,q)\Rightarrow\exists b\in B_c:\operatorname{Actor}(b)=a\land\operatorname{Permits}(b,q)\land\operatorname{PermitsTarget}(b,\operatorname{Target}(q))\land\operatorname{PermitsDecisionBoundary}(b,\operatorname{DecisionBoundary}(q))
\]
