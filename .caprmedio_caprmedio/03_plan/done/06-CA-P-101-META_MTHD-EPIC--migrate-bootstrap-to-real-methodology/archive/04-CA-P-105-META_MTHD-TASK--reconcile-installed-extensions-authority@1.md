---
atom_id: CA-P-105
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Applicable Methodology/Sources/Installed Extensions
    occurrent:
      - Extension Authority Reconciliation
  depends_on:
    occurrent:
      - CA-P-104
version: 1
updated_at: 2026-08-26 04:35:53 +0400
autonomous_confidence_threshold: 98
relations: {}
---
# Reconcile Installed Extensions Authority

**when** CA-P-104 is Done, **then** the Assignee **must** reconcile 002_INSTALLED_EXTENSIONS as the immutable installed Extension source Layer of Applicable Methodology.

## Scope

`(all active and draft Atoms, manifests, catalogs, and provenance records that govern Extension identity, version, Author, Source, Source Version, immutable origin, installation, dependency and compatibility declarations, CAPRMEDIO_FOR_CAPRMEDIO, and other installed Extension authority)`

## Definition of Done

the Task is **not done if** (an installed Extension lacks immutable identity, version, Author, Source, Source Version, or origin provenance **or** installation makes an Extension applicable without Local Configuration **or** an installed Extension Carrier is locally mutated **or** CAPRMEDIO_FOR_CAPRMEDIO remains modeled as CAPRMEDIO_APPLICATION instead of an Extension **or** Project installation state is duplicated into every Extension Atom **or** Extension-supplied compatibility declarations and Project-owned compatibility resolutions are conflated).

## Details

preserve installed Extension authority at its original provenance boundary. installation admits an available immutable source; it does not activate, customize, replace, prioritize, or resolve that source for the current Project.
