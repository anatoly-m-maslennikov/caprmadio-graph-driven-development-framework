---
subjects:
  governs: "Atom/Active History"
  depends_on:
    - "Projection"
    - "Artifact/Revision"
version: 13
updated_at: "2026-09-17 20:53:16 +0000"
llm_session_ids:
  - codex:019fc24e-24ed-7921-b4db-cf4df3e14bf7
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-R-1062
    - CA-R-1069
    - CA-M-148
---
# Active Atom history correctness

## Claim checked

the generated history reports a replayable daily active-Atom series whose total **and** Type, structural-level, **and** structural-unit rollups reconcile at **every** date.

## Test case

1. build a Git fixture spanning several dates **in** the configured timezone with dates that contain multiple commits **and** dates **without** commits; create, move, archive, **and** reactivate Atoms of multiple Types across structural units **and** change the topology **in** one historical revision.
2. generate the history **and** require exactly `<project-control-root>/biz_atoms_active_history.md`, the last authoritative revision at **or** **before** each date's end, **and** carry-forward values on dates **without** a new revision.
3. for **every** date require one correct grand total, **all** registered Type, structural-level, **and** structural-unit members including zero counts, **and** **every** dimension rollup sum equal **to** the date's grand total.
4. require lifecycle **and** topology interpretation from each historical revision rather than the current working tree; alter filesystem timestamps **without** changing Git history **and** require byte-identical semantic output.
5. add an uninterpretable historical carrier **without** a compatibility rule **and** require a build error; **then** provide the governed rule **and** require the correct replayed count.
6. generate twice from one Git frontier, date range, timezone, **and** configuration **and** require byte-stable semantic output; extend the frontier **and** require currentness failure **until** the completed atomic rebuild records it.

## Acceptance criteria

**every** reporting date uses the correct authoritative revision **and** exposes exact, zero-inclusive, reconciling active-Atom totals **and** rollups with deterministic replay **and** currentness.

## Failure disposition

reject the history, retain the previous Projection bytes for recovery **without** treating retention as proof of currentness; classify those bytes against their own source frontier under CA-R-1062, report the first missing date, wrong frontier, malformed historical carrier, incorrect lifecycle interpretation, non-reconciling count, **or** stale result, **and** record a Concern **before** publication.

## Sources

- [CA-R-1062 — Validate Projection currentness](../04_requirement/CA-R-1062-TOOLS-REQUIREMENT--validate-projection-currentness.md)
- [CA-R-1069 — Generate active Atom history](../04_requirement/CA-R-1069-TOOLS-REQUIREMENT--generate-active-atom-history.md)
