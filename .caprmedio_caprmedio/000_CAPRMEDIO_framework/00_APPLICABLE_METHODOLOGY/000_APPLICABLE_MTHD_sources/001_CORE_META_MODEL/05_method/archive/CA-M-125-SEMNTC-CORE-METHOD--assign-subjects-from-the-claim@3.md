---
cce_version: cce_1
cce_form: method
subjects:
  declared:
    continuant:
      - subject
      - semantics
      - atom-boundary
version: 3
updated_at: 2026-08-23 14:53:58
relations:
  child_of:
    - CA-R-1012
    - CA-R-1013
    - CA-R-1090
---
# Assign Subjects from the Claim

TO assign an Atom's Subjects, the Author MUST PERFORM ALL OF:

1. Select only concepts, entities, conditions, or processes that participate in the Atom's Claim.
2. Classify each Subject as declared when the Claim establishes authority about it or as prerequisite when the Claim requires it before the Claim applies or its governed action may proceed without establishing authority about it.
3. Classify each Subject as continuant when it exists through time or as occurrent when it happens or unfolds through time.
4. Use the exact canonical reference for an identified governed entity and a lowercase kebab-case term for any other Subject.
5. Declare each distinct Subject exactly once under its matching Claim Role and Claim Participant Temporal Form.
