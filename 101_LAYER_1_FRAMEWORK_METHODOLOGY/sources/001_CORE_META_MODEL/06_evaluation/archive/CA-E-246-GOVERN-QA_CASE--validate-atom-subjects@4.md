---
atom_id: CA-E-246
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    occurrent:
      - subject-validation
  prerequisite:
    continuant:
      - subject
      - atom-boundary
    occurrent:
      - evaluation
version: 4
updated_at: 2026-08-23 15:25:04
relations:
  evaluation_for:
    - CA-R-1013
    - CA-R-1014
    - CA-R-1084
    - CA-R-1085
    - CA-R-1086
    - CA-R-1087
    - CA-R-1088
    - CA-R-1089
    - CA-R-1090
    - CA-R-1091
    - CA-R-1092
    - CA-M-125
    - CA-M-126
    - CA-R-1015
---
# Validate Atom Subjects

## Claim checked

Every active or draft Atom declares at least one Subject, declares at most one continuant Subject and at most one occurrent Subject, classifies every Subject by exactly one Claim Role and one Claim Participant Temporal Form, and does not use Subjects as Scope coordinates or independent vocabulary authority.

## Test case

Create Atoms covering all four Claim-Role and Temporal-Form combinations, both permitted declared Temporal Forms in one Atom, zero declared Subjects with at least one prerequisite Subject, two declared continuants, two declared occurrents, a missing subjects property, an empty branch, an unknown axis key, a duplicate Subject reference, an invalid Subject reference, a legacy flat subjects sequence, a legacy subject_scopes property, and a Subject Projection that changes a Subject classification or adds an undeclared Subject.

## Acceptance criteria

Every valid Atom passes. Every Atom with zero declared Subjects fails and requires at least one new declared Subject derived from its Claim. Every Atom with more than one declared Subject under the same Claim Participant Temporal Form fails and requires an Atom split. Every other invalid Atom fails. The Subject Projection contains exactly the distinct Subjects declared by the selected Atoms under their source Claim Roles and Claim Participant Temporal Forms.

## Failure disposition

Record a Concern naming each affected Atom and Subject.
