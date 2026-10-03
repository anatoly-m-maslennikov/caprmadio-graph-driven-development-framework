---
subject_scopes:
  - principles
version: 7
updated_at: 2026-08-21 07:29:53
relations:
  child_of:
    - CA-INTENT
---
# Provide project operation without specialist craft work

CAPRMEDIO must enable the Operator to create, deliver, run, and maintain a feasible project without requiring its human participants to acquire or personally perform the project's specialist craft work.

## Formal statement

Let \(F\) be the set of feasible projects, \(O\) the Operator, \(H(O)\) the Operator's human participants, and \(L=\{\operatorname{create},\operatorname{deliver},\operatorname{run},\operatorname{maintain}\}\) the governed project lifecycle capabilities.

\[
\forall p\in F:
\bigl(\forall l\in L:\operatorname{CanObtain}(O,l,p)\bigr)
\land
\bigl(\forall h\in H(O):\neg\operatorname{RequiresPersonalSpecialistCraft}(h,p)\bigr)
\]
