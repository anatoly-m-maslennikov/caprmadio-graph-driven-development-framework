---
atom_id: CA-E-246
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Atom Subject Validation
  depends_on:
    continuant:
      - "Atom"
      - "Atom/Subjects"
      - "Subject"
      - "Subject Path"
      - "Subject/Relation Kind"
      - "Subject/Temporal Form"
      - "Entity"
      - "Term"
      - "Subject Projection"
      - "Concern"
version: 10
updated_at: "2026-09-09 02:44:46 +0400"
relations:
  evaluation_for:
    - CA-R-1275
    - CA-R-1279
    - CA-M-125
---
# Validate Atom Subjects

## Claim checked

**every** Atom has valid Subjects that connect the Atom to independent Entity references.

## Test case

create fixtures for **all** Relation Kinds, **all** Temporal Forms, **`=1`** GOVERNS Subject, **`>=0`** DEPENDS_ON Subjects, a definition Claim, **and** a prerequisite Entity. **then** introduce a stored **or** owned referenced Entity, a missing Relation Kind, multiple Relation Kinds, a missing Temporal Form, multiple Temporal Forms, zero GOVERNS Subjects, multiple GOVERNS Subjects, a definition whose GOVERNS Subject references the wrong Entity **or** omits its defined Term, an omitted prerequisite Entity, a Term's wording substituted for a Subject connection, a duplicate Subject, **and** a Subject Projection that changes **or** adds a Subject.

## Acceptance criteria

**every** valid fixture passes. **every** invalid fixture fails with the affected Atom, Subject Path, Relation Kind, Temporal Form, Entity reference, **or** cardinality rule. the Subject Projection reproduces exactly the selected current Subjects **without** independent authority.

## Failure disposition

record a Concern naming **every** affected Atom **and** Subject.
