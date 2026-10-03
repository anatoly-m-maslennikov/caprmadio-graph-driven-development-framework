---
subject_scope: artifact-model
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-META-REQU-250--internal-atom-types-equal-content-roles
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-248--three-artifact-forms
      - CAPRMEDIO-META-REQU-254--eight-content-roles-with-delivery-and-ops
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-258--derive-artifact-coordinates-from-registered-types
      - CAPRMEDIO-META-REQU-260--one-independently-replaceable-claim-per-atom
---

# Requirement — Derive internal Atom Types from eight Content roles

For every governed artifact whose Artifact form is `atom` and Governance locus is `internal`, the canonical `artifact_type` name equals its `content_role` value:

```text
atom × concern × internal        → concern
atom × analysis × internal       → analysis
atom × requirement × internal    → requirement
atom × method × internal         → method
atom × evaluation × internal      → evaluation
atom × delivery × internal       → delivery
atom × implementation × internal → implementation
atom × ops × internal            → ops
```

The equality is exact in canonical machine-readable vocabulary. A direct subtype may refine an internal Atom Type but cannot replace, rename, or introduce another top-level Type for the same Content role.

Stable naming patterns may distinguish recurring domain claims before GOV admits formal subtypes. For example, entity definitions, lifecycle states, status entry criteria, status exit criteria, transition routes, invariants, and events may remain Requirement atoms identified through summaries, relations, and subject scope. A later subtype admission must preserve their top-level `requirement` Type.

This derivation is a META invariant because every conforming CAPRMEDIO project can compute it without project policy. GOV owns external and relational Atom Type names, direct subtype vocabularies, identity prefixes, carriers and paths, catalogs and whitelists, schemas and validation, and migrations.

## Primary claim

The canonical Type name of every internal Atom is exactly its Content role name.

## Rationale

The direct equality makes the most common atomic vocabulary predictable and removes a redundant internal naming layer. The pattern applies uniformly to all eight CAPRMEDIO roles.
