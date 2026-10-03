---
subject_scopes:
  - principles
version: 2
updated_at: 2026-08-21 04:43:43
relations:
  child_of:
    - CA-INTENT
---
# Use two Actor Types for governed actions

CAPRMEDIO must classify every Actor that performs or authorizes a governed action as exactly one of two Actor Types: Operator or AI Agent.

## Formal statement

Let \(A\) be the set of Actors that perform or authorize governed actions and \(T\) the Actor Type function.

\[
\operatorname{ActorTypes}=\{\operatorname{Operator},\operatorname{AI\ Agent}\}\land\forall a\in A:\exists!t\in\operatorname{ActorTypes}:\operatorname{HasType}(a,t)
\]
