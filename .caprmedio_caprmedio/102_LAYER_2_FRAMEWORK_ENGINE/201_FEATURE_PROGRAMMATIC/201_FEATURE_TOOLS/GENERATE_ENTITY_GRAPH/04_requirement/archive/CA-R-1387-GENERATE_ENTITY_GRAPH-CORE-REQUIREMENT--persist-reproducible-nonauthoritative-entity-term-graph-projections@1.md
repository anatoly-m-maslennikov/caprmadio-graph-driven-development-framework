---
atom_id: CA-R-1387
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - projection-pipeline
version: 1
updated_at: 2026-09-04 03:10:59 +0400
relations: {}
---
# Persist reproducible non-authoritative Entity and Term graph Projections

`GENERATE_ENTITY_GRAPH` MUST accept one explicitly selected folder or equivalent source frontier and derive one reproducible, non-authoritative Projection. The result MUST contain every declared Term found in the parseable frontier; each Term's direct parent when declared; the direct dependency graph; the complete dependency-Term closure; cycles and relation-cardinality violations; source Carrier path and digest lineage; unknown or unparseable regions; the selected frontier identity; and an explicit non-authoritative status.

Identical readable source bytes and settings MUST produce byte-identical semantic output in stable order. Unknown or unparseable regions remain visible and MUST NOT be silently omitted, repaired, or interpreted as absence. A cycle or cardinality violation is reported as projection data and a failed validation disposition, never repaired by changing authority.

Description and ordinary generation are mutation-free. Persistence occurs only when the caller supplies an explicit output path or a registered Project setting resolves one unambiguous Projection destination. One output Carrier represents exactly one source frontier and is replaced atomically. The Tool MUST reject destinations inside governed Atom or Journal authority, path traversal, symlink escape, ambiguous configured destinations, and any request that would make the Projection authoritative.

The persisted Projection is suitable for strictly read-only consumption by `GRAPH_APP`, but Atoms and Journals remain the sole project source of truth.
