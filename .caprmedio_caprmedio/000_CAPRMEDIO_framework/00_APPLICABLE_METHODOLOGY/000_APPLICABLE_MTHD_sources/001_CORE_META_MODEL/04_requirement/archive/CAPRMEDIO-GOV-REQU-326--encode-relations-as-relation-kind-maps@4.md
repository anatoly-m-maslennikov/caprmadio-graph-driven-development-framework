---
subject_scopes:
  - relation-model
version: 4
updated_at: 2026-08-22 01:51:09
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-117--store-each-semantic-relation-once
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Relation-kind maps

Every Markdown Atom encodes `relations` as a mapping from each registered
relation kind to one non-empty list of unique project-graph node references:

```yaml
relations:
  child_of:
    - CAPRMEDIO-REQU-003--apply-dry-across-caprmedio
    - CAPRMEDIO-META-REQU-154--semantic-irreducibility
```

`relations` is omitted when empty. Each relation kind appears at most once;
relation-kind and target order have no semantic meaning. Unknown relation
kinds, duplicate targets, empty target lists, and the legacy `type` plus
`targets` wrapper are invalid after the governed migration cutover.

An Artifact target uses its canonical filename-derived reference. A Scope Unit
target is resolved relative to the source Atom's owning Scope Unit and uses the
exact registered full human-readable Scope Unit name:

- `.` references the current Scope Unit;
- `./<NAME>` references the one descendant named `<NAME>` inside the current
  Scope Unit's subtree;
- `../<NAME>` references the one sibling named `<NAME>`.

Names are matched exactly. A missing or ambiguous match, an unregistered
relative form, or the retired `scope_unit:<prefix>` form is invalid. A relation
kind's registered source and target classes determine which node partition
each reference may occupy. Legacy top-level `relation_kind` and `endpoints`
properties are invalid.

The same Scope Unit reference grammar applies to
`relational_endpoints.controller.scope_unit` and every
`relational_endpoints.followers[].scope_unit`. `relational_endpoints` is a
separate typed endpoint structure, not a relation-kind map.
