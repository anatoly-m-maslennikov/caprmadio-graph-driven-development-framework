---
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 5
updated_at: 2026-08-23 17:53:53 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-1061
    - CA-R-1062
    - CA-R-1068
    - CA-M-146
---
# Requirement Lineage Map correctness

## Claim checked

The generated Lineage Map places each selected active Requirement exactly once under its complete reachable Principle-root set, preserves direct parent evidence, and orders lineage groups and Orphans deterministically.

## Applicable conditions

1. Build a fixture with Principles `REQU-002` and `REQU-003`, one Core under only `REQU-002`, one Core shared by both Principles, Standards below each Core, and one Standard below both Cores; place some descendants in a different selected structural unit from their Principle roots.
2. Generate the Map for the descendant structural unit, require exactly `<selected-structural-unit-root>/stg_requirements_lineage_sections.md`, and require ancestry to resolve through the complete active project graph while only selected-unit Requirements appear as displayed rows.
3. Require descendants rooted only in `REQU-002` under group `2`, shared descendants under `2+3`, and descendants rooted only in `REQU-003` under `3`; require group order `2`, `2+3`, `3` and require every Requirement exactly once with no copy of a shared descendant in `2` or `3`.
4. Add groups `2+4` and `10` and require numeric-vector order with a prefix before its extensions; inside each group require Principle, Core, and Standard tier order followed by numeric Requirement-ID order.
5. Require exactly the `TYPE + ID`, `Summary`, and `Child of` columns, canonical links for each `REQU-NNN`, exact first-H1 Summary text, and only direct authored `child_of` links sorted numerically rather than Principle ancestors or the group key.
6. Include a missing parent, inactive parent, wrong-tier edge, rootless chain, and cycle; require each affected selected Requirement once in the final `Orphans` section with the correct reason and nowhere in a lineage group.
7. Remove or duplicate a first H1 and require a build error; generate twice from one frontier and require byte-stable semantic output, then change a source and require currentness failure until the completed rebuild records the new frontier.

## Acceptance criteria

Every selected active Requirement appears exactly once in the correct numeric-vector lineage group or final Orphans section, with exact tier order, three columns, H1 Summary, direct parents, cross-scope ancestry, and deterministic currentness.

## Failure disposition

Reject the Lineage Map, retain the previous current Projection, report the first missing, duplicated, incorrectly rooted, misordered, stale, or malformed row, and record a Concern before publication.
