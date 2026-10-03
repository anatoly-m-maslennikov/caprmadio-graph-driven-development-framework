---
atom_id: CA-P-106
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Applicable Methodology/Sources/Local Configuration
    occurrent:
      - Configuration Authority Reconciliation
  depends_on:
    occurrent:
      - CA-P-105
version: 2
updated_at: 2026-08-26 16:23:41 +0400
autonomous_confidence_threshold: 98
relations: {}
---
# Reconcile Local Configuration Authority

**when** CA-P-105 is Done, **then** the Assignee **must** reconcile 003_LOCAL_CONFIGURATION so it states the Project-owned Customizations and composition decisions that select active Installed Extensions and resolve their compatibility, priority, and replacement for compilation with CORE_META_MODEL.

## Scope

`(all active and draft Atoms, configurations, manifests, and provenance records that govern current Project identity, Extension activation, selected Extension version, Project Customization, replacement, priority, compatibility resolution, local Tool, MCP, and App modes, and Applicable Methodology source selection)`

## Definition of Done

the Task is **not done if** (Local Configuration does not identify exactly one current Project **or** it cannot determine one complete ordered source frontier for compilation with CORE_META_MODEL **or** an installed but inactive Extension contributes to Applicable Methodology **or** a Project Customization mutates CORE_META_MODEL or an installed Extension Atom **or** activation, selected version, replacement, priority, compatibility resolution, or local mode decisions lack Project-owned authority **or** Local Configuration duplicates immutable Core Meta-Model or Extension content **or** one decision requires unfinished compiled output to establish its own validity).

## Details

represent every local modification as a separate Project Customization Atom with exact relations to the authority it customizes. keep every selection and resolution decision Project-owned. make the resolved composition complete enough for deterministic compilation, but do not duplicate or mutate CORE_META_MODEL or immutable installed Extension authority. use only those two authoritative source Layers as prerequisites of Local Configuration.
