---
atom_id: CA-D-002
subject_scopes:
  - principles
version: 11
updated_at: 2026-09-05 00:51:50 +0400
relations:
  child_of:
    - CA-R-1420
---
# Make information clear to the Operator

CAPRMEDIO must adapt governed meaning exposed to the Operator until the Operator accepts its representation as sufficient for the current governed use, or explicitly report that sufficient understanding has not been achieved.

## Formal statement

Let \(G\) be the set of governed meanings, \(O\) the Operator, \(T\) the set of governed uses, and \(R_A(g,O,t)\) the representations produced by applicable adaptation attempts for meaning \(g\) and use \(t\).

\[
\forall g\in G,\forall t\in T:\operatorname{ExposedTo}(g,O,t)\Rightarrow\operatorname{AcceptedAsSufficient}(O,\operatorname{InitialRepresentation}(g,O,t),t)\lor\bigl(\exists r\in R_A(g,O,t):\operatorname{AcceptedAsSufficient}(O,r,t)\bigr)\lor\bigl(\operatorname{ApplicableAdaptationExhaustedOrDeclined}(g,O,t)\land\operatorname{ExplicitComprehensionGap}(g,O,t)\bigr)
\]
