---
subjects:
  declared:
    occurrent:
      - terminology-validation
  prerequisite:
    continuant:
      - terminology
      - subject-path
      - entity
    occurrent:
      - evaluation
cce_version: cce_1
cce_form: evaluation
version: 1
updated_at: 2026-08-25 01:20:06
relations: {}
---
# Validate Governed Term Entity Names

## Claim checked

**every** governed Term used as an Entity name excludes `/`, so **every** `/` in a Subject Path remains an unambiguous Entity-segment separator.

## Test case

create governed Terms without `/` **and** use them as Base Entity **and** Dependent Entity segments. then attempt to define Terms named `Atom/Status`, `/Status`, `Status/`, **and** `Atom//Status` **and** attempt to use each as one Subject Path segment.

## Acceptance criteria

**every** slash-free governed Term passes. **every** governed Term containing `/` fails before Subject Path construction, **and** no failed Term is emitted into a Terminology, Subject, **or** Term Entity Graph Projection.

## Failure disposition

record a Concern naming the affected Definition Atom **and** governed Term.
