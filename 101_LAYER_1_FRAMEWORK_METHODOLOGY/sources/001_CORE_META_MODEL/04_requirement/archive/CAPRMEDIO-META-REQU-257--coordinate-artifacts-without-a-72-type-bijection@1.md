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
      - CAPRMEDIO-META-REQU-251--coordinate-artifacts-without-a-63-type-bijection
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-248--three-artifact-forms
      - CAPRMEDIO-META-REQU-254--eight-content-roles-with-delivery-and-ops
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-258--derive-artifact-coordinates-from-registered-types
      - CAPRMEDIO-META-REQU-084--relational-artifacts-declare-endpoints
      - CAPRMEDIO-META-REQU-098--scope-path-does-not-change-semantic-coordinates
      - CAPRMEDIO-META-REQU-256--internal-atom-types-equal-eight-content-roles
---

# Requirement — Coordinate artifacts without a 72-Type bijection

Every governed artifact occupies exactly one semantic coordinate:

```text
Artifact form × Content role × Governance locus
```

`scope_path` remains an independent structural ownership coordinate. Direct subtype, carrier format, creation procedure, change procedure, priority, lifecycle condition, and source provenance remain qualifying properties rather than additional primary axes.

The Cartesian product of three Artifact forms, eight Content roles, and three Governance loci describes 72 possible coordinates. It is a classification space, not a mandate to invent 72 distinct top-level Type names or enable every coordinate in every project.

META derives Type names only where a universal invariant exists, including the internal Atom rule. GOV may register additional form-local Types and direct subtypes and admit or reject coordinates. A top-level Type may recur across coordinates only when distinct direct subtypes make every registered type pair resolve to exactly one coordinate.

Writers and validators resolve Artifact form, Content role, and Governance locus from the complete registered type pair. They must never infer a coordinate from the top-level Type alone when that Type recurs. An unknown, disabled, contradictory, or ambiguous pair fails closed.

## Primary claim

Artifact form, Content role, and Governance locus define an explicit classification space without requiring a one-to-one catalog of 72 distinct Type names.

## Rationale

Unique registered type-pair mappings preserve the orthogonal model while allowing predictable internal Atom names and reusable top-level vocabulary without artificial Type names for every cell.
