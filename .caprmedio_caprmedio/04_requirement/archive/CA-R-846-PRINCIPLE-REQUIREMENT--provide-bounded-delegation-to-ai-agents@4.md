---
subject_scopes:
  - principles
version: 4
updated_at: 2026-08-21 06:08:16
relations:
  child_of:
    - CA-INTENT
---
# Provide bounded delegation to AI Agents

CAPRMEDIO must let the Operator create, inspect, limit, modify, suspend, and revoke delegations and mandatory authorization rules for identified AI Agents.

## Formal statement

Let \(O\) be the Operator, \(A\) the set of identified AI Agents, \(D\) the set of delegations to AI Agents, and \(G\) the set of mandatory AI Agent authorization rules.

\[
\forall a\in A:\operatorname{CanCreateDelegation}(O,a)\land\operatorname{CanCreateMandatoryAuthorizationRule}(O,a)
\]

\[
\forall b\in D\cup G:\operatorname{CanInspect}(O,b)\land\operatorname{CanLimit}(O,b)\land\operatorname{CanModify}(O,b)\land\operatorname{CanSuspend}(O,b)\land\operatorname{CanRevoke}(O,b)
\]
