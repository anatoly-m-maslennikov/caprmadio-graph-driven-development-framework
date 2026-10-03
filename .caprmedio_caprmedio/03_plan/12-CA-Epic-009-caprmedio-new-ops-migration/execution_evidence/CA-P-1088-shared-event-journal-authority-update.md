# Shared event Journal authority update

Operator-directed source-content update, 2026-09-14 01:17:47 +0400. This is non-authoritative execution evidence, not a second Journal. The accepted design is one authoritative logical event table per Project, with artifact-change and Process-execution logs derived as Projections of its admitted records.

## Changes

- META656 v10 defines the logical event-record table, keeps event versus record distinct, preserves append-only history and separates historical evidence from current Atom Claims.
- META158 v10 requires one Project Journal and one canonical admitted record for each recorded event; distinct events within one execution remain distinct.
- D339 v7 clarifies that existing NDJSON segments materialize the same logical table. No storage format, path, database, or schema changes.
- R1463 v1 requires both log views to derive their historical facts and event references from the shared Journal. One event may appear in both; read-only executions need no invented Artifact change. This is a General rule for Journal-derived Projections, not a new Type, alias, or generic Process.
- GOV-EVAL-003 v12 extends the existing storage-boundary check with explicit shared-event/view fixtures. Existing checks and the aggregate threshold are preserved; the mandatory Journal-view gate cannot be hidden by that score. Its checked Subject is Carrier, replacing the obsolete generic evaluation label.
- P1088 v2 and P983 v3 receive administrative alignment only. Both remain Active, prerequisites unchanged; no Task is executed or marked Done.

## Boundaries

Exact predecessors are preserved in their existing archive directories. There is no replacement or absorption, so the M274 exception is not used. Current Journal history is retained and new actual update receipts are appended through the existing canonical appender. The Tool event schema, replacement-lineage fields, concrete log builders, stored event data, settings, generated Applicable Methodology and Git remain unchanged. M224 extraction is still unapplied and blocked on its separate replacement-lineage carrier decision. R1462/D433/D434/O004-O011 reservations remain untouched.

One reviewer independently checked current Journal/Projection authority and the two Task boundaries; the root retained the existing general Projection model rather than introduce a speculative Journal Log Type. A Journal record remains evidence, not its event or automatic proof of the claimed outcome.

## Verification

The source frontier before this amendment is 1,565, with 53 excluded Drafts. Four existing source revisions and one new R yield 1,566 active admitted sources. Fifteen prior ordered maps stay immutable. Validation checks exact predecessor bytes, restricted source/body changes, direct Subject encoding on touched source Atoms, new-ID admission, unchanged Task dependency gates, all unrelated source and baseline files, and the current Git index. Source-content/fixture-definition validation is not execution of a log builder or the newly specified Evaluation cases.
