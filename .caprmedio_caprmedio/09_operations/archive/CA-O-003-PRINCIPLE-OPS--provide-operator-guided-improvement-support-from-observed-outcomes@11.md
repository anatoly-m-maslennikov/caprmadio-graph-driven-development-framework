---
subject_scopes:
  - principles
version: 11
updated_at: 2026-08-21 07:29:53
relations:
  child_of:
    - CA-INTENT
---
# Provide Operator-guided improvement support from observed outcomes

CAPRMEDIO must provide the Operator with support for turning material observed project outcomes into evaluated improvement proposals for the narrowest affected scope within the Operator's current authority.

## Formal statement

Let \(Y_m\) be the set of material observed project outcomes, \(O\) the Operator, and \(A_O\) the Operator's current authority. For each \(y\in Y_m\), let \(p_y\) be a candidate improvement proposal and \(s_y\) its narrowest affected scope.

\[
\forall y\in Y_m:
\operatorname{Scope}(p_y)=s_y
\land
\operatorname{NarrowestAffectedScope}(s_y,y)
\land
\operatorname{WithinAuthority}(p_y,A_O)
\land
\operatorname{CanSupport}\bigl(\operatorname{CAPRMEDIO},O,\operatorname{ProduceAndEvaluate}(p_y)\bigr)
\]
