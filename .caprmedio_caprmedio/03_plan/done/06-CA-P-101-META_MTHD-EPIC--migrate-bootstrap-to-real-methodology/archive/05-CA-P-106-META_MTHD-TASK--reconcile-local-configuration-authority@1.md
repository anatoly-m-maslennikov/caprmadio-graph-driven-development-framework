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
version: 1
updated_at: 2026-08-26 04:35:53 +0400
autonomous_confidence_threshold: 98
relations: {}
---
# Reconcile Local Configuration Authority

**when** CA-P-105 is Done, **then** the Assignee **must** reconcile 003_LOCAL_CONFIGURATION as the Project-owned source of Extension selection, Customization, resolution, and local mode decisions for Applicable Methodology.

## Scope

`(all active and draft Atoms, configurations, manifests, and provenance records that govern current Project identity, Extension activation, selected Extension version, Project Customization, replacement, priority, compatibility resolution, local Tool, MCP, and App modes, and Applicable Methodology source selection)`

## Definition of Done

the Task is **not done if** (Local Configuration does not identify exactly one current Project **or** an installed but inactive Extension contributes to Applicable Methodology **or** a Project Customization mutates an installed Extension Atom **or** activation, selected version, replacement, priority, compatibility resolution, or local mode decisions lack Project-owned authority **or** Local Configuration duplicates immutable Extension content **or** one decision requires unfinished compiled output to establish its own validity).

## Details

represent every local modification as a separate Project Customization Atom with exact relations to the authority it customizes. keep every selection and resolution decision Project-owned. use only Core Meta-Model and immutable installed Extension authority as prerequisites of Local Configuration.
