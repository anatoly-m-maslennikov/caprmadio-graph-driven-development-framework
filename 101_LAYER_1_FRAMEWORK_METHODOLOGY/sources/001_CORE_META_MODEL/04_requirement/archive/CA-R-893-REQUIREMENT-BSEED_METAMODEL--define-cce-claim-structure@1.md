---
subject_scopes:
  - language
relations:
  child_of:
    - CAPRMEDIO-META-REQU-132--define-role-specific-atom-atomicity
    - CAPRMEDIO-META-REQU-154--semantic-irreducibility
version: 1
updated_at: 2026-08-22 02:53:47
---
# Define CCE Claim structure

A CAPRMEDIO Controlled English (CCE) Claim must be one typed representation of one role-specific atomic meaning. The representation must contain exactly one CCE version identifier, exactly one statement-form identifier, exactly one primary semantic head, and every filling required by that statement form.

A statement form must declare its required and optional fillings, their admitted value kinds, their cardinalities, their canonical order, and whether each filling carries a term, predicate, participant reference, quantifier, modality, polarity, condition, Applicability boundary, ordered action, acceptance condition, or failure disposition. A filling must reference registered meaning rather than redefine it.

A CCE Claim may use several canonical sentences or ordered items only when its one statement form requires them to express the Atom's one independently replaceable role-specific unit. Human-readable explanations, filename Summaries, H1 titles, formulas, examples, evidence, and rendering syntax are not parts of the CCE Claim representation.
