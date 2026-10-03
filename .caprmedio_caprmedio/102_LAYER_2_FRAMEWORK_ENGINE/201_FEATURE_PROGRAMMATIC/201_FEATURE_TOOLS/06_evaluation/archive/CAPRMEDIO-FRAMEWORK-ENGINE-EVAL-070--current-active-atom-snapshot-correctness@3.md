---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 3
updated_at: 2026-08-23 11:39:04
llm_session_ids:
  - codex:019fc24e-24ed-7921-b4db-cf4df3e14bf7
relations:
  evaluation_for:
    - CA-R-1060
    - CA-R-1061
    - CA-R-1062
    - CA-M-147
---
# Current active Atom snapshot correctness

## Claim checked

The generated current snapshot counts every active Atom exactly once and reports reconciling totals by canonical Type, structural level, and structural unit at one declared current source frontier.

## Applicable conditions

1. Build a fixture containing active and inactive Atoms of multiple Types across Project, Layer, and Feature structural units, including zero-count registered dimension members, one malformed carrier, and one duplicate identity.
2. Generate the snapshot without the malformed and duplicate carriers and require exactly `<project-control-root>/biz_atoms_current_snapshot.md`, the correct grand total, every registered Type, structural level, and structural unit, explicit zero counts, and each rollup sum equal to the grand total.
3. Move an Atom between active and inactive registered lifecycle placements and require the total and every affected rollup to change by exactly one without reading lifecycle state from frontmatter.
4. Restore the malformed or duplicate carrier and require a build error rather than omission, guessing, or double counting.
5. Generate twice from one frontier and require byte-stable semantic output; change one carrier or topology setting and require currentness failure until a completed atomic rebuild records the new frontier.

## Acceptance criteria

The snapshot exposes the exact active population, complete zero-inclusive dimension rollups, internally reconciling totals, deterministic ordering, and currentness bound to one source frontier.

## Failure disposition

Reject the snapshot, retain the previous current Projection, report the first missing, duplicated, malformed, misclassified, non-reconciling, or stale result, and record a Concern before publication.
