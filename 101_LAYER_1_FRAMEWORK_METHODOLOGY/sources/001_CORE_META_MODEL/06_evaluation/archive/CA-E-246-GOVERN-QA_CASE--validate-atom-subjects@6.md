---
atom_id: CA-E-246
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Claim-Subject Relation Validation
  depends_on:
    continuant:
      - Claim-Subject Relation
      - Subject
      - Subject Path
version: 6
updated_at: 2026-08-29 01:16:37 +0400
relations: {}
---
# Validate Claim-Subject Relations

## Claim checked

**every** active **or** draft Atom has valid Claim-Subject Relations to independent Subject Entities.

## Test case

create fixtures for **all** Kinds, **all** Temporal Forms, one GOVERNS relation, two GOVERNS relations with different Temporal Forms, **any** number of DEPENDS_ON relations, a definition Claim, **and** a prerequisite Subject. **then** introduce a stored **or** owned Subject, a missing Kind, multiple Kinds, a missing Temporal Form, multiple Temporal Forms, zero GOVERNS relations, two GOVERNS relations with one Temporal Form, an omitted defined Term, an omitted prerequisite Subject, a duplicate relation, **and** a Subject Projection that changes **or** adds a relation.

## Acceptance criteria

**every** valid fixture passes. **every** invalid fixture fails with the affected Atom, Subject Path, Kind, Temporal Form, **or** cardinality rule. the Subject Projection reproduces exactly the selected current Claim-Subject Relations **without** independent authority.

## Failure disposition

record a Concern naming **every** affected Atom **and** Claim-Subject Relation.
