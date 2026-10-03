---
subject_scopes:
  - scope-topology
version: 3
updated_at: 2026-08-22 01:56:15
relations:
  child_of:
    - CA-E-001-PRINCIPLE-EVALUATION--make-accepted-requirements-checkable
    - CA-E-206-EVAL_APPROACH--require-usable-inputs-for-reliance
  evaluation_for:
    - CA-R-886-REQUIREMENT-BSEED_SEMANTICS--resolve-scope-unit-references-relative-to-the-owning-scope
    - CAPRMEDIO-GOV-REQU-326--encode-relations-as-relation-kind-maps
---
# Validate relative Scope Unit references

## Claim checked

Every machine-readable Scope Unit reference resolves deterministically from the source Atom's owning Scope Unit through the admitted relative grammar.

## Test case

Create one current Scope Unit with a named descendant and a named sibling. Resolve `.`, `./<FULL DESCENDANT NAME>`, and `../<FULL SIBLING NAME>` from both a relation target and a `relational_endpoints` descriptor. Then try an unknown name, an ambiguous descendant name, a sibling through `./`, a descendant through `../`, a registered short prefix in place of the full name, the retired `scope_unit:<prefix>` form, and an unregistered relative form. Scan Atom prose and structured properties for abbreviated current Scope Unit mentions outside identifiers, governed compact addresses, and explicitly preserved historical evidence.

## Acceptance criteria

Each valid reference resolves to exactly one expected Scope Unit. Every invalid or ambiguous reference fails and identifies the source owner, supplied token, permitted structural position, and unresolved or conflicting candidates. Any abbreviated Scope Unit mention inside Atom meaning fails.

## Failure disposition

Record a Concern naming the invalid reference and stop acceptance of the relation that contains it.
