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
    - CA-R-1076
    - CA-M-153
---
# Interactive HTML graph view behavior

## Claim checked

The single generated MRT renders current active Requirement Subject and lineage-section views from their STG Projections and actual Atom sources without becoming a second authority surface.

## Applicable conditions

1. Create current `stg_requirements_subjects.md` and `stg_requirements_lineage_sections.md` files in multiple active structural-unit roots, materialize the MRT, and require exactly one `.caprmedio/mrt_atoms.html` with embedded JavaScript and presentation assets and no sibling script, stylesheet, data, index, view, or per-Atom HTML files.
2. Require the MRT source-lineage manifest to name every consumed STG file and every underlying active Atom with canonical path and digest; require the Subject and lineage-section views to match the STG structure while node text, body, frontmatter, and live digest match the actual Atom.
3. Change registered project scope paths and require the structural-unit filter tree and discovered STG set to change without code modification; exercise tier, structural-unit, and Requirement-subtype filters and require no inactive Requirement to become visible.
4. Toggle RMED orphans and prove filtering never recomputes orphan status or invents an orphan merely because its neighbor is hidden.
5. In `short` mode, require `<scope>-<number> <Summary>` from the exact Atom H1, body without frontmatter in a panel above the node on first click, and complete raw Atom source including frontmatter on second click.
6. In `detailed` mode, require the same label plus the actual full body without frontmatter above the node and complete raw Atom source including frontmatter on one click.
7. Change one STG file and one Atom independently after MRT generation; require the embedded JavaScript to retrieve the current sources and visibly distinguish stale STG, stale MRT, and changed-Atom digest states.
8. Preserve filter and focused-node state in the URL, keep every identity linked to its canonical Atom path, and prove deleting `mrt_atoms.html` changes no Atom, STG Projection, or Journal.

## Acceptance criteria

Every selected active Requirement and direct edge appears in the correct Subject and lineage-section view, the one-file MRT declares complete STG-and-Atom lineage, every filter and display mode behaves deterministically, live interactions expose the required source forms and stale states, and the HTML remains non-authoritative.

## Failure disposition

Reject the MRT build, identify the first missing, extra, ambiguous, stale, incorrectly linked, or incorrectly interactive element, and retain the STG Requirement Projections as the preceding current derived views.
