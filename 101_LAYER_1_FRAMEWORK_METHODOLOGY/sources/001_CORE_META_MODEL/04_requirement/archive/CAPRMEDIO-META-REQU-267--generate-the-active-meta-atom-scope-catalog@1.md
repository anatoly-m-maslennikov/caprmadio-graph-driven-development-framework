---
subject_scope: artifact-model
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-266--use-one-canonical-subject-scope-per-meta-atom
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-248--three-artifact-forms
      - CAPRMEDIO-META-REQU-091--normative-atoms-are-the-caprmedio-specification
      - CAPRMEDIO-META-REQU-259--nonduplicative-current-artifact-properties
---

# Requirement — Generate the active META Atom Scope Catalog

A deterministic CAPRMEDIO generator owns one Markdown Catalog Projection with
stable identity `CAPRMEDIO-META-CATL-002--active-atoms-by-subject-scope`. The Projection groups every active
META Atom under its singular `subject_scope` in the canonical order declared by
META-124 and orders entries by `artifact_id` within each group.

Active discovery scans the META layer recursively and excludes any carrier
under `archive/` or `drafts/`, non-Markdown host files, and the generated
Projection itself. Every admitted source must have parseable YAML frontmatter,
a unique `artifact_id`, and exactly one allowed `subject_scope`. A missing,
legacy plural, unknown, multiple, or duplicate value stops generation without
changing the committed Projection.

The generated frontmatter declares:

- `artifact_type: catalog` and `artifact_subtype: requirement`;
- `artifact_id: CAPRMEDIO-META-CATL-002--active-atoms-by-subject-scope`;
- `scope_path: layer:meta` and `subject_scope: artifact-model`;
- a stable generator identity and format version;
- the number of included source Atoms; and
- a SHA-256 frontier digest over each ordered source's artifact ID and exact
  carrier digest.

The body contains only the canonical scope headings, source Atom IDs, and source
titles. It introduces no normative paraphrase, absolute path, generation time,
or manually maintained semantic content. The generator writes only when the
complete expected bytes differ, supports dry-run and check modes, and replaces
the target atomically after full preflight succeeds.

The Catalog is a non-authoritative Projection. Source Atoms remain the semantic
authority, and the generator implementation remains native project code.

## Primary claim

CAPRMEDIO deterministically regenerates one non-authoritative Catalog Projection
that groups every active META Atom exactly once by canonical Subject scope and
binds the result to an exact source frontier.

## Rationale

A generated Catalog provides the requested helicopter view without moving
Atoms, duplicating their claims, or creating another writable authority.
