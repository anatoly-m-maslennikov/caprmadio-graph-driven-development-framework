---
cce_version: cce_1
cce_form: method
subjects:
  declared:
    occurrent:
      - subject-assignment
  prerequisite:
    continuant:
      - subject
      - semantics
      - atom-boundary
version: 5
updated_at: 2026-08-23 15:25:04
relations:
  child_of:
    - CA-R-1012
    - CA-R-1013
    - CA-R-1090
    - CA-R-1091
    - CA-R-1092
---
# Assign Subjects from the Claim

TO assign an Atom's Subjects, the Author MUST PERFORM ALL OF:

1. Select only concepts, entities, conditions, or processes that participate in the Atom's Claim.
2. Classify each Subject as declared when the Claim establishes authority about it or as prerequisite when the Claim requires it before the Claim applies or its governed action may proceed without establishing authority about it.
3. Classify each Subject as continuant when it exists through time or as occurrent when it happens or unfolds through time.
4. IF no selected Subject has DECLARED Claim Role, THEN introduce at least one and at most two declared Subjects from the Claim's semantic nucleus with at most one Subject under each Claim Participant Temporal Form.
5. Keep at most one declared continuant Subject and at most one declared occurrent Subject in the Atom.
6. Split the Atom before assignment when its Claim contains more than one independently replaceable declared Subject with the same Claim Participant Temporal Form.
7. Use the exact canonical reference for an identified governed entity and a lowercase kebab-case term for any other Subject.
8. Declare each distinct Subject exactly once under its matching Claim Role and Claim Participant Temporal Form.
