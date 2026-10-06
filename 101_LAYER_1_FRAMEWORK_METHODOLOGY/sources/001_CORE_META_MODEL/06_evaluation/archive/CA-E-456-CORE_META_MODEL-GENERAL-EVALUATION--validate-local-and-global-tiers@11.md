---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Atom Tier Validation
  depends_on:
    - Atom/Global Tier
    - Atom/Local Tier
    - Atom/Scope
    - Scope Unit
    - Project
version: 11
updated_at: "2026-09-22 23:02:20 +0000"
relations: {"evaluation_for": ["CA-R-155", "CA-R-680", "CA-R-1442", "CA-R-1443", "CA-R-1389", "CA-R-1390", "CA-R-1391", "CA-R-1392", "CA-D-285", "CA-R-1566", "CA-R-1573"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Validate Local and Global Tiers

## Claim

the Evaluation **must** reject an Atom **if** **any** following condition holds:

- its Local Tier cardinality **or** admitted value violates CA-R-155, CA-R-680, CA-R-1442, the applicable Project Goal exception, **or** an applicable Goal, Type, **or** CAPO/I Standard restriction under CA-R-1566.
- its Global Tier violates the Project **or** recursive structural mapping.
- its Principle tier lies outside the Project under CA-R-1443.
- its non-Project Goal is **not** a Standard Atom of its direct parent Scope Unit.
- its ownership **or** structural ancestry is unresolved.
- its complete Claim fails the applicable Local Tier definition **and** the evidence procedure governed by CA-M-272.
- its classification is unresolved **or** inferred from breadth, an old label, source ownership, importance, **or** reuse alone; applying the explicit CAPO/I Standard rule is required **and** is **not** unsupported role-based inference.
- a tier-parent edge is based on the value defined by an Atom rather than that Atom's own admitted tier.
- governance from Global Tier `N` **to** **any** greater Global Tier **in** the Scope Unit is omitted because of a different Content Role, a different Subject, a non-adjacent tier, **or** an unoccupied intermediate tier, contrary **to** CA-R-1573.

validate the internally carried Local Tier **and** Global Tier against the applicable mapping; a filename alone is **not** their source. filename interpretation follows CA-D-285: recognize the external Project Goal's tierless grammar **before** applying the ordinary omitted-Standard default. an incorrect tier inferred by ignoring that exception **must** fail this Evaluation.
