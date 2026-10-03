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
      - CA-P-112
version: 3
updated_at: 2026-08-26 17:42:48 +0400
autonomous_confidence_threshold: 98
relations: {}
---
# Reconcile Core Meta-Model Authority

**when** CA-P-112 is Done, **then** the Assignee **must** reconcile 001_CORE_META_MODEL so it provides the minimal self-applicable canonical model necessary and sufficient to represent, govern, validate, and compile CAPRMEDIO Methodology authority.

## Scope

`(all active and draft Atoms in the frozen CA-P-102 source frontier, regardless of current Carrier or Current Scope, that govern or are candidates to govern Project Graphs, Entity Graphs, Nodes, Entities, relations, Artifacts, Carriers, Atom Content Roles, internal, external, and relational Atom classification, lifecycle and core Status models, Type registration or defaults, identity, revision, provenance, Extension and Local Configuration models, Applicable Methodology compilation, or recursive self-application)`

## Definition of Done

the Task is **not done if** (any general invariant has no single current owner **or** any independently replaceable Claim remains combined **or** any admitted Core Meta-Model Claim is unnecessary to its Job **or** the remaining Core Meta-Model authority is insufficient to satisfy its complete Job **or** any Core Meta-Model Claim depends on a later source Layer **or** the Core Meta-Model cannot represent its own Atoms and Dependent Entities **or** it cannot represent and govern Extension, Local Configuration, Applicable Methodology, compilation, or carrier concepts required by the later Tasks **or** a proposed default Type is accepted below the Autonomous Confidence Threshold).

## Details

place only authority required by the CORE_META_MODEL Job in 001_CORE_META_MODEL. treat a Claim as necessary only when removing it prevents satisfaction of a required Core model capability, and treat the Core as sufficient only when no additional canonical Claim is required to represent, govern, validate, or compile the methodology system. place replaceable or optional CAPRMEDIO-specific authority in an installed Extension, including CAPRMEDIO_FOR_CAPRMEDIO where applicable. leave activation, Customization, replacement, priority, compatibility resolution, and local mode selection to 003_LOCAL_CONFIGURATION.
