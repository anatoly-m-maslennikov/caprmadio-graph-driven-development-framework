---
subject_scopes:
  - artifact-catalog
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-REQU-461--four-character-type-prefix-identities
  - type: child_of
    targets:
      - CAPRMEDIO-GOV-REQU-467--register-atom-types-by-role-and-locus
      - CAPRMEDIO-GOV-REQU-313--govern-catalog-map-and-hub-projections
  - type: relates_to
    targets:
      - CAPRMEDIO-GOV-REQU-456--separate-route-catalog-and-project-whitelist
      - CAPRMEDIO-GOV-REQU-303--optional-project-prefix
      - CAPRMEDIO-GOV-REQU-304--expandable-scope-path-identities
---

# Requirement — Register Atom and Projection Type prefixes

Every registered artifact Type has exactly one globally unique, immutable, four-character uppercase identity prefix. The artifact catalog owns the mapping. Frontmatter keeps the full semantic `artifact_type`; the short prefix is an identity token and never replaces the Type name.

The canonical filename grammar is:

```text
<PROJECT>-<SCOPE_PATH>-<TYPE_PREFIX>-<NNN>[-<SUBTYPE>]--<SUMMARY>.<ext>
```

Project-prefix and scope-path segments follow the project’s governed identity settings. Omitted optional segments do not leave empty separators. The stable artifact ID ends at `<NNN>`. A subtype segment is semantic filename metadata but is not part of the stable ID. The `--` token separates identity metadata from the human-readable summary.

Numbering is one monotonically increasing sequence per registered Type across all of its subtypes.

## Canonical prefix registry

| Type | Prefix |
|---|---|
| `concern` | `CONC` |
| `external_problem` | `XPRB` |
| `conflict` | `CNFL` |
| `analysis` | `ANAL` |
| `external_analysis_report` | `XARP` |
| `conflict_analysis` | `CFAN` |
| `requirement` | `REQU` |
| `constraint` | `CNST` |
| `contract` | `CNTR` |
| `method` | `METH` |
| `implementation_methodology` | `IMET` |
| `integration_decision` | `IDEC` |
| `evaluation` | `EVAL` |
| `evaluation_standard` | `AUST` |
| `review_protocol` | `RVPR` |
| `implementation` | `IMPL` |
| `external_git_commit` | `XGCM` |
| `pull_request` | `PULL` |
| `observation` | `OBSV` |
| `external_evidence_record` | `XEVR` |
| `verification_record` | `VERC` |
| `catalog` | `CATL` |
| `map` | `MAPS` |
| `hub` | `HUBS` |

Examples:

```text
CAPRMEDIO-GOV-REQU-001--artifact-form-is-explicit.md
CAPRMEDIO-GOV-EVAL-002-QA-CASE--projection-interpretability.md
CAPRMEDIO-OPS-EVAL-003-EVALUATION-CONTROL--queue-stall-detection.md
CAPRMEDIO-TOOL-IMPL-001--resolve-project-local-governance.md
CAPRMEDIO-META-CATL-001--requirement-atom-catalog.md
```

Changing a registered prefix requires one governed, complete identity migration across active and archived carriers, relations, Projections, implementations, and evaluation records. The newly admitted registry establishes the target vocabulary; it does not silently rename existing carriers.

## Primary claim

GOV assigns one unique four-character identity prefix to every registered Atom and Projection Type.

## Rationale

The predecessor’s prefix registry encoded superseded internal Types and the retired Specification Type. The successor aligns identities with role-equals-Type internal Atoms and the Catalog, Map, and Hub Projection vocabulary while preserving compact deterministic filenames.
