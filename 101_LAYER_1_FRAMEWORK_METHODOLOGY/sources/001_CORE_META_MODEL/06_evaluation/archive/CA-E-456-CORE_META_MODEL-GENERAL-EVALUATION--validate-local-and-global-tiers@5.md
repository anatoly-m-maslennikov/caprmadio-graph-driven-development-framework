---
atom_id: CA-E-456
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
version: 5
updated_at: "2026-09-15 06:32:56 +0400"
relations: {}
---
# Validate Local and Global Tiers

the Evaluation **must** reject an Atom **when** its Local Tier cardinality **or** admitted value violates CA-R-155, CA-R-680, CA-R-1442, **or** the applicable Project Goal exception, its Global Tier violates the Project **or** recursive structural mapping, its Principle tier lies outside the Project, its non-Project Goal is **not** a Standard Atom of its direct parent Scope Unit, its ownership **or** structural ancestry is unresolved, **or** its complete Claim fails the applicable Local Tier definition **and** the evidence procedure governed by CA-M-272. unresolved classification, classification inferred from breadth, an old label, source ownership, role, importance, **or** reuse alone, **and** a tier-parent edge based on the value defined by an Atom rather than that Atom's own admitted tier **must** fail.
