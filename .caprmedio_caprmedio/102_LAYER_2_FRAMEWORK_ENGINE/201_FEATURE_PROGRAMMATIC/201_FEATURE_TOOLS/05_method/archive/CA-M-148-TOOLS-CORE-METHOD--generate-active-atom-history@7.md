---
subjects:
  governs:
    continuant:
      - projection-pipeline
version: 7
updated_at: 2026-08-30 16:44:07 +0400
llm_session_ids:
  - codex:019fc24e-24ed-7921-b4db-cf4df3e14bf7
relations:
  method_for:
    - CA-R-1062
    - CA-R-1069
---
# Generate active Atom history

Generate the active Atom history through this procedure:

1. Resolve the configured Artifact timestamp timezone and the authoritative first-parent Git revision frontier. Use calendar dates in that timezone; never use carrier filesystem creation or modification times as historical evidence.
2. For every calendar date from the first authoritative revision through the requested end date, select the last authoritative revision at or before that date's end and carry the preceding revision forward across dates without a new revision.
3. At each selected revision, resolve the structural topology, Type registry, canonical Atom addresses, and registered lifecycle placement from that revision. Count every active Atom exactly once and fail closed when the historical revision cannot be interpreted without a declared compatibility rule.
4. For every reporting date compute one grand total and complete independent rollups by canonical Type, structural level, and structural unit. Emit registered zero-count members and require every rollup for that date to sum to its grand total.
5. Bind the output to `<project-control-root>/biz_atoms_active_history.md` and emit one stably ordered long-form table with `date`, `dimension`, `member`, and `active_atom_count`, where `dimension` is exactly `total`, `type`, `structural_level`, or `structural_unit`.
6. Bind the Git frontier, reporting range, timezone, historical compatibility configuration, generator version, and source digests; replace the Projection atomically, record the completed rebuild through the Work Journal, and require byte-stable semantic output from the same frontier before reporting the history current.
