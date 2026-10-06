---
atom_id: CA-E-246
cce_version: cce_1
cce_form: evaluation
subjects:
  - subject
  - evaluation
  - atom-boundary
version: 1
updated_at: 2026-08-23 01:44:00
relations:
  evaluation_for:
    - CA-R-1013
    - CA-R-1014
    - CA-M-125
    - CA-M-126
    - CA-R-1015
---
# Validate Atom Subjects

## Claim checked

Every active or draft Atom declares queryable Subjects without using those Subjects as Scope coordinates or independent vocabulary authority.

## Test case

Create Atoms with one Subject, multiple Subjects, a missing `subjects` property, an empty `subjects` property, an invalid Subject term, a legacy `subject_scopes` property, and a Subject Projection that adds an undeclared Subject.

## Acceptance criteria

Every valid Atom passes. Every invalid Atom fails. The Subject Projection contains exactly the distinct Subjects declared by the selected Atoms.

## Failure disposition

Record a Concern naming each affected Atom and Subject.
