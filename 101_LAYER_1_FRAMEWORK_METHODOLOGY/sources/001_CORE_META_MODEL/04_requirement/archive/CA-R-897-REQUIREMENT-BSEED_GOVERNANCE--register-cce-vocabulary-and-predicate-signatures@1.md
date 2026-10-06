---
subject_scopes:
  - language
relations:
  child_of:
    - CA-R-892
    - CA-R-894
    - CAPRMEDIO-META-REQU-126--govern-canonical-scoped-vocabulary
    - CAPRMEDIO-META-REQU-121--store-only-direct-semantic-relations
version: 1
updated_at: 2026-08-22 02:53:47
---
# Register CCE vocabulary and predicate signatures

Each CCE content term must be registered by its one active meaning-owning Atom through one `cce_terms` entry. A term entry must contain `token`, `lexical_kind`, and `denotes_kind`. `lexical_kind` must be `common_noun`, `proper_name`, or `individual_reference`. The entry's carrier is its meaning owner; an alias may resolve to the token for Translation but must not occur in a CCE Claim.

Each CCE predicate phrase must be registered by its one active meaning-owning Atom through one `cce_predicates` entry. A predicate entry must contain `phrase`, `arity`, `direction`, `world_assumption`, and an ordered nonempty `participant_slots` list. Every participant slot must contain `slot_name`, `value_kind`, `cardinality`, and `reference_mode`. `reference_mode` must be `by_value` or one registered reference kind. The declared arity must equal the number of participant slots.

A direct relational predicate must use `direction: direct`. Its optional `inverse_predicate` names only a registered derived reading and must not create a second stored relation. `world_assumption` defaults to `open`; `closed` additionally requires `exhaustive_source` and `completeness_evaluation` references. A non-relational predicate uses `direction: not_applicable`.

The CCE vocabulary registry is a deterministic Projection of all active `cce_terms` and `cce_predicates` entries plus the function vocabulary owned by the selected CCE version. Duplicate tokens, duplicate predicate phrases, overlapping case-folded spellings, missing owners, unknown kinds, invalid slot cardinality, arity mismatch, inverse cycles, and incomplete closed-world declarations invalidate the registry.

An active CCE Claim may use only the active registry. A draft CCE Claim may additionally use explicitly related draft candidate entries, but those entries remain outside active interpretation and must be reported as candidate dependencies. No parser may infer an entry from ordinary prose, a filename, capitalization, grammatical position, or similarity to a registered spelling.
