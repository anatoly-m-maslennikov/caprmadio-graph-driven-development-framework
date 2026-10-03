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
      - CAPRMEDIO-META-REQU-239--total-one-to-one-semantic-route-catalog
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-248--three-artifact-forms
      - CAPRMEDIO-META-REQU-249--seven-content-roles-and-three-governance-loci
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-211--type-derived-artifact-routes
      - CAPRMEDIO-META-REQU-084--relational-artifacts-declare-endpoints
      - CAPRMEDIO-META-REQU-227--scope-path-is-structural
      - CAPRMEDIO-META-REQU-250--internal-atom-types-equal-content-roles
---

# Requirement — Coordinate artifacts without a 63-Type bijection

Every governed artifact occupies exactly one semantic coordinate:

```text
Artifact form × Content role × Governance locus
```

`scope_path` remains an independent structural ownership coordinate. Direct subtype, carrier format, creation procedure, change procedure, priority, lifecycle condition, and source provenance remain qualifying properties rather than additional primary axes.

The Cartesian product of three Artifact forms, seven Content roles, and three Governance loci describes 63 possible coordinates. It is a classification space, not a mandate to invent 63 distinct top-level Type names or enable every coordinate in every project.

META derives Type names only where a universal invariant exists, including the internal Atom rule. GOV may register additional form-local Types and direct subtypes, admit or reject coordinates, and let one operational Type vocabulary recur across coordinates when the complete coordinate remains explicit and unambiguous.

Writers and validators must never infer Artifact form, Content role, or Governance locus solely from a Type name when the Type is valid at more than one coordinate. An unknown, disabled, contradictory, or ambiguous coordinate fails closed.

## Primary claim

Artifact form, Content role, and Governance locus define an explicit classification space without requiring a one-to-one catalog of 63 distinct Type names.

## Rationale

The predecessor made the semantic matrix depend on a globally bijective Type taxonomy. Explicit coordinates preserve the useful orthogonal model while allowing predictable internal Atom names and reusable Journal or Projection vocabularies without artificial names for every cell.
