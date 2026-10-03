---
subjects:
  governs: "Atom/Current Active Snapshot"
  depends_on:
    - "Projection"
    - "Artifact/Revision"
version: 12
updated_at: "2026-09-17 20:53:10 +0000"
llm_session_ids:
  - codex:019fc24e-24ed-7921-b4db-cf4df3e14bf7
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-R-1060
    - CA-R-1061
    - CA-R-1062
    - CA-M-147
---
# Current active Atom snapshot correctness

## Claim checked

the generated current snapshot counts **every** active Atom exactly once **and** reports reconciling totals by canonical Type, structural level, **and** structural unit at one declared current source frontier.

## Test case

1. build a fixture containing active **and** inactive Atoms of multiple Types across Project, Layer, **and** Feature structural units, including zero-count registered dimension members, one malformed carrier, **and** one duplicate identity.
2. generate the snapshot **without** the malformed **and** duplicate carriers **and** require exactly `<project-control-root>/biz_atoms_current_snapshot.md`, the correct grand total, **every** registered Type, structural level, **and** structural unit, explicit zero counts, **and** each rollup sum equal **to** the grand total.
3. move an Atom between active **and** inactive registered lifecycle placements **and** require the total **and** **every** affected rollup **to** change by exactly one **without** reading lifecycle state from frontmatter.
4. restore the malformed **or** duplicate carrier **and** require a build error rather than omission, guessing, **or** double counting.
5. generate twice from one frontier **and** require byte-stable semantic output; change one carrier **or** topology setting **and** require currentness failure **until** a completed atomic rebuild records the new frontier.

## Acceptance criteria

the snapshot exposes the exact active population, complete zero-inclusive dimension rollups, internally reconciling totals, deterministic ordering, **and** currentness bound **to** one source frontier.

## Failure disposition

reject the snapshot, retain the previous Projection bytes for recovery **without** treating retention as proof of currentness; classify those bytes against their own source frontier under CA-R-1062, report the first missing, duplicated, malformed, misclassified, non-reconciling, **or** stale result, **and** record a Concern **before** publication.

## Sources

- [CA-R-1060 — Generate current active Atom snapshot](../04_requirement/CA-R-1060-TOOLS-REQUIREMENT--generate-current-active-atom-snapshot.md)
- [CA-R-1061 — Rebuild one programmatic Projection](../04_requirement/CA-R-1061-TOOLS-REQUIREMENT--rebuild-one-programmatic-projection.md)
- [CA-R-1062 — Validate Projection currentness](../04_requirement/CA-R-1062-TOOLS-REQUIREMENT--validate-projection-currentness.md)
