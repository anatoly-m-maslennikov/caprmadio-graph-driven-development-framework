---
atom_id: CA-R-819
subject_scopes:
  - principles
version: 8
updated_at: 2026-09-05 00:48:29 +0400
relations:
  child_of:
    - CA-INTENT
---
# Build what you want without requiring proficiency in the craft

CAPRMEDIO must enable the Operator to create, deliver, run, and maintain a feasible project without requiring its human participants to acquire or personally perform the project's specialist craft work.

## Formal statement

Let \(F\) be the set of feasible projects, \(O\) the Operator, \(H(O)\) the Operator's human participants, and \(L=\{\operatorname{create},\operatorname{deliver},\operatorname{run},\operatorname{maintain}\}\) the governed project lifecycle capabilities.

\[
\forall p\in F:
\bigl(\forall l\in L:\operatorname{CanObtain}(O,l,p)\bigr)
\land
\bigl(\forall h\in H(O):\neg\operatorname{RequiresPersonalSpecialistCraft}(h,p)\bigr)
\]
