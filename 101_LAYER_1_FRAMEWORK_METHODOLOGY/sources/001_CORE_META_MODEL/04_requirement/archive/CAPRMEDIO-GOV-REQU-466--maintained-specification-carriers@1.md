---
subject_scopes:
  - carrier-format
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-247--thin-maintained-specifications
  - type: relates_to
    targets:
      - CAPRMEDIO-GOV-REQU-456--separate-route-catalog-and-project-whitelist
      - CAPRMEDIO-GOV-REQU-306--job-based-carrier-policy
      - CAPRMEDIO-GOV-REQU-461--four-character-type-prefix-identities
      - CAPRMEDIO-GOV-REQU-309--revision-bound-parent-child-commit-messages
---

# Requirement — Govern maintained Specification carriers

`specification` is the internal, maintained, Definition-role artifact Type for
thin semantic views enabled by META. Its four-character identity prefix is
`SPEC`.

A Specification uses Markdown with YAML frontmatter and lives directly in its
owning structural scope rather than in an Atomic Artifact Type folder. Its
canonical filename is:

```text
<PROJECT>-<SCOPE_PATH>-SPEC-<NNN>--<SUMMARY>.md
```

The stable Specification identity ends at `<NNN>`. Numbering follows the
Type-owned sequence. Supported direct subtypes are `domain_model`, `behavior`,
`architecture`, `design`, and `governance`; subtype remains frontmatter
classification and is omitted from the default filename.

Frontmatter contains only applicable non-derived properties:

```yaml
---
artifact_type: specification
artifact_subtype: domain_model
artifact_id: CAPRMEDIO-META-SPEC-001
scope_path: layer:meta
priority: high
---
```

The body names Atomic Artifact IDs directly at every represented semantic
claim. Exact source revisions are carried by the governed Git transaction that
creates or updates the Specification; paths and links to other maintained
views are navigation only.

Creation and every update require a Git commit. The Specification ID is listed
as a new or updated child as applicable. Git history owns its revisions, so
`commit_on_create` and `commit_on_update` are invariants rather than
operator-selectable settings.

A Specification is current when its latest committed revision represents every
applicable source revision required by its scope. A changed source makes it
subject to lineage-impact review. `compatible` preserves the current
Specification revision; any affected disposition blocks a gate requiring that
Specification until an updated revision is committed. No frontmatter status
duplicates this derived condition.

## Primary claim

Specification is a maintained Markdown Type with stable `SPEC` identity,
scope-root placement, direct atomic provenance, and Git-governed revisions.

## Rationale

A concrete carrier contract makes the newly enabled semantic view usable
without treating it as an atom, hiding source revisions in frontmatter, or
creating a second currentness authority.
