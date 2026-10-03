---
subjects:
  - relation-model
  - atom-boundary
cce_version: cce_1
cce_form: obligation
version: 8
updated_at: 2026-08-23 11:39:04
relations:
  child_of:
    - CA-R-1054
    - CAPRMEDIO-META-REQU-117--store-each-semantic-relation-once
    - CAPRMEDIO-META-REQU-121--store-only-direct-semantic-relations
---
# Register complete relation-kind metadata

GOVERNANCE MUST expose exactly one canonical machine-readable Atom relation-type dictionary with one row per admitted declared relation. Each row MUST declare the relation family, ordering domain, declared name, inverse-derived name, declaration carrier, declared target position, inverse target position, allowed source and target lifecycle states and classes, declaration owner, cardinality, authority effect, transitivity, applicable authority modes, status, and exclusive meaning.

Each relation's `declaration_carrier` MUST equal `atom_carrier` or `work_journal_event`, and the direct edge MUST be persisted only in that carrier. Atom carriers and authoritative Journal events MUST use only declared names. Every inverse relation MUST be derived and MUST NOT be stored. Declared and inverse-derived names MUST be unique, each declared name MUST map to exactly one inverse-derived name, applying the inverse mapping twice MUST return the original kind, paired target positions MUST be opposite within one ordering domain, and missing, duplicate, or ambiguous metadata MUST make the relation unavailable to deterministic Tools.
