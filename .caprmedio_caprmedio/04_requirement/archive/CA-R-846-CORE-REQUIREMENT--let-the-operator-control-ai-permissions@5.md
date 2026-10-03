---
atom_id: CA-R-846
subject_scopes:
  - principles
version: 5
updated_at: 2026-09-05 00:54:31 +0400
relations:
  child_of:
    - CA-P-033
---
# Let the Operator control AI permissions

CAPRMEDIO must let the Operator create, inspect, limit, modify, suspend, and revoke delegations and mandatory authorization rules for identified AI Agents.

## Formal statement

Let \(O\) be the Operator, \(A\) the set of identified AI Agents, \(D\) the set of delegations to AI Agents, and \(G\) the set of mandatory AI Agent authorization rules.

\[
\forall a\in A:\operatorname{CanCreateDelegation}(O,a)\land\operatorname{CanCreateMandatoryAuthorizationRule}(O,a)
\]

\[
\forall b\in D\cup G:\operatorname{CanInspect}(O,b)\land\operatorname{CanLimit}(O,b)\land\operatorname{CanModify}(O,b)\land\operatorname{CanSuspend}(O,b)\land\operatorname{CanRevoke}(O,b)
\]
