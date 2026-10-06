---
subject_scopes:
  - artifact-catalog
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: relates_to
    targets:
      - CAPRMEDIO-GOV-REQU-456--separate-route-catalog-and-project-whitelist
      - CAPRMEDIO-GOV-REQU-303--optional-project-prefix
      - CAPRMEDIO-GOV-REQU-304--expandable-scope-path-identities
      - CAPRMEDIO-GOV-REQU-460--canonical-role-locus-types-and-qa-cases
---

# Requirement — Use four-character Type prefixes in artifact identities

Every registered artifact Type has exactly one globally unique, immutable,
four-character uppercase identity prefix. The artifact catalog owns the
mapping. Frontmatter keeps the full semantic `artifact_type`; the short prefix
is an identity token and never replaces the semantic name.

The canonical filename grammar is:

```text
<PROJECT>-<SCOPE_PATH>-<TYPE_PREFIX>-<NNN>[-<SUBTYPE>]--<SUMMARY>.<ext>
```

Project-prefix and scope-path segments follow the project’s governed identity
settings. Omitted optional segments do not leave empty separators.

The stable artifact ID ends at `<NNN>`. A subtype segment is semantic filename
metadata but is not part of the stable ID. The `--` token unambiguously
separates identity metadata from the human-readable summary. Correcting a
summary does not change artifact identity.

Numbering is one monotonically increasing sequence per registered Type across
all of its subtypes. A Type that requires a subtype, including QA Case, must
include the canonical subtype segment in its filename. Other Types omit the
segment when no subtype applies.

## Canonical prefix registry

| Type | Prefix |
|---|---|
| Problem | `PROB` |
| External Problem | `XPRB` |
| Conflict | `CNFL` |
| Analysis Report | `ANRP` |
| External Analysis Report | `XARP` |
| Conflict Analysis | `CFAN` |
| Requirement | `REQU` |
| Constraint | `CNST` |
| Contract | `CNTR` |
| Technical Decision | `TDEC` |
| Implementation Methodology | `IMET` |
| Integration Decision | `IDEC` |
| QA Case | `QACS` |
| Evaluation Standard | `AUST` |
| Review Protocol | `RVPR` |
| Git Commit | `GCOM` |
| External Git Commit | `XGCM` |
| Pull Request | `PULL` |
| Evidence Record | `EVRC` |
| External Evidence Record | `XEVR` |
| Verification Record | `VERC` |
| Specification | `SPEC` |

## Examples

```text
CAPRMEDIO-GOV-REQU-001--github-compatible-artifacts.md
CAPRMEDIO-GOV-QACS-002-EVAL-CASE--relation-interpretability.md
CAPRMEDIO-TOOL-TDEC-001--use-project-local-resolver.md
CAPRMEDIO-TOOL-IDEC-001--connect-cli-to-governance.md
CAPRMEDIO-GOV-EVRC-001--structural-validation-result.md
CAPRMEDIO-META-SPEC-001--atomic-artifact-domain.md
```

The corresponding stable IDs are `CAPRMEDIO-GOV-REQU-001`,
`CAPRMEDIO-GOV-QACS-002`, `CAPRMEDIO-TOOL-TDEC-001`, `CAPRMEDIO-TOOL-IDEC-001`, and
`CAPRMEDIO-GOV-EVRC-001`. The maintained Specification identity is
`CAPRMEDIO-META-SPEC-001`.

## Migration boundary

Changing a registered prefix requires one governed, complete identity
migration across active and archived carriers, relations, plans, generated
views, implementations, and proofs. A project cannot accept two current
prefixes for the same Type.

## Rationale

Fixed-width prefixes make identities compact and mechanically parseable while
remaining recognizable in file lists and relation targets. Placing subtype
after the sequence preserves one Type-owned number line and keeps the stable
identity independent of optional filename detail.
