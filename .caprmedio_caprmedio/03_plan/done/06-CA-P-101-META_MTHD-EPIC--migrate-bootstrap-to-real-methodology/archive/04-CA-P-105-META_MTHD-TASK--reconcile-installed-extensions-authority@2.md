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
version: 2
updated_at: 2026-08-26 16:23:41 +0400
autonomous_confidence_threshold: 98
relations: {}
---
# Reconcile Installed Extensions Authority

**when** CA-P-104 is Done, **then** the Assignee **must** reconcile 002_INSTALLED_EXTENSIONS so it preserves exact installed Extension source revisions and their provenance as immutable candidate inputs to methodology compilation without activating or modifying them.

## Scope

`(all active and draft Atoms, manifests, catalogs, Carriers, and provenance records in the frozen CA-P-102 source frontier that govern Extension identity, version, Author, Source, Source Version, immutable origin, installation, dependency and compatibility declarations, CAPRMEDIO_FOR_CAPRMEDIO, and other installed Extension authority)`

## Definition of Done

the Task is **not done if** (an installed Extension lacks immutable identity, exact source revision, version, Author, Source, Source Version, origin provenance, or a reproducible content digest **or** an installed Extension is unavailable to Local Configuration as a candidate input **or** installation makes an Extension applicable without Local Configuration **or** an installed Extension Carrier is locally mutated **or** CAPRMEDIO_FOR_CAPRMEDIO remains modeled as CAPRMEDIO_APPLICATION instead of an Extension **or** Project installation state is duplicated into every Extension Atom **or** Extension-supplied compatibility declarations and Project-owned compatibility resolutions are conflated).

## Details

preserve installed Extension authority at its exact original provenance boundary. installation admits an available immutable candidate source; it does not activate, customize, replace, prioritize, or resolve that source for the current Project. keep every Project-owned decision outside 002_INSTALLED_EXTENSIONS.
