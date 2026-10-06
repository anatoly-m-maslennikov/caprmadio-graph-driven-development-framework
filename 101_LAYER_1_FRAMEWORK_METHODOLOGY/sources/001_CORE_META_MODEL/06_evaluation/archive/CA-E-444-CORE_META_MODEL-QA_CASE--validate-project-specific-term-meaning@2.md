---
atom_id: CA-E-444
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Term/meaning validation"
  depends_on:
    - "Term"
    - "Project"
    - "Definition Atom"
    - "Atom/Claim"
    - "Atom"
    - "Subject"
    - "Entity"
    - "Subject Path"
    - "Terminology Projection"
    - "Concern"
    - "Action"
    - "Process"
version: 2
updated_at: "2026-09-13 02:05:21 +0400"
relations:
  evaluation_for:
    - CA-R-1318
    - CA-R-1319
    - CA-R-1320
    - CA-R-1275
    - CA-R-1279
    - CA-R-1321
    - CA-R-1194
    - CA-R-1325
    - CA-M-114
    - CA-M-125
---
# Validate Project-specific Term meaning

## Claim checked

a Term has a Project-specific meaning that remains consistent across **all** its uses, distinct from an Atom's direct Subject reference.

## Test case

create an active Definition Atom that gives a word **or** phrase a Project-specific meaning, **and** use that meaning consistently **in** several Claims. create an ordinary English word used consistently **without** a Project-specific definition. create a definition that merely repeats ordinary dictionary meaning, a Term used with conflicting Project-specific meanings, a Term's wording substituted for a direct Subject reference, **and** a complete composite Subject Path classified as a Term.

## Acceptance criteria

the consistently used Project-specific Term passes **and** resolves **to** its active Definition Atom. the ordinary word remains valid general language **without** being classified as a Term. consistent use, capitalization, **or** occurrence **in** a Subject Path alone does **not** establish a Term. a dictionary-only definition does **not** qualify for the Terminology Projection. conflicting meanings fail with the defining Atom **and** conflicting uses identified. a direct GOVERNS **or** DEPENDS_ON reference connects an Atom **to** its canonical Entity, Action, **or** Process target; substituting the Term's wording for a direct Subject reference **or** classifying a complete composite Subject Path as a Term fails. terminology entries retain their source references **without** independent authority.

## Failure disposition

record a Concern identifying the affected wording, defining Atom, conflicting use, direct Subject reference, **or** Terminology Projection entry.
