---
subjects:
  declared:
    occurrent:
      - cce-operator-validation
  prerequisite:
    continuant:
      - cce-operator
      - terminology
      - unit-name
    occurrent:
      - evaluation
cce_version: cce_1
cce_form: evaluation
version: 1
updated_at: 2026-08-25 01:20:06
relations: {}
---
# Validate CCE Operator Identity and Unit Name Exclusion

## Claim checked

a Definition Atom **must not** redefine **any** CCE Operator, **and** a Unit Name **must not** equal the uppercase underscore-joined rendering of **any** word-form CCE Operator.

## Test case

attempt to define `means`, `if`, `then`, `must`, `every`, **and** one multiword CCE Operator as governed Terms. attempt to create Scope Units with Unit Names `MEANS`, `IF`, `THEN`, `MUST`, `EVERY`, **and** one uppercase underscore-joined multiword Operator rendering such as `NOT_IN`. create one conforming non-Operator Unit Name such as `MUST_TOOL`. attempt to use a symbolic CCE Operator as a Unit Name.

## Acceptance criteria

**every** attempted Operator redefinition fails, **every** word-form Operator Unit Name fails the CCE Operator exclusion, the symbolic Unit Name fails the Unit Name grammar, **and** the conforming non-Operator Unit Name passes.

## Failure disposition

record a Concern naming the conflicting Definition Atom, Unit Name, **or** CCE Operator.
