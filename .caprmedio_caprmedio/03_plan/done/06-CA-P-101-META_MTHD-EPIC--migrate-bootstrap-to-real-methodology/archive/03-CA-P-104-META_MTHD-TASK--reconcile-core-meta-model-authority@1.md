---
atom_id: CA-P-104
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Applicable Methodology/Sources/Core Meta-Model
    occurrent:
      - Authority Reconciliation
  depends_on:
    occurrent:
      - CA-P-103
version: 1
updated_at: 2026-08-26 04:35:53 +0400
autonomous_confidence_threshold: 98
relations: {}
---
# Reconcile Core Meta-Model Authority

**when** CA-P-103 is Done, **then** the Assignee **must** reconcile 001_CORE_META_MODEL as the canonical self-hosting source Layer of Applicable Methodology.

## Scope

`(all active and draft BSEED Atoms that govern Project Graphs, Entity Graphs, Nodes, Entities, relations, Artifacts, Carriers, Atom Content Roles, internal, external, and relational Atom classification, lifecycle and core Status models, Type registration or defaults, identity, revision, provenance, Extension and Local Configuration models, and recursive self-application)`

## Definition of Done

the Task is **not done if** (any general invariant has no single current owner **or** any independently replaceable Claim remains combined **or** any Core Meta-Model Claim depends on a later source Layer **or** the Core Meta-Model cannot represent its own Atoms and Dependent Entities **or** it cannot define Extension, Local Configuration, Applicable Methodology, compilation, or carrier concepts required by the later Tasks **or** a proposed default Type is accepted below the Autonomous Confidence Threshold).

## Details

place only canonical self-hosting authority in 001_CORE_META_MODEL. place replaceable or optional CAPRMEDIO-specific authority in an installed Extension, including CAPRMEDIO_FOR_CAPRMEDIO where applicable. leave activation, Customization, replacement, priority, compatibility resolution, and local mode selection to 003_LOCAL_CONFIGURATION.
