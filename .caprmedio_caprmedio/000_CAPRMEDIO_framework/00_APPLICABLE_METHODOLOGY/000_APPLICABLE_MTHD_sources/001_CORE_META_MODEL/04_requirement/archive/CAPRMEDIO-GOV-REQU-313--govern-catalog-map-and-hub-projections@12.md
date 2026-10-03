---
subjects:
  - carrier-format
project_graph_state:
  artifacts:
    enabled_types:
      - catalog
      - map
      - hub
version: 12
updated_at: 2026-08-23 11:39:04
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a01cb4-e15e-78d1-9084-766bf6b0cd63
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-466--maintained-specification-carriers
  child_of:
    - CA-R-1054
  relates_to:
    - CAPRMEDIO-GOV-REQU-385--resolve-artifact-routes-from-governed-authority-and-project-settings
    - CAPRMEDIO-GOV-REQU-306--job-based-carrier-policy
    - CAPRMEDIO-GOV-REQU-309--revision-bound-parent-child-commit-messages
---
# Govern Catalog, Map, and Hub Projections

GOVERNANCE registers these three internal navigation Projection Types:

| Projection Type | Permitted contribution |
|---|---|
| `catalog` | A selected inventory of source Atom IDs grouped and ordered by declared coordinates, scope, subject, entity, lifecycle state, or another governed key |
| `map` | A rendered correspondence or topology among already-governed source identities, relations, keys, or endpoints |
| `hub` | A navigation entry point to scoped Atoms, Catalogs, Maps, or other governed surfaces |

Catalog, Map, and Hub are Types within Artifact form `projection`; they are not Content roles or creation mechanisms. Each has exactly one Content role. Its Type and Content role therefore derive `projection × <role> × internal` without storing a duplicate coordinate. A role-specific Projection may link to artifacts of other roles for navigation but cannot absorb or restate their semantic claims.

A Projection uses the carrier selected for its governed job and has a stable governed identity. Narrative Projections use Markdown with YAML frontmatter; structured Maps may use standalone YAML; Project Scope Unit Graph Projections use TOML.

Markdown Projection filenames follow the registered Type-prefix grammar:

```text
<PROJECT>-<SCOPE_PATH>-<TYPE_PREFIX>-<NNN>--<SUMMARY>.md
```

Markdown frontmatter declares only applicable non-derived properties. Native structured Projection carriers encode only the metadata required by their registered job without duplicating coordinates derivable from canonical placement or identity. Blanket source-frontier inventories are prohibited; a Projection records only the explicit provenance or dependency references required to understand or rebuild its emitted values.

The body may contain headings, grouping and ordering labels, direct Atom IDs and links, Journal record identities and frontiers, source titles, and rendered governed relations. It must not introduce a normative paraphrase needed to understand or satisfy a source Atom. Any independently meaningful explanation, conclusion, Requirement, Method, Evaluation rule, Implementation claim, or Ops fact is emitted as its own Atom and then linked from the Projection.

A Projection may be generated programmatically or through LLM inference. These are generation procedures and provenance facts, not Artifact forms or authority; neither grants authority to the Projection. Creation and every rebuild are committed as new or updated children under the exact Atom revisions and Journal records consumed.

A Projection is current only when its registered rebuild and currentness rules reproduce the committed view. A change to an explicit dependency triggers lineage-impact review. A compatible result may preserve the existing Projection revision; an affected result requires a rebuild before a gate that requires the Projection may pass.

`specification` is not registered as an independent Projection Type. A current view of the distributed normative specification is represented by a Catalog, Map, Hub, or bounded combination whose Content role is `requirement`.

## Rationale

These three navigation Types preserve inventory, topology, and navigation without recreating a second prose specification. The view can be rebuilt whenever its source frontier changes, while each semantic claim remains governed by its owning Atom.
