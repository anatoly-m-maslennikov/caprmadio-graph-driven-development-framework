---
subject_scopes:
  - projection-pipeline
version: 5
updated_at: 2026-08-23 11:39:04
llm_session_ids:
  - codex:019fc24e-24ed-7921-b4db-cf4df3e14bf7
relations:
  method_for:
    - CA-R-1060
    - CA-R-1061
    - CA-R-1062
---
# Generate current active Atom snapshot

Generate the current active Atom snapshot through this procedure:

1. Resolve the complete current project structural topology and canonical Type registry, enumerate Atom carriers through the canonical address resolver, and derive active state from each Type's registered lifecycle placement rather than from frontmatter, filename text, or filesystem timestamps.
2. Assign every active Atom exactly one canonical Type, one structural level, and one structural unit. Fail closed on an unknown, ambiguous, malformed, duplicated, or topologically unregistered carrier instead of omitting or double-counting it.
3. Compute one grand total and three complete independent rollups: active Atoms by canonical Type, by structural level, and by structural unit. Emit every registered dimension member, including members with a zero count, and require each rollup to sum to the grand total.
4. Bind the output to `<project-control-root>/biz_atoms_current_snapshot.md` and emit the declared source frontier and as-of timestamp followed by `Total`, `By Type`, `By structural level`, and `By structural unit` sections with stably ordered rows and integer `active_atom_count` values.
5. Bind the exact carrier frontier, lifecycle and topology configuration, generator version, source digests, and `updated_at`; replace the Projection atomically and record the completed rebuild through the Work Journal.
6. Regenerate from the same frontier and configuration and require byte-stable semantic output before reporting the snapshot current.
