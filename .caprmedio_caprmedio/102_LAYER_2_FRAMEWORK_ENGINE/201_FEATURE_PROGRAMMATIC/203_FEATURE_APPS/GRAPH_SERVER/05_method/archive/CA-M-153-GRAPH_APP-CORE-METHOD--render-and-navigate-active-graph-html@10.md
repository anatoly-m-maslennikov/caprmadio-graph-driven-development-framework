---
subjects:
  governs:
    continuant:
      - projection-pipeline
version: 10
updated_at: 2026-08-30 16:44:07 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  method_for:
    - CA-R-1076
  derived_from:
    - CA-A-057
---
# Render and navigate active graph HTML

Render and use the active graph views through this procedure:

1. Discover the applicable active structural units from current project topology and require one current `stg_requirements_subjects.md` and one current `stg_requirements_lineage_sections.md` in each selected structural-unit root.
2. Use the Subject STG files for Subject, tier, and orphan placement; use the lineage-section STG files for Principle-root sections and direct Requirement relations; and read the actual active Atom Markdown for canonical identity, first-H1 Summary, body, frontmatter, path, and current digest. Reject a missing STG, inconsistent STG pair, unresolved Atom, or STG-to-Atom digest mismatch.
3. Materialize exactly one `.caprmedio/mrt_atoms.html` file by atomic replacement. Embed all JavaScript and presentation assets in that file, generate no sibling JavaScript, CSS, data, index, view, or per-Atom HTML files, and keep service state only under `.caprmedio_runtime`.
4. Embed a machine-readable source-lineage manifest covering every consumed STG file, every underlying Atom, their source-frontier relation, canonical paths, and digests. The embedded JavaScript must use the read-only graph-source service to retrieve current STG and Atom content rather than treating embedded HTML text as authority.
5. Derive the structural-unit filter tree from current registered scope paths and expose tier, structural-unit, and Requirement-subtype filters plus a show-or-hide control for RMED orphans. Preserve complete-graph orphan classification when a display filter hides a neighbor.
6. Let the HTML setting select `short` or `detailed` initial node display. A short node shows `<scope>-<number> <Summary>` from the exact first H1; its first click shows the actual current body without frontmatter in a panel above the node and its second click shows complete raw Markdown including frontmatter. A detailed node initially shows that body above the label and one click shows complete raw Markdown.
7. Compare every live STG and Atom digest with the lineage manifest, visibly identify stale STG, stale MRT, and unavailable-source states, preserve filters and focused-node state in the URL, and keep each identity linked to its canonical source path.
