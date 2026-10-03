---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "projection-pipeline"
  depends_on: []
version: 8
updated_at: "2026-09-23 04:25:00 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Persist reproducible non-authoritative Entity and Term graph Projections

`GENERATE_ENTITY_GRAPH` **must** accept one explicitly selected folder **or** equivalent source frontier **and** derive one reproducible, non-authoritative Projection. The result **must** contain **every** declared Term found **in** the parseable frontier; each Term's direct parent **when** declared; the direct dependency graph; the complete dependency-Term closure; cycles **and** relation-cardinality violations; source Carrier path **and** digest lineage; unknown **or** unparseable regions; the selected frontier identity; **and** an explicit non-authoritative status.

Identical readable source bytes **and** settings **must** produce byte-identical semantic output **in** stable order. Unknown **or** unparseable regions remain visible **and** **must not** be silently omitted, repaired, **or** interpreted as absence. A cycle **or** cardinality violation is reported as projection data **and** a failed validation disposition, never repaired by changing authority.

Description **and** ordinary generation are mutation-free. Persistence occurs **only** **when** the caller supplies an explicit output path **or** a registered Project setting resolves one unambiguous Projection destination. One output Carrier represents exactly one source frontier **and** is replaced atomically. The Tool **must** reject destinations inside governed Atom **or** Journal authority, path traversal, symlink escape, ambiguous configured destinations, **and** **any** request that would make the Projection authoritative.

the persisted Projection is suitable for strictly read-only consumption by `GRAPH_SERVER` and optional presentation by `GRAPH_UI`, but it has no authority of its own: current Atoms, Journals, authoritative Settings Artifacts, **and** **any** other authority admitted by the applicable methodology remain authoritative independently of the Projection.
