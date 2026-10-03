---
artifact_subtype: change_plan
subject_scopes:
  - development-flow
version: 6
updated_at: 2026-08-24 04:47:00
---
# Implement the FRAMEWORK_ENGINE in vertical slices

1. Reconcile the selected FRAMEWORK_ENGINE Requirements, Methods, Evaluations, and Deliveries with the final SKILLS, TOOLS, and APPS Feature structure before implementing them.
2. Implement the common CLI and Tool router in the one shared environment under `.caprmedio_runtime`, including capability discovery and sufficient usage instructions for every selected Tool.
3. Implement read-only Finders first, including Checkers for carrier structure, frontmatter, filenames, placement, relations, topology, generated-data currentness, and repository hygiene.
4. Implement Doers through the same interface. Every Doer must accept Structural-unit, Type, subtype, and single-filename inputs, produce a complete dry run, and change only declared sources or derived outputs after explicit application.
5. Implement programmatic Projection generators for Requirement Subject and lineage-section Markdown, active-Atom business snapshots and history, and every other accepted deterministic view.
6. Implement declarative standing project briefs for questions such as current architecture, open risks, and in-flight work as current non-authoritative Markdown Projections. Each brief must preserve its declared question, source identities, source frontier, and currentness state; regenerate deterministically when its source graph changes; and never establish or rewrite project authority.
7. Implement `GRAPH_APP` as a source indexer, rebuildable derived database, local read-only server, and interconnected web interface; implement agent-host plugin packages under `AGENT_HOST_PLUGINS`, beginning with `CODEX_PLUGIN`, without duplicating provider-neutral Skill or Tool behavior. Atoms and Journals remain the source; the database and views remain disposable and rebuildable. Select the database engine through a separate accepted Method before binding the implementation.
8. Make Skills the primary operator and LLM interface to FRAMEWORK_METHODOLOGY and the Engine while preserving direct CLI access for operators.
9. Add deterministic Tests and Evaluations as one case per Evaluation Atom, cover each vertical slice end to end, and keep all cache, logs, backups, database state, and service state under `.caprmedio_runtime`.
10. Finish with one natural-language request that routes through a Skill, finds governed context, dry-runs and applies a source change, validates it, refreshes projections and the `GRAPH_APP` read model, and records the result through the Work Journal.
