---
subjects:
  declared:
    occurrent:
      - subject-validation
  prerequisite:
    continuant:
      - subject
      - subject-path
      - claim-subject-relation
      - subject-temporal-form
      - atom-boundary
    occurrent:
      - evaluation
cce_version: cce_1
cce_form: evaluation
version: 4
updated_at: 2026-08-25 01:32:22
relations: {}
---
# Validate Qualified Atom Subjects

## Claim checked

**every** active **or** draft Atom identifies each Subject by one exact Subject Path, classifies each Subject by one Claim-Subject Relation **and** one Subject Temporal Form, **and** keeps Subject identity independent of Current Scope **and** Claim Scope.

## Test case

create valid fixtures for `Atom`, `Atom/Content Role`, `Atom/Content Role/Spec Content Roles`, `Atom/Content Role/Spec Content Roles/Status`, `Atom/Content Role/Spec Content Roles/Status/Draft`, `Task/Definition of Done`, `Something1/Status/Draft`, `Something2/State/Draft`, a Property borne by a Base Entity, a Property borne by a Dependent Entity, both Claim-Subject Relations, both Subject Temporal Forms, **and** both permitted GOVERNS Temporal Forms in one Atom. define one Draft entry criterion **and** one Draft exit criterion with GOVERNS Subject Path `Atom/Content Role/Spec Content Roles/Status/Draft`. then introduce `Something1/Draft` together with `Something2/Status/Draft` so that Draft occupies two Subject Path positions, introduce `Atom/Status` as a path that skips the required bearer chain, a path that starts with a Dependent Entity, an empty segment, a leading **or** trailing `/`, an Entity Term containing `/`, an arbitrary graph relation encoded with `/`, a path that ends above the governed semantic locus, a criterion name appended without independent identity, zero GOVERNS Subjects, two GOVERNS CONTINUANT Subjects, two GOVERNS OCCURRENT Subjects, an invalid axis key, a duplicate Subject Path, **and** a Subject Projection that changes one classification **or** path.

## Acceptance criteria

**every** valid fixture passes. **every** invalid fixture fails with the violated Entity-name, Dependent-Entity Term position, Subject Path, Claim-Subject Relation, Subject Temporal Form, cardinality, **or** projection rule identified. the Draft entry-criterion **and** exit-criterion fixtures both resolve to `Atom/Content Role/Spec Content Roles/Status/Draft`.

## Failure disposition

record a Concern naming each affected Atom **and** Subject Path.
