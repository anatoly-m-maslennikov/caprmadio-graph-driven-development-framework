---
subjects:
  - relation-model
  - atom-boundary
version: 6
updated_at: 2026-08-23 01:44:00
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
    - CAPRMEDIO-META-REQU-117--store-each-semantic-relation-once
    - CAPRMEDIO-META-REQU-121--store-only-direct-semantic-relations
---
# Register complete relation-kind metadata

GOVERNANCE must expose exactly one canonical machine-readable Atom relation-type dictionary with one row per admitted declared relation. Each row declares the relation family, ordering domain, declared name, inverse-derived name, declaration carrier, declared target position, inverse target position, allowed source and target lifecycle states and classes, declaration owner, cardinality, authority effect, transitivity, applicable authority modes, status, and exclusive meaning.

Each relation's `declaration_carrier` is either `atom_carrier` or `work_journal_event`; the direct edge may be persisted only in that carrier. Atom carriers and authoritative Journal events may use only declared names. Every inverse relation is derived and must never be stored. Declared and inverse-derived names are unique, each declared name maps to exactly one inverse-derived name, applying the inverse mapping twice returns the original kind, paired target positions are opposite within one ordering domain, and missing, duplicate, or ambiguous metadata makes the relation unavailable to deterministic Tools.
