---
subjects:
  declared:
    occurrent:
      - subject-assignment
  prerequisite:
    continuant:
      - subject
      - subject-path
      - claim-subject-relation
      - subject-temporal-form
      - atom-boundary
cce_version: cce_1
cce_form: method
version: 3
updated_at: 2026-08-25 01:32:22
relations: {}
---
# Assign Qualified Subject Paths from the Claim

to assign an Atom's Subjects, the Author must perform all of:

1. select the narrowest semantic locus that the Claim governs or depends on.
2. construct one Subject Path from its Base Entity through every identity-bearing Dependent Entity to that semantic locus.
3. compare each Term used as a Dependent Entity in the constructed Subject Path with its occurrences in all other Subject Paths and reject the path when that Term occupies a different ordinal position after the Base Entity.
4. use `Atom/Content Role/Spec Content Roles/Status` when the Claim governs the Status shared by Atoms whose Content Role is in Spec Content Roles.
5. use `Atom/Content Role/Spec Content Roles/Status/Draft` when the Claim establishes Draft or an entry criterion or exit criterion for Draft within that Status model.
6. do not append `Entry Criterion` or `Exit Criterion` unless the Claim governs that criterion as a Dependent Entity with its own identity.
7. classify the Subject as GOVERNS when the Claim establishes authority about it or as DEPENDS_ON when the Claim requires it without establishing authority about it.
8. classify the Subject Temporal Form from the terminal entity of the Subject Path.
9. introduce at least one and at most two GOVERNS Subjects with at most one Subject under each Subject Temporal Form.
10. split the Atom before assignment when its Claim contains more than one independently replaceable GOVERNS Subject with the same Subject Temporal Form.
11. record each distinct Subject Path exactly once under its matching Claim-Subject Relation and Subject Temporal Form.
