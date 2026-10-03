---
atom_id: CA-E-246
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - Atom/Subjects
  depends_on:
    continuant:
      - "Atom"
      - "Subject"
      - "Subject Path"
      - "Subject/Relation Kind"
      - "Subject/Temporal Form"
      - "Entity"
      - "Term"
      - "Subject Projection"
      - "Concern"
      - "Atom/Claim"
      - "Atom/Content Role: Evaluation"
      - "Evaluation For Relation"
version: 11
updated_at: "2026-09-11 22:54:39 +0400"
relations:
  evaluation_for:
    - CA-R-1275
    - CA-R-1279
    - CA-M-125
    - CA-R-1018
---
# Validate Atom Subjects

## Claim checked

**every** Atom has valid Subjects that connect the Atom to independent Entity references.

## Test case

create fixtures for **all** Relation Kinds, **all** Temporal Forms, **`=1`** GOVERNS Subject, **`>=0`** DEPENDS_ON Subjects, a definition Claim, **and** a prerequisite Entity. **then** introduce a stored **or** owned referenced Entity, a missing Relation Kind, multiple Relation Kinds, a missing Temporal Form, multiple Temporal Forms, zero GOVERNS Subjects, multiple GOVERNS Subjects, a definition whose GOVERNS Subject references the wrong Entity **or** omits its defined Term, an omitted prerequisite Entity, a Term's wording substituted for a Subject connection, a duplicate Subject, **and** a Subject Projection that changes **or** adds a Subject.

add a conformance-check Evaluation fixture whose checked Entity persists through time **and** whose GOVERNS Subject has Temporal Form CONTINUANT, **and** another whose checked Entity unfolds through time **and** whose GOVERNS Subject has Temporal Form OCCURRENT. resolve their checked authority separately through `evaluation_for` under CA-R-1018. introduce variants that substitute a generic Evaluation label **or** the execution of the check for the checked Entity, derive Temporal Form from Content Role alone, **or** confuse the checked-authority Atom references with the Entity referenced by GOVERNS. a missing **or** invalid `evaluation_for` target **must** also fail its applicable check.

## Acceptance criteria

**every** valid fixture passes. **every** invalid fixture fails with the affected Atom, Subject Path, Relation Kind, Temporal Form, Entity reference, **or** cardinality rule. the Subject Projection reproduces exactly the selected current Subjects **without** independent authority.

## Failure disposition

record a Concern naming **every** affected Atom **and** Subject.
