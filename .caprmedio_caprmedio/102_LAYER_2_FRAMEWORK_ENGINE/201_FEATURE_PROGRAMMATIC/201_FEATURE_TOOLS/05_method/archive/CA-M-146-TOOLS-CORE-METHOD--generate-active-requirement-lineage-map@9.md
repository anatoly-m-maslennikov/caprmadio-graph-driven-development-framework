---
subjects:
  governs:
    continuant:
      - projection-pipeline
version: 9
updated_at: 2026-08-30 16:44:07 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  method_for:
    - CA-R-1061
    - CA-R-1062
    - CA-R-1068
---
# Generate active Requirement Lineage Map

Generate the Lineage Map through this procedure:

1. Resolve exactly one requested structural unit from the common selectors, bind the output to `<selected-structural-unit-root>/stg_requirements_lineage_sections.md`, and select every active Requirement in that unit for displayed rows, but build and validate ancestry from the complete active project Requirement graph so a selected Layer or Feature retains Principle ancestry declared outside its own scope.
2. Treat each Principle as its own lineage root. Traverse only direct authored `child_of` Requirement edges upward; require every Core Requirement parent to be a Principle and every Standard Requirement parent to be a Core, and classify missing, inactive, wrong-tier, cyclic, or rootless Requirements as Orphans with explicit reasons.
3. For each non-orphan Requirement, compute the sorted unique set of all reachable Principle Requirement numbers. Name its group by joining those unpadded numbers with `+`, so descendants of only `REQU-002` belong to `2` and descendants shared by `REQU-002` and `REQU-003` belong once to `2+3` rather than also appearing in `2` or `3`.
4. Sort group names lexicographically as integer vectors, with an exhausted prefix before any extension: `2`, `2+3`, `2+4`, `3`. Within each group emit Principle, Core, and Standard subsections in that order and sort rows within each tier by numeric Requirement ID.
5. Require one parseable first level-one heading per displayed Requirement and use its text after `# ` verbatim as `Summary`; fail the build when it is missing or ambiguous and never use filename text.
6. Emit exactly three columns: `TYPE + ID`, `Summary`, and `Child of`. Link `TYPE + ID` as `REQU-NNN` to the canonical Atom; link the direct authored `child_of` targets in `Child of`, sorted numerically; never substitute reachable ancestors or the lineage group key.
7. After all normal lineage groups, emit exactly one final `Orphans` section. Retain tier and numeric ordering inside it, and include each orphan reason without adding a fourth table column.
8. Bind the selected structural unit, exact complete-graph Atom source frontier, generator version, configuration, source digests, and `updated_at`; replace `stg_requirements_lineage_sections.md` atomically in that structural-unit root, record the completed Work Journal event, and prove byte-stable semantic output from the same frontier before reporting it current.
