---
subject_scopes:
  - artifact-model
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-267--generate-the-active-meta-atom-scope-catalog
  child_of:
    - CAPRMEDIO-META-REQU-091--normative-atoms-are-the-caprmedio-specification
    - CAPRMEDIO-META-REQU-106--keep-meta-and-gov-implementation-neutral
---
# Provide the active META Atom Scope Catalog

CAPRMEDIO provides one current, non-authoritative Catalog Projection that lists
every active META Atom under each of its canonical `subject_scopes` and in the
Subject-scope order governed by META. An Atom appears exactly once within each
declared scope and may therefore appear in more than one Catalog section.

The Catalog is bound to an exact source frontier and distinguishes a current
result from a stale or incomplete result. Draft Atoms, archived Atoms, and
completed Plans under `done/` are excluded from the active view. A missing,
empty, unknown, or duplicate source identity or Subject scope prevents the
Catalog from claiming currentness.

The Catalog presents source Atom identities and human-readable labels without
paraphrasing their claims or establishing normative truth. Its carrier format,
serialization, source-digest algorithm, generation mechanism, storage path,
and replacement mechanics are governed downstream rather than by META.
