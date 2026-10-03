---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 5
updated_at: 2026-08-23 11:39:04
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-1059
    - CA-R-1061
    - CA-R-1062
    - CA-M-145
---
# Requirement Subject Catalog correctness

## Claim checked

The generated Subject Catalog contains exactly the selected structural unit's active Requirements, grouped by authored Subject and ordered by tier, with precise source-derived columns and Orphans last.

## Applicable conditions

1. Build a fixture with active Principle, Core, and Standard Requirements in at least two Subjects and structural units; include inactive Requirements, multiple numeric IDs, one cross-scope valid parent, one missing parent, one inactive parent, one wrong-tier parent, and one cycle.
2. Generate the Catalog for one structural unit, require exactly `<selected-structural-unit-root>/stg_requirements_subjects.md`, and require only that unit's active Requirements as rows while validating their parents against the complete active project graph.
3. Require non-orphans under the governed Subject order, then Principle, Core, and Standard subsections, with numeric Requirement-ID ordering inside every tier; require one final `Orphans` section containing every structurally unplaceable selected Requirement once with the correct reason.
4. Require exactly the `TYPE + ID`, `Summary`, and `Child of` columns. Require each `REQU-NNN` identity and every direct `child_of` target to link to its canonical Atom, and require multiple parents to be numerically ordered without ancestor substitution.
5. Give a Requirement an H1 that differs from its filename and require the H1 text verbatim in `Summary`; remove or duplicate the first H1 and require a build error rather than a filename fallback.
6. Generate twice from the same structural unit, source frontier, and configuration and require byte-stable semantic output; modify one source and require currentness failure until an atomic rebuild records the new frontier, digest, timestamp, and Work Journal event.

## Acceptance criteria

The Catalog has the exact selected active row set, Subject and tier ordering, three columns, H1 Summaries, direct parent links, and final orphan placement, and it becomes current only through a deterministic completed rebuild.

## Failure disposition

Reject the Catalog, retain the previous current Projection, report the first missing, extra, stale, misordered, malformed, or misclassified row, and record a Concern before publication.
